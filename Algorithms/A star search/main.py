from collections import defaultdict
import math
import csv
from queue import PriorityQueue

# Import class time from time module
from time import time


COORDINATES_FILE = "Coordinates.csv"
DISTANCE_FILE = "distances.csv"


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
        self.graph[dst].append([src, int(cost)])

    def calculateHeuristic(self, start, goal):
        x1, y1, z1 = self.coordinates[start]
        x2, y2, z2 = self.coordinates[goal]

        heuristic = math.ceil(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2))

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
                if path:
                    return path, g_score[goal]
                else:
                    return None, None
            
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor in self.graph[current_node]:
                if neighbor[0] not in visited:
                    parent[neighbor[0]] = current_node
                    g_score[neighbor[0]] = int(g_score[current_node]) + int(neighbor[1])
                    f_score[neighbor[0]] = g_score[neighbor[0]] + self.calculateHeuristic(neighbor[0], goal)
                    pq.put((f_score[neighbor[0]], neighbor[0]))
                    # print(
                    #     f"Node:{neighbor} parent:{parent[neighbor[0]]} f:{f_score[neighbor[0]]}"
                    # )
        return None, None


    def Dijkstra(self, start, goal):
        pq = PriorityQueue()

        g_score = {node: float("inf") for node in self.graph}
        g_score[start] = 0

        parent = {start: None}
        visited = set()

        pq.put((g_score[start], start))

        while not pq.empty():
            current_node = pq.get()[1]

            if current_node == goal:
                path = self.__getPath(parent, current_node)
                if path:
                    return path, g_score[goal]
                else:
                    return None, None

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor in self.graph[current_node]:
                if neighbor[0] not in visited:
                    
                    new_g_score = int(g_score[current_node]) + int(neighbor[1])
                    if new_g_score < g_score[neighbor[0]]:
                        g_score[neighbor[0]] = new_g_score
                        parent[neighbor[0]] = current_node
                        pq.put((g_score[neighbor[0]], neighbor[0]))
        return None, None


    def __getPath(self, parent, node):
        path = [node]
        current_node = node

        while parent[current_node] is not None:
            current_node = parent[current_node]
            path.append(current_node)

        return list(reversed(path))

    def printGraph(self):
        for source, destination in self.graph.items():
            print(f"{source}-->{destination}")


g = Graph()

with open(COORDINATES_FILE, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for star_name, x, y, z in reader:
        g.coordinates[star_name] = (int(x), int(y), int(z))

with open(DISTANCE_FILE, "r") as file:
    reader = csv.reader(file)
    for source, destination, dist in reader:
        g.addEdge(source, destination, dist)


initialTime = time()
path, cost = g.AStar("Sun", "61 Virginis")
finalTime = time()

print("A*")
print(f"Total time: {finalTime - initialTime}")
print(path)
print(f"Cost: {cost}\n\n\n")


initialTime = time()
path, cost = g.Dijkstra("Sun", "61 Virginis")
finalTime = time()

print("Dijkstra:")
print(f"Total time: {finalTime - initialTime}")
print(path)
print(f"Cost: {cost}")
