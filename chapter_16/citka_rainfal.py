# daily precipitation rates in Sitka

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # uncomment to find the index of the column headers
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # get dates and precipitation levels from the file
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcps.append(prcp)

# plot the precipitation levels
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='blue')

# format plot
title = "Daily precipitation amounts - 2018\nSitka Airport"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()