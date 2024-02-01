
from collections import deque

class DirectedGraph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.parent = [-1] * len(graph)
        self.flow = 0
        self.max_flow = 0
        self.s = 0
        self.t = 0
        self.path = []
        self.queue = []
    
    def bfs(self):
        n = len(self.graph)
        self.visited = [False] * n
        self.queue = deque()
        self.queue.append(self.s)
        self.visited[self.s] = True
        
        while self.queue:
            u = self.queue.popleft()
            for v in range(n):
                if not self.visited[v] and self.graph[u][v] > 0:
                    self.queue.append(v)
                    self.visited[v] = True
                    self.parent[v] = u
        return self.visited[self.t]

    def FordFulkerson(self):
        while self.bfs():
            self.path = []
            self.path_flow = float("inf")
            s = self.t
            
            # find the path
            while s != self.s:
                self.path.append(s)
                s = self.parent[s]
            self.path.append(self.s)
            self.path = self.path[::-1]
            
            # find the flow
            for i in range(1, len(self.path)):
                u = self.path[i-1]
                v = self.path[i]
                self.path_flow = min(self.path_flow, self.graph[u][v])
            self.max_flow += self.path_flow
            
            # update the residual graph
            v = self.t
            while v != self.s:
                u = self.parent[v]
                self.graph[u][v] -= self.path_flow
                self.graph[v][u] += self.path_flow
                v = u
                
        return self.max_flow
    
    def print_graph(self):
        for i in range(len(self.graph)):
            print(self.graph[i])

    def addSuperSourceSink(self, sources, sinks):
        # extend the graph
        for i in range(len(self.graph)):
            self.graph[i].extend([0, 0])
        
        # add super source 
        self.s = len(self.graph)
        self.graph.append([0] * (len(self.graph) + 2))
        for source in sources:
            self.graph[self.s][source] = float("inf")
        
        # add super sink
        self.t = len(self.graph)
        self.graph.append([0] * (len(self.graph) + 1))
        for sink in sinks:
            self.graph[sink][self.t] = float("inf")
            
        # update the parent and visited arrays
        self.parent.extend([-1, -1])
        self.visited.extend([False, False])
        
        
        # update super source to point to the sources
        for source in sources:
            self.graph[self.s][source] = float("inf")
        
        # update sinks to point to super sink
        for sink in sinks:
            self.graph[sink][self.t] = float("inf")
            
        # self.print_graph()

def solution(srcs, sinks, path):
    # initialize graph
    graph = DirectedGraph(path)
    
    # # create super source and sink
    graph.addSuperSourceSink(srcs, sinks)
    
    # return max flow
    return graph.FordFulkerson()

tests = [
    {
        "input": ([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]),
        "output": 6
    },
    {
        "input": ([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
        "output": 16
    }
]

for test in tests:
    input = test["input"]
    output = test["output"]
    
    assert solution(*input) == output