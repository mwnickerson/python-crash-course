# rolling the dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create two d6
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list
results = [(die_1.roll() + die_2.roll()) for roll_num in range(1000)]

# analyze the results
max_result = die_1.roll() + die_2.roll()
frequencies = [results.count(value) for value in range(2, max_result+1)]
# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two d6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')


