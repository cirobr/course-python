import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def connected_components_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)

A1 = np.loadtxt("./data/adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("./data/adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

print(np.shape(G1.nodes())[0] > np.shape(G2.nodes())[0])
print(np.shape(G1.edges())[0] > np.shape(G2.edges())[0])


### connected components
gen = connected_components_subgraphs(G1)
g = gen.__next__()                                   # iterable
print(len(G1), len(G1) == G1.number_of_nodes())
print(len(g))

# largest connected component
G1_LCC = max(nx.connected_components(G1), key=len)
G1_LCC = nx.Graph(G1_LCC)
G2_LCC = max(nx.connected_components(G2), key=len)
print(len(G1_LCC), len(G2_LCC))

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
