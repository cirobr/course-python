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
gen1 = (G1.subgraph(c) for c in nx.connected_components(G1))
print(len(G1), len(G1) == G1.number_of_nodes())
gen2 = (G2.subgraph(c) for c in nx.connected_components(G2))

# largest connected component
G1_LCC = max(gen1, key=len)
print(len(G1_LCC))
G2_LCC = max(gen2, key=len)

f, axes = plt.subplots(2,1, figsize=(20, 20))
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20, ax=axes[0])
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20, ax=axes[1])
