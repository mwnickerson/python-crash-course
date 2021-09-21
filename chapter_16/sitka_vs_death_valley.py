# sitka vs death valley comparison
# plotted on the same graph

import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows,
                     date_index, high_index, low_index):
    """get the highs and lows from the data file"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # get dates and high and low from this file
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# get weather data for sitka
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2,
                 high_index=5, low_index=6)

# plot sitka weather data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='blue', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.25)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# add weather data for death valley
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=4, low_index=5)

# add death valley data
ax.plot(dates, highs, c='red', alpha=0.9)
ax.plot(dates, lows, c='red', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.25)

# format plot
title = "Daily high and low temperatures - 2018\nDeath Valley vs Sitka"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10,130)

plt.show()
