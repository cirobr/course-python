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
# Convert birddata.date_time to the `pd.datetime` format.
import datetime
birddata.date_time = [datetime.datetime.strptime(d[:-3], "%Y-%m-%d %H:%M:%S") for d in birddata.date_time]

# Create a new column of day of observation
birddata["date"] = pd.Series([birddata.date_time[i].date() for i in birddata.index], index=birddata.index)

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date")

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates["altitude"].mean()

# q3
# Use `groupby()` to group the data by bird and date.
grouped_birdday = 

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = 