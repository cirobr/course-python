import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.erdos_renyi_graph(100, 0.03)
G2 = nx.erdos_renyi_graph(100, 0.30)

degree_sequence1 = [d for n, d in G1.degree()]
plt.hist(degree_sequence1, histtype="step")
plt.show()
plt.close()

degree_sequence2 = [d for n, d in G2.degree()]
plt.hist(degree_sequence2, histtype="step")
plt.show()
plt.close()
