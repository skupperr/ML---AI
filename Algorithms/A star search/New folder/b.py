import math
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = dict()
        self.coordinates = dict()

    def addEdge(self, src, dst, cost):
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        
        self.graph[src].append([dst, int(cost)])
    
    def calculateHeuristic(self, start, goal):
        x1, y1 = self.coordinates[start]
        x2, y2 = self.coordinates[goal]
        
        heuristic = math.ceil(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        
        return heuristic
    
    def AStar(self, start, goal):
        heuristic = self.calculateHeuristic(start, goal)

        pq = PriorityQueue()
        f_score = {start: 0 + heuristic}
        pq.put((f_score[start], start))

        g_score = {start: 0}  # track actual cost
        parent = {start: None}  # track parent of each node
        visited = set()  # track visited node
        
        while not pq.empty():
            current_node = pq.get()[1]
            
            if current_node == goal:
                path = self.__getPath(parent, current_node)
                return path, g_score[goal]
            
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbor in self.graph[current_node]:
                neighbor_node, cost = neighbor
                temp_g_score = g_score[current_node] + cost
                if neighbor_node not in g_score or temp_g_score < g_score[neighbor_node]:
                    parent[neighbor_node] = current_node
                    g_score[neighbor_node] = temp_g_score
                    f_score[neighbor_node] = g_score[neighbor_node] + self.calculateHeuristic(neighbor_node, goal)
                    pq.put((f_score[neighbor_node], neighbor_node))
        
        return None, None
    
    def __getPath(self, parent, node):
        path = [node]
        while parent[node] is not None:
            node = parent[node]
            path.append(node)
        return list(reversed(path))




graph = Graph()

with open("a.txt", "r") as file:
    lines = file.readlines()

num_nodes = int(lines[0].strip())

for i in range(1, num_nodes + 1):
    parts = lines[i].strip().split()
    node, x, y = parts[0], int(parts[1]), int(parts[2])
    graph.coordinates[node] = (x, y)

num_edges = int(lines[num_nodes + 1].strip())

for i in range(num_nodes + 2, num_nodes + 2 + num_edges):
    parts = lines[i].strip().split()
    src, dst, cost = parts[0], parts[1], int(parts[2])
    graph.addEdge(src, dst, cost)

path, cost = graph.AStar("S", "G")
print("Shortest Path:", path)
print("Cost:", cost)
