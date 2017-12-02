import trajectory
from matplotlib import pyplot as plt


i = -6
while i <= 6:
    j = -6
    while j <= 6:
        if ((i == 5) or (i == -5)) and (j == 0):
            i += 0.5
            j += 0.5
        x, y = trajectory.get_trajectory(i, j, 10000, 2)
        plt.plot(x, y)
        j += 0.5
    i += 0.5
plt.show()