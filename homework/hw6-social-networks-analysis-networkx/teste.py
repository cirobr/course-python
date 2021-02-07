from collections import Counter
import numpy as np

chars = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

c = Counter(chars)
cv = Counter(c.values())
t = np.sum([v for v in cv.values()])

cv
