import csv

filename ='data/global_fires_7_days.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)
