# modeling the highs and low in san francisco

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_fran_2018_simple.csv'
with open(filename) as f:
    reader =csv.reader(f)
    header_row = next(reader)

    # uncomment to find the index of the column headers
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get dates and high and low temps from file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = float(row[5])
            low = float(row[6])
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
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# format plot
title = "Daily high and low temperatures - 2018\n San Francisco, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10,130)

plt.show()