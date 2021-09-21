# Comparing the temperatures between Death Valley and Sitka Airport
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# read and plot sitka
s_filename = 'data/ sitka_weather_2018_simple.csv'
with open(s_filename) as sf:
    reader =csv.reader(sf)
    header_row = next(reader)

    # get dates and high and low temps from the file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
title = "Comparison of Daily high and low temperatures" \
        "\nDeath Valley v. Sitka - 2018"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)
plt.show(

# read and plot the data for death valley
dv_filename = 'data/death_valley_2018_simple.csv'
with open(dv_filename) as dvf:
    reader = csv.reader(dvf)
    header_row =next(reader)

    # get dates and high and low temps from file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# format plot
title = "Comparison of Daily high and low temperatures" \
        "\nDeath Valley v. Sitka - 2018"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
