import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

#df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@movie_data.csv", index_col=0)
df = pd.read_csv("./data/movie_data.csv", index_col=0)

# q1
print(df.head())
print(df.columns)

print(df.head(1)["original_title"])

# q2
df.insert(loc=len(df.columns), column="profitable", value=0)
df.profitable = np.where(df.revenue > df.budget, 1, 0)

regression_target = "revenue"
classification_target = "profitable"

print(np.sum(df.profitable == 1))

# q3
not_wanted = [np.inf, -np.inf]
df = df.replace(not_wanted, np.nan)
df = df.dropna(axis=0, how="any")

print(len(df))

# q4
genres_list = []
for genre in df.genres:
    for g in genre.split(","):
        g2 = g.strip()
        if g2 not in genres_list:
            genres_list.append(g2)

for genre in genres_list:
    df.insert(loc=len(df.columns), column=genre, value=0)
    col = [int(genre in df.genres[i]) for i in df.index]
    df[genre] = col

print(len(genres_list))

# q5
continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
plotting_variables = ['budget', 'popularity', regression_target]

axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, \
       color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))
# show the plot.
plt.show()

# determine the skew.
skew_list = df[outcomes_and_continuous_covariates].skew(axis=0, skipna=True)
print(skew_list)

# q6
right_skew = list(skew_list[skew_list.values > 0].index)
print(right_skew)
df[right_skew] = df[right_skew].apply(lambda x: np.log10(1+x))

print(df[outcomes_and_continuous_covariates].skew(axis=0, skipna=True).runtime)

# q7
df.to_csv("./data/movies_clean.csv", sep=",")
