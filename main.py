import function
import trajectory
import grafic
from matplotlib import pyplot as plt


x, y = trajectory.get_trajectory(-2, 0, 100000, 0)

grafic.show_grafic_autonomous_system(x, y)
