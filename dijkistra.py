import heapq

class DijkstraGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        predecessors = {vertex: None for vertex in self.graph}

        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)
            if current_distance > distances[u]:
                continue

            for neighbor, weight in self.graph[u]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = u
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()

        if distances[end] == float('infinity'):
            return "No path", []
        return distances[end], path

def menu():
    while True:
        print("\nMain Menu:")
        print("1. Dijkstra's Algorithm")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            g = DijkstraGraph()
            num_edges = int(input("Enter number of edges for Dijkstra's algorithm: "))
            for _ in range(num_edges):
                u, v, w = input("Enter edge (u v w): ").split()
                g.add_edge(u, v, float(w))

            start = input("Enter starting vertex: ")
            end = input("Enter ending vertex: ")
            distance, path = g.dijkstra(start, end)
            if distance == "No path":
                print(f"No path from {start} to {end}")
            else:
                print(f"Shortest path from {start} to {end} is {distance}")
                print("Path:", " -> ".join(path))
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
