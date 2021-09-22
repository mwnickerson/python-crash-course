# chapter 16 exercise 8
# map the past 30 days of earthquakes
# date of creation: 9/22/2021

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# open and read the json file
filename = 'data/eq_data_most_recent.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

eq_meta = all_eq_data['metadata']
all_eq_dicts = all_eq_data['features']

# extract magnitude and location of earthquakes
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# map the data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*abs(mag) for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

# format the final file
title = eq_meta['title']
my_layout = Layout(title=f'{title}')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='recent_earthquakes.html')
