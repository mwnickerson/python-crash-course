# Earthquake Explore Data

import json

# explore the structure of the data
filename = 'data/eq_data_most_recent.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

# create a formatted json that is human readable from the json
# uncomment to create the formatted file
readable_file = 'data/readable_eq_data2.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)