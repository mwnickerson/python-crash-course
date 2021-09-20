# scatter squares
# chapter 15
# plotting and styling individual points with scatter()

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)

# set chart title and label
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
