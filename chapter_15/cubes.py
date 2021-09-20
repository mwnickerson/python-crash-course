# Cubes
# chapter 15: exercise 1
# plotting cubes to a graph

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# set the chatrt titlke and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_ylabel("Cubed Values", fontsize=14)
ax.set_xlabel("Value", fontsize=14)

# set the range for each axis
ax.axis([0, 5000, 0, (5001**3)])

plt.show()
