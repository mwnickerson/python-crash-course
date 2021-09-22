# chapter 16 exercise 7
# automate the title from the metadata

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# open and read the json file
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
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

# map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
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
offline.plot(fig, filename='global_earthquakes.html')