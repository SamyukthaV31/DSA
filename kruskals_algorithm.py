import networkx as nx
import matplotlib.pyplot as plt

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def kruskal_mst(self):
        self.graph.sort(key=lambda edge: edge[2]) 
        mst = [] 
        disjoint_set = DisjointSet(self.V)

        for edge in self.graph:
            u, v, weight = edge
            if disjoint_set.find(u) != disjoint_set.find(v):
                mst.append((u, v, weight))
                disjoint_set.union(u, v)

        return mst

    def plot_graph(self):
        G = nx.Graph()
        for edge in self.graph:
            u, v, weight = edge
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        edge_labels = {(u, v): w['weight'] for u, v, w in G.edges(data=True)}

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=500, node_color='skyblue', edge_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph")
        plt.show()

vertices = ['A', 'B', 'C', 'D', 'E']
graph = KruskalMST(vertices)

graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 3)
graph.add_edge('B', 'E', 5)
graph.add_edge('C', 'D', 6)
graph.add_edge('C', 'E', 7)
graph.add_edge('D', 'E', 8)

mst = graph.kruskal_mst()
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : Weight = {edge[2]}")

graph.plot_graph()

