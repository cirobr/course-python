# q1
from collections import Counter
import numpy as np

def marginal_prob(chars):
    cv = Counter(chars.values())
    t = np.sum([v for v in cv.values()])
    
    d = list()
    for i in cv:
        k = cv[i] / t
        #print(i, cv[i], k)
        d.append((i, k))

    d = dict(d)
    return d

def chance_homophily(chars):
    mp = marginal_prob(chars)
    #print(mp)
    chance = np.sum([v ** 2 for v in mp.values()])

    return chance

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)

# q2
import pandas as pd
#df  = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df  = pd.read_csv("./data/asset-v1.csv", low_memory=False, index_col=0)

df_filter = (df.village == 1)
df1 = df[df_filter]
df1 = df1.dropna(axis=1, how="any")

df2 = df[df.village == 2]
df2 = df2.dropna(axis=1, how="any")

dfx = df1.head()
dfx = dfx[dfx.resp_gend == 1]
print(len(dfx))

# q3
sex1      = dict(zip(df1.pid, df1.resp_gend))
caste1    = dict(zip(df1.pid, df1.caste))
religion1 = dict(zip(df1.pid, df1.religion))

sex2      = dict(zip(df2.pid, df2.resp_gend))
caste2    = dict(zip(df2.pid, df2.caste))
religion2 = dict(zip(df2.pid, df2.religion))

print(caste2[202802])

# q4
chance_homophily(sex1)
chances = [("sex1", chance_homophily(sex1)), ("caste1", chance_homophily(caste1)), \
           ("religion1", chance_homophily(religion1)), ("sex2", chance_homophily(sex2)), \
           ("caste2", chance_homophily(caste2)), ("religion2", chance_homophily(religion2))]
chances = dict(chances)
print(chances)
max_key = max(chances, key=chances.get)
print(max_key)

# q5
def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)

# q6
#data_filepath1 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_1.csv"
#data_filepath2 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_2.csv"
data_filepath1 = "./data/key_vilno_1.csv"
data_filepath2 = "./data/key_vilno_2.csv"

pid1 = pd.read_csv(data_filepath1, low_memory=False, index_col=0)
pid2 = pd.read_csv(data_filepath2, low_memory=False, index_col=0)

print(pid1.loc[100,"0"])

# q7
import networkx as nx
#A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
#A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
A1 = np.array(pd.read_csv("./data/adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("./data/adj_allVillageRelationships_vilno2.csv", index_col=0))

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

pid1 = pd.read_csv(data_filepath1, dtype=int)['0'].to_dict()
pid2 = pd.read_csv(data_filepath2, dtype=int)['0'].to_dict()

print("sex1:", homophily(G1, sex1, pid1))
print("caste1:", homophily(G1, caste1, pid1))
print("religion1:", homophily(G1, religion1, pid1))

print("sex2:", homophily(G2, sex2, pid2))
print("caste2:", homophily(G2, caste2, pid2))
print("religion2:", homophily(G2, religion2, pid2))
