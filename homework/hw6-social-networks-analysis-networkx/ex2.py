import networkx as nx

G = nx.Graph()
G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
print(G.degree())
print("\n")
print("No 33", G.degree(33))
print(G.number_of_nodes(), G.number_of_edges())
