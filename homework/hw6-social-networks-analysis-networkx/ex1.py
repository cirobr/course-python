import networkx as nx

G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(3,4)])
print(G.number_of_nodes(), G.number_of_edges())
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
