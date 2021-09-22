# Chapter 16 exercise 9
# map the world's fires and show their brightness
# created on 9/22/2021

import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

num_rows = 10_000

# open and read the csv file
filename ='data/global_fires_7_days.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    row_num = 0

    # get dates, latitude, longitude, and brightness of fires
    hover_texts, lats, longs, brights = [], [], [], []

    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        lats.append(float(row[0]))
        longs.append(float(row[1]))
        brights.append(float(row[2]))
        hover_texts.append(f"{date.strftime('%m/%d/%y')} - {brightness}")

        row_num += 1
        if row_num == num_rows:
            break

# Map the data
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [(bright // 20) for bright in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }
}]
my_layout = Layout(title='Global Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')



