# mpl squares
# chapter 15
# plotting a simple line graph

import matplotlib.pyplot as plt

squares = [1, 2, 4, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()