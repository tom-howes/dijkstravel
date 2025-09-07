from flights import Flights
from airport import Airport
import heapq
airports = {"New York": ["JFK", "EWR", "LGA", "SWF", "BUF", "ALB", "SYR"],
                "Chicago": ["ORD", "MDW", "RFD", "DPA"],
                "Boston": ["BOS"],
                "Los Angeles": ["LAX", "VNY"],
                "Philadelphia": ["PHL", "TTN"],
                "San Antonio": ["SAT"],
                "Seattle": ["SEA", "LKE","BFI", "PAE"]}
class Vertices:

    def __init__(self, all_airports: dict, origin: str):
        self.vertices = []
        for city in all_airports.keys():
            if origin in all_airports[city]:
                self.vertices.append(origin)
                continue
            for airport in all_airports[city]:
                self.vertices.append(airport)
    
    def print_vertices(self):
        for vertex in self.vertices:
            print(vertex)

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {v: [] for v in vertices}
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, start, end):
        distances = {v: float('infinity') for v in self.vertices}
        prev = {v: None for v in self.vertices}
        distances[start] = 0

        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)

            if u in visited:
                continue
            visited.add(u)

            if u == end:
                break

            for v, weight in self.graph[u]:
                if v not in visited:
                    new_dist = current_distance + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    prev[v] = u
                    heapq.heappush(priority_queue, (new_dist, v))

            path = []
            current = end

            while current is not None:
                path.append(current)
                current = prev[current]
            path.reverse()

            return distances[end], path


if __name__== "__main__":
    vertices = Vertices(airports, "SEA")
    vertices.print_vertices()