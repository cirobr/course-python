import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# generating regression data
n = 100
beta_0 = 5
beta_1 = 2
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)

plt.figure()
plt.plot(x, y, "o", ms=5)

xx = np.array([0,10])
plt.plot(xx, beta_0 + beta_1 * xx);

# rss residual sum of squares
def compute_rss(y_estimate, y):
    return sum(np.power(y-y_estimate, 2))

def estimate_y(x, b_0, b_1):
    return b_0 + b_1 * x

rss = compute_rss(estimate_y(x, beta_0, beta_1), y) 
print("{:.2f}".format(rss))

# lss least sum of squares in code
rss = []
slopes = np.arange(-10, 15, 0.01)
for slope in slopes:
    rss.append(np.sum((y - (beta_0 + slope * x)) ** 2))

ind_min = np.argmin(rss)
print(ind_min)
print("Estimate for the slope:", "{:.2f}".format(slopes[ind_min]))

plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slopes")
plt.ylabel("RSS");

# simple linear regression code
import statsmodels.api as sm
mod = sm.OLS(y, x)   # modelo de reta apenas com slope, sem intercept (passa por 0,0)
est = mod.fit()
print(est.summary())

X = sm.add_constant(x)   # adicionar intercept ao modelo
mod = sm.OLS(y, X)
est = mod.fit()
print(est.summary())
