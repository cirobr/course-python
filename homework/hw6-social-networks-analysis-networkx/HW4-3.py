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

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

mp = marginal_prob(favorite_colors)
print(mp)
