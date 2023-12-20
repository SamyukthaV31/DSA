import sys
import networkx as nx
import matplotlib.pyplot as plt

class PrimMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)
        self.plot_graph(parent)

    def plot_graph(self, parent):
        G = nx.Graph()

        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                    G.add_edge(i, j, weight=self.graph[i][j])

        mst_edges = [(parent[i], i) for i in range(1, self.V)]

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=500, node_color='skyblue', edge_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()})

        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2.0)

        plt.title("Graph with Minimum Spanning Tree (MST)")
        plt.show()

graph = PrimMST(5)
graph.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

graph.prim_mst()
