import math
import csv
import heapq
from collections import defaultdict
from queue import PriorityQueue
import time

# Constants for file names
COORDINATES_FILE = "Coordinates.csv"
DISTANCE_FILE = "distances.csv"

# Read coordinates
coordinates = {}
adjacency_list = defaultdict(list)

with open(COORDINATES_FILE, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for star_name, x, y, z in reader:
        coordinates[star_name] = (int(x), int(y), int(z))

# Read distances (adjacency list)
with open(DISTANCE_FILE, "r") as file:
    reader = csv.reader(file)
    for source, destination, dist in reader:
        adjacency_list[source].append((destination, int(dist)))
        adjacency_list[destination].append((source, int(dist)))  # bidirectional edge

# Function to compute Euclidean distance
def euclidean_distance(star1, star2):
    x1, y1, z1 = coordinates[star1]
    x2, y2, z2 = coordinates[star2]
    return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2 + (z2 - z1) ** 2)

# Dijkstra's Algorithm
def dijkstra(start, goal):
    start_time = time.time()
    min_heap = [(0, start)]  # (distance, node)
    distances = {start: 0}
    previous_nodes = {start: None}
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_node == goal:
            break
        for neighbor, weight in adjacency_list[current_node]:
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()
    end_time = time.time()
    return path, distances[goal], (end_time - start_time)

# AStar class with the provided method
class AStar:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def __getPath(self, parent, current_node):
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]
        path.reverse()
        return path

    def AStar(self, start, goal):
        pq = PriorityQueue()
        f_score = {start: 0 + self.heuristic[start]}
        pq.put((f_score[start], start))

        g_score = {start: 0}  # Track actual cost
        parent = {start: None}  # Track parent of each node
        visited = set()  # Track visited nodes

        while not pq.empty():
            current_node = pq.get()[1]

            if current_node == goal:
                return self.__getPath(parent, current_node)

            if current_node in visited:
                continue

            visited.add(current_node)
            for neighbor, weight in self.graph[current_node]:
                if neighbor not in visited:
                    parent[neighbor] = current_node
                    g_score[neighbor] = int(g_score[current_node]) + int(weight)
                    f_score[neighbor] = g_score[neighbor] + self.heuristic.get(neighbor, 0)
                    pq.put((f_score[neighbor], neighbor))
                    #print(f"Node: {neighbor}, Parent: {parent[neighbor]}, f: {f_score[neighbor]}")
        return None  # Return None if no path found

# Build the heuristic (Euclidean distances to the goal)
def build_heuristic(goal, coordinates):
    heuristic = {}
    for star in coordinates:
        heuristic[star] = euclidean_distance(star, goal)
    return heuristic

# Correct way to calculate the a_star_cost
def calculate_a_star_cost(path, adjacency_list):
    cost = 0
    for i in range(len(path) - 1):
        # Find the distance between consecutive nodes
        current_node = path[i]
        next_node = path[i + 1]
        
        # Search for the distance in the adjacency list
        for neighbor, distance in adjacency_list[current_node]:
            if neighbor == next_node:
                cost += distance
                break
    return cost

# Example Usage
start_star = "Sun"
end_star = "61 Virginis"

# Build the heuristic for the goal star
heuristic = build_heuristic(end_star, coordinates)

# Create the AStar object
astar = AStar(adjacency_list, heuristic)

# Run Dijkstra and A* algorithms
dijkstra_path, dijkstra_cost, dijkstra_time = dijkstra(start_star, end_star)
a_star_path = astar.AStar(start_star, end_star)
a_star_cost = calculate_a_star_cost(a_star_path, adjacency_list)

# Output results for both algorithms
print("\nA* Algorithm:")
print(f"Path: {' -> '.join(a_star_path)}")
print(f"Cost: {a_star_cost}")
print(f"Time: {dijkstra_time:.3f} seconds")

print("\nDijkstra Algorithm:")
print(f"Path: {' -> '.join(dijkstra_path)}")
print(f"Cost: {dijkstra_cost}")
print(f"Time: {dijkstra_time:.3f} seconds")