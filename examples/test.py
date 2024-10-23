import numpy as np
from nlmpy import nlmpy
import matplotlib.pyplot as plt
import pylandstats as pls

nRow = 50  # Number of rows
nCol = 50  # Number of columns

landscape = np.zeros((nRow, nCol))
landscape[0:25, 25:50] = 1
landscape[25:50, 0:25] = 2
landscape[20:30, 20:30] = 3
landscape[0:25, 0:25] = 3

ls = pls.Landscape(landscape, res=(100, 100))
ls.plot_landscape(legend=True)
plt.show()



print(ls.compute_patch_metrics_df(metrics=["perimeter_area_ratio"]))
print(ls.compute_class_metrics_df(metrics=["total_area", "patch_density"]))
