# logistic regression
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
#%matplotlib notebook

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# generate data
def gen_data(n, h, sd1, sd2):
    x1 = ss.norm.rvs(loc=-h, scale=sd1, size=n)
    y1 = ss.norm.rvs(loc=0, scale=sd1, size=n)
    
    x2 = ss.norm.rvs(loc=h, scale=sd2, size=n)
    y2 = ss.norm.rvs(loc=0, scale=sd2, size=n)
    
    return(x1, y1, x2, y2)

x1, y1, x2, y2 = gen_data(1000, 1.5, 1, 1.5)

# plot data
def plot_data(x1, y1, x2, y2):
    plt.figure()
    plt.plot(x1, y1, "o", ms=2)
    plt.plot(x2, y2, "o", ms=2)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")
    #plt.plot()
    
# question
x1, y1, x2, y2 = gen_data(1000, 0, 1, 1)
plot_data(x1, y1, x2, y2)
x1, y1, x2, y2 = gen_data(1000, 1, 2, 2.5)
plot_data(x1, y1, x2, y2)
x1, y1, x2, y2 = gen_data(1000, 10, 100, 100)
plot_data(x1, y1, x2, y2)
x1, y1, x2, y2 = gen_data(1000, 20, .5, .5)
plot_data(x1, y1, x2, y2)


### logistic regression
from sklearn.linear_model import LogisticRegression
n = 1000

# generate the data
x1, y1, x2, y2 = gen_data(1000, 1.5, 1, 1.5)

# generate the model's object
clf = LogisticRegression()

# formatar X, y de forma a serem aceitos pelo modelo
X = np.vstack((np.vstack((x1, y1)).T, np.vstack((x2, y2)).T))
y = np.hstack((np.repeat(1,n), np.repeat(2,n)))

# gerar trainset e testset
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    train_size=0.5,
                                                    random_state=1)
# fit the model
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

# probabilidade de um ponto ser classe 1 ou 2
ponto = np.array([-2, 0]).reshape(1, -1)

print(clf.predict_proba(ponto))
print(clf.predict(ponto))

