# Highs from the Year 2018 at sitka airport

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/ sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader =csv.reader(f)
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
ax.set_title("Daily High and low temperatures, - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()