import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# scikit learn for linear regression
n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1
np.random.seed(1)
x1 = 10 * ss.uniform.rvs(size=n)
x2 = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x1 + beta_2 * x2 + \
    ss.norm.rvs(loc=0, scale=1, size=n)
X = np.stack([x1, x2], axis=1)


lm = LinearRegression(fit_intercept=True)
lm.fit(X, y)
print(lm.intercept_, lm.coef_[0], lm.coef_[1])


X_0 = np.array([2, 4])
print(lm.predict(X_0.reshape(1, -1)))  # sem o reshape aparece warning
print(lm.score(X, y))


# assessing model accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    train_size=0.5,
                                                    random_state=1)
lm = LinearRegression(fit_intercept=True)
lm.fit(X_train, y_train)
print(lm.score(X_test, y_test))
