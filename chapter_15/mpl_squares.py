# mpl squares
# chapter 15
# plotting a simple line graph

import matplotlib.pyplot as plt

squares = [1, 2, 4, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()