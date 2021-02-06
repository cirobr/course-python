import networkx as nx

G = nx.Graph()
G = nx.erdos_renyi_graph(10,0)
nx.draw(G)
