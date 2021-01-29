import pandas as pd
birddata = pd.read_csv("./data/bird_tracking.csv")
birddata.info()
print(birddata.head())

import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(7,7))
plt.plot(x,y)
