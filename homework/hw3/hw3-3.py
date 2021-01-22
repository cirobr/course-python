import numpy as np, random, scipy.stats as ss

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


# e1
import pandas as pd
folder = "./data/"
file = "wine.csv"
fullname = folder + file
df = pd.read_csv(fullname)

df_temp = df.head(5)
print(np.sum(df_temp.high_quality == 1), "\n")


# e2
numeric_data = df
is_red = []
for c in numeric_data.color:
    if c == "red":
        is_red.append(1)
    elif c == "white":
        is_red.append(0)

numeric_data["is_red"] = is_red
numeric_data = numeric_data.drop(columns=["color", "quality", "high_quality"])

print(np.sum(numeric_data.is_red), "\n")


# e3
from sklearn import preprocessing
scaled_data = preprocessing.scale(numeric_data, axis=0)
numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns)

from sklearn import decomposition
pca = decomposition.PCA(n_components = 2)
principal_components = pca.fit_transform(numeric_data)
print(principal_components.shape, "\n")


# e4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])

x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
            c = df["high_quality"],
            cmap = observation_colormap,
            edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()


# e5
import numpy as np 
np.random.seed(1) # do not change this!

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)

def accuracy(predictions, outcomes):
    acc = np.mean(predictions == outcomes)
    return acc

print(accuracy(x, y) * 100, "\n")


# e6
x = df["high_quality"]
y = np.zeros(x.shape)
print(accuracy(x, y) * 100, "\n")


# e7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, df["high_quality"])

library_predictions = knn.predict(numeric_data)
print(accuracy(x, library_predictions) * 100, "\n")


# e8
