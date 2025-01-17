import numpy as np
from nlmpy import nlmpy
import matplotlib.pyplot as plt
import pylandstats as pls

nRow = 50  # Number of rows
nCol = 50  # Number of columns

landscape = np.array([0, 1, 2, 3, 4])
landscape = np.tile(landscape, 500)
landscape = landscape.reshape(nRow,nCol)

ls = pls.Landscape(landscape, res=(100, 100))
ls.plot_landscape(legend=True)
plt.show()



print(ls.compute_patch_metrics_df(metrics=["perimeter_area_ratio", "euclidean_nearest_neighbor"]))
print(ls.compute_class_metrics_df(metrics=["total_area", "patch_density"]))
