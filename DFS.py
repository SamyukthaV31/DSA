import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def depth_first_search(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def draw_graph(self):
        G = nx.DiGraph()
        for u in self.graph:
            for v in self.graph[u]:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()

def take_input():
    graph = Graph()
    while True:
        try:
            u, v = map(int, input("Enter edge (u v) (Enter -1 to stop): ").split())
            if u == -1 or v == -1:
                break
            graph.add_edge(u, v)
        except ValueError:
            print("Please enter valid integers.")

    return graph

if __name__ == "__main__":
    print("Enter edges for the graph:")
    user_graph = take_input()

    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print("Depth-First Traversal:")
    user_graph.depth_first_search(start_vertex)

    print("Plotting the graph:")
    user_graph.draw_graph()
