# prepare datasets

from sklearn.cluster import SpectralCoclustering
import numpy as np, pandas as pd

whisky = pd.read_csv("./data/whiskies.csv", index_col=0)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)


# q1
cluster_colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161']
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = dict(zip(regions, cluster_colors))
print(region_colors["Campbelltown"])


# q3
distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i][j] < 0.7:                   # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            group_di = int(whisky[whisky.Distillery == distilleries[i]].Group)
            group_dj = int(whisky[whisky.Distillery == distilleries[j]].Group)
            if group_di == group_dj:   # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]])       # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.

# q6
region_cols = [region_colors[r] for r in whisky.Region]

# q7
classification_cols = [cluster_colors[g] for g in whisky.Group]