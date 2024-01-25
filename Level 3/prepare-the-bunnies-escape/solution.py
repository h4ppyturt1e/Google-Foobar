from time import time
from collections import deque

def getShortestPath(adjMatrixValid, start, end):
    # Queue for BFS
    queue = deque([start])
    # Track visited nodes
    visited = set()
    visited.add(start)
    # Track the previous node for each visited node
    prev = {start: None}

    # BFS
    while queue:
        node = queue.popleft()
        # Stop if the end node is reached
        if node == end:
            break
        # Add unvisited neighbors to the queue
        for neighbor in adjMatrixValid[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                prev[neighbor] = node

    # Reconstruct the shortest path
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    return path if path[0] == start else []

def solution(maze):
    adjMatrixValid, adjMatrixInvalid = generateAdjacencyMatrix(maze)
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    # print(f'adjMatrixValid = {adjMatrixValid[(0, 0)]}')
    
    shortest = float('inf')
    shortestSoln = []
    
    # get path to end
    visited = getShortestPath(adjMatrixValid, start, end)
    
    # check if end is reachable
    if (len(maze) - 1, len(maze[0]) - 1) in visited:
        # print(visited)
        # print('end is reachable')
        shortest = len(visited)
        shortestSoln = visited
        
    # if able to break 1 wall, check all possible walls
    for node in visited:
        # get surrounding invalid nodes
        invalidNodes = adjMatrixInvalid[node]
        # print(f'invalidNodes = {invalidNodes}')
        
        for wall in invalidNodes:
            # remove wall
            # print(f"removing wall at {wall} -> {node}")
            adjMatrixValid[node][wall] = True
            
            # get path to end
            visited = getShortestPath(adjMatrixValid, start, end)
            
            # check if end is reachable
            if (len(maze) - 1, len(maze[0]) - 1) in visited:
                # print(visited)
                # print('end is reachable')
                shortest = min(shortest, len(visited))
                shortestSoln = visited
            # replace wall
            adjMatrixValid[wall][node] = False
    
    # visualizeMaze(maze, shortestSoln)
    return shortest

def generateAdjacencyMatrix(maze):
    # maze[0][0] -> [(maze[0][1], True), (maze[1][0], False)]
    # (0, 0) -> [((0, 1), True), ((1, 0), False)]
    # True -> can move through, False -> can't move through
    
    adjMatrixAll = dict()
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            
            # get all possible moves from this position
            moves = []
            if i > 0:
                moves.append(((i - 1, j), False if maze[i - 1][j] else True))
            if i < len(maze) - 1:
                moves.append(((i + 1, j), False if maze[i + 1][j] else True))
            if j > 0:
                moves.append(((i, j - 1), False if maze[i][j - 1] else True))
            if j < len(maze[0]) - 1:
                moves.append(((i, j + 1), False if maze[i][j + 1] else True))
            
            adjMatrixAll[(i, j)] = moves
    
    adjMatrixValid = dict()
    adjMatrixInvalid = dict()
    
    for key in adjMatrixAll:
        # print(f'{key} -> {adjMatrixAll[key]}')
        validMoves, invalidMoves = {}, {}

        for move in adjMatrixAll[key]:
            if move[1]:
                validMoves[move[0]] = move[1]
            else:
                invalidMoves[move[0]] = move[1]
        adjMatrixValid[key] = validMoves
        adjMatrixInvalid[key] = invalidMoves
        # print(f'{key} -> {adjMatrixValid[key]}')
    
    return adjMatrixValid, adjMatrixInvalid
    

def visualizeMaze(maze, visited):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in visited:
                print('X', end='')
            else:
                print(maze[i][j], end='')
        print()

tests = [([[0, 0, 0, 0, 0, 0], 
           [1, 0, 1, 1, 1, 0], 
           [0, 0, 0, 0, 0, 0], 
           [0, 1, 1, 1, 1, 1], 
           [0, 1, 1, 1, 1, 1], 
           [0, 0, 0, 0, 0, 0]], 11), 
         
         ([[0, 1, 1, 0], 
           [0, 0, 0, 1], 
           [1, 1, 0, 0], 
           [1, 1, 1, 0]], 7)]

for test in tests:
    start = time()
    for line in test[0]:
        print(line)
        pass
    print(f'solution() = {solution(test[0])} (expected {test[1]}) -- {time() - start} seconds')
