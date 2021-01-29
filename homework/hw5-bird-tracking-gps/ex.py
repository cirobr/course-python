import pandas as pd
birddata = pd.read_csv("./data/bird_tracking.csv")
birddata.info()
print(birddata.head())

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,7))
bird_names = pd.unique(birddata.bird_name)
for bird_name in bird_names:
    ix = (birddata.bird_name == bird_name)
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()

ix = (birddata.bird_name == "Eric")
speed = birddata.speed_2d[ix]
#ind = np.isnan(speed)
#ind1 = ~ind
plt.hist(speed, bins=np.linspace(0, 30, 20))
