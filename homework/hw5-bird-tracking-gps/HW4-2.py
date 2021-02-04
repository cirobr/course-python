# DO NOT EDIT THIS CODE
import pandas as pd
import numpy as np
birddata = pd.read_csv("./data/bird_tracking.csv")
birddata.info()
print(birddata.head())

# q1
grouped_birds = birddata.groupby("bird_name")
mean_speeds = grouped_birds["speed_2d"].mean()
mean_altitudes = grouped_birds["altitude"].mean()
print(mean_speeds)
print(mean_altitudes)

# q2
import datetime
birddata.date_time = [datetime.datetime.strptime(d[:-3], "%Y-%m-%d %H:%M:%S") \
             for d in birddata.date_time]
#birddata["date"] = pd.Series(timestamps, index=birddata.index)
