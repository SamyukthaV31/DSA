from collections import defaultdict 
import networkx as nx
import matplotlib.pyplot as plt

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    def BFS(self, start): 
        if start not in self.graph:
            print("Vertex not found ")
            return

        queue = [] 
        visited = set()

        queue.append(start) 
        visited.add(start) 

        while queue: 
            current = queue.pop(0) 
            print(current, end=" ") 

            for neighbor in self.graph[current]: 
                if neighbor not in visited: 
                    queue.append(neighbor) 
                    visited.add(neighbor)  

def create_graph():
    g = Graph()
    edges = [
        (0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)
    ]
    for u, v in edges:
        g.addEdge(u, v)
    return g

def display_graph(graph):
    G = nx.DiGraph()
    for u, neighbors in graph.graph.items():
        for v in neighbors:
            G.add_edge(u, v)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold')
    plt.show()

g = create_graph()

display_graph(g)

start_vertex = 1
print("BFS (starting from vertex", start_vertex, "):")
g.BFS(start_vertex)
