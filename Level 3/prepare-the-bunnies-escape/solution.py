from time import time, sleep
from collections import deque
# for live visualization
from tkinter import Tk, Canvas, Frame, BOTH
from math import sqrt

def getShortestPath(maze, adjMatrixValid, start, end, root, canvas):
    # Queue for A* search
    queue = [(0, start)]
    # Track visited nodes
    visited = set()
    visited.add(start)
    # Track the previous node for each visited node
    prev = {start: None}
    # Track the cost to reach each node
    cost = {start: 0}

    # A* search
    while queue:
        _, node = min(queue)
        queue.remove((_, node))
        # Stop if the end node is reached
        if node == end:
            break
        # Add unvisited neighbors to the queue
        for neighbor in adjMatrixValid[node]:
            new_cost = cost[node] + 1
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + straight_line_distance(neighbor, end)
                queue.append((priority, neighbor))
                visited.add(neighbor)
                drawMaze(maze, visited, root, canvas)
                prev[neighbor] = node

    # Reconstruct the shortest path
    path = []
    at = end
    while at is not None:
        path.append(at)
        if at not in prev:
            break
        at = prev[at]
    path.reverse()

    return path if path[0] == start else []

def straight_line_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solution(maze, root, canvas):
    adjMatrixPath, adjMatrixWall, allWalls = generateAdjacencyMatrix(maze)
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    # print(f'adjMatrixValid = {adjMatrixValid[(0, 0)]}')
    
    shortest = float('inf')
    shortestSoln = []
    
    # get path to end
    visited = getShortestPath(maze, adjMatrixPath, start, end, root, canvas)
    
    # check if end is reachable
    if start in visited and end in visited:
        shortest = len(visited)
        shortestSoln = visited
    #     print(f"Inital solution - {shortest} steps")
    #     visualizeMaze(maze, shortestSoln)
    # else:
    #     print("No naive solution")
        
    # if able to break 1 wall, check all possible walls
    for node in allWalls:
        maze[node[0]][node[1]] = 0
        adjMatrixPath, _, _ = generateAdjacencyMatrix(maze)
        
        # get path to end
        visited = getShortestPath(maze, adjMatrixPath, start, end, root, canvas)
        
        # check if end is reachable and if it's the shortest path
        curlen = len(visited)
        if start in visited and end in visited and curlen < shortest:
            shortest = curlen
            shortestSoln = visited
            # print(f"1 Wall broken solution - {shortest} steps")
            # visualizeMaze(maze, shortestSoln)

        maze[node[0]][node[1]] = 1
    
    drawMaze(maze, shortestSoln, root, canvas)
    return shortest

def generateAdjacencyMatrix(maze):
    # maze[0][0] -> [(maze[0][1], True), (maze[1][0], False)]
    # (0, 0) -> [((0, 1), True), ((1, 0), False)]
    # True -> can move through, False -> can't move through
    
    adjMatrixAll = dict()
    allInvalids = []
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
            
            # get all nodes with walls
            if maze[i][j] == 1:
                allInvalids.append((i, j))
    
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
        # print(f'{key} -> {adjMatrixInvalid[key]}')
    
    return adjMatrixValid, adjMatrixInvalid, allInvalids
    

def visualizeMaze(maze, visited):
    print('+' + '-' * len(maze[0]) + '+')
    for i in range(len(maze)):
        print('|', end='')
        for j in range(len(maze[0])):
            if (i, j) in visited:
                print('X', end='')
            else:
                if maze[i][j] == 0:
                    print(' ', end='')
                else:
                    print('█', end='')
        print('|')
    print('+' + '-' * len(maze[0]) + '+')

def drawMaze(maze, visited, root, canvas, delay=0.00):
    # make delay inversely proportional to maze size
    mazeSize = len(maze) * len(maze[0])
    # delay = delay = 0.1 * (mazeSize ** -0.5)
    blockSize = 50
    canvas.delete("all")  # Clear the canvas
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            color = 'red' if (i, j) in visited else 'white' if maze[i][j] == 0 else 'black'
            canvas.create_rectangle(j * blockSize, i * blockSize, j * blockSize + blockSize, i * blockSize + blockSize, fill=color)
    root.update()  # Update the window
    sleep(delay)

maze1 = [
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]
maze2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
maze3 = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
maze4 = [
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]


tests = [([[0, 0, 0, 0, 0, 0], 
           [1, 0, 1, 1, 1, 0], 
           [0, 0, 0, 0, 0, 0], 
           [0, 1, 1, 1, 1, 1], 
           [0, 1, 1, 1, 1, 1], 
           [0, 0, 0, 0, 0, 0]], 11), 
         
         ([[0, 1, 1, 0], 
           [0, 0, 0, 1], 
           [1, 1, 0, 0], 
           [1, 1, 1, 0]], 7),
         
         (maze1, -1),
         (maze2, -1),
         (maze3, -1),
         (maze4, -1)         
        ]

for test in tests:
    maze = test[0]
    start = time()
    root = Tk()
    root.title("Maze")
    root.geometry(f"{len(maze[0]) * 50}x{len(maze) * 50}")
    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=1)
    # visualizeMaze(maze, [])
    print(f'solution() = {solution(maze, root, canvas)} (expected {test[1]}) -- {time() - start} seconds')

# to keep the windows open
input()
