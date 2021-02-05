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
print(mean_altitudes_perday)
print(mean_altitudes_perday[datetime.date(2013, 9, 12)])

# q3
# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday["altitude"].mean()
print(mean_altitudes_perday)
print(mean_altitudes_perday.Eric[datetime.date(2013, 8, 18)])

# q4
import matplotlib.pyplot as plt
eric_daily_speed  = grouped_birdday["speed_2d"].mean().Eric
sanne_daily_speed = grouped_birdday["speed_2d"].mean().Sanne
nico_daily_speed  = grouped_birdday["speed_2d"].mean().Nico

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()

print(nico_daily_speed[datetime.date(2014, 4, 4)])

