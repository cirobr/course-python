import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

def make_prediction_grid(predictors, outcomes, limits, h, k):
    (xmin, xmax, ymin, ymax) = limits
    
    xs = np.arange(xmin, xmax, h)
    ys = np.arange(ymin, ymax, h)
    xx, yy = np.meshgrid(xs, ys)
    
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(predictors, outcomes)
    prediction_grid = knn.predict(np.concatenate(xx, yy))
            
    return (xx, yy, prediction_grid)
    
def plot_prediction_grid (xx, yy, prediction_grid):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))

# ler iris dataset
iris = datasets.load_iris()

# ler todas as 150 observações, mas apenas os dois primeiros predictors
predictors = iris.data[:,0:2]

# ler o outcome (classificação) das 150 observações
# outcomes expressos como fatores.
#significado de cada fator em iris.target_names
outcomes = iris.target

# plotar predictors para a classe "0" 
x = predictors[outcomes==0][:,0]   # primeiro predictor
y = predictors[outcomes==0][:,1]   # segundo predictor
plt.plot(x, y, "ro")

# plotar classes 1 e 2
x = predictors[outcomes==1][:,0]   # primeiro predictor
y = predictors[outcomes==1][:,1]   # segundo predictor
plt.plot(x, y, "go")
x = predictors[outcomes==2][:,0]   # primeiro predictor
y = predictors[outcomes==2][:,1]   # segundo predictor
plt.plot(x, y, "bo")
plt.title("Iris Dataset")
plt.xlabel("Predictor 0 - Setosa")
plt.ylabel("Predictor 1 - Versicolor")

plt.show()
#plt.savefig("iris.pdf")

# predict with KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)
print(np.mean(outcomes == sk_predictions))

res = make_prediction_grid(predictors, outcomes, (0, 5, 0, 5), 0.1, k=5)
plot_prediction_grid()
