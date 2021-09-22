# Chapter 16 exercise 9
# map the world's fires and show their brightness
# created on 9/22/2021

import csv

filename ='data/global_fires_7_days.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# get latitude, longitude, and brightness of fire
