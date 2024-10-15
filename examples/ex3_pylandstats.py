import pylandstats as pls
from nlmpy import nlmpy
import matplotlib.pyplot as plt

nRow = 50  # Number of rows
nCol = 50  # Number of columns

landscape = nlmpy.mpd(nRow, nCol, 0.75)
landscape = nlmpy.classifyArray(landscape, [1, 1, 1, 1])

ls = pls.Landscape(landscape, res=(50, 50))
ls.plot_landscape(legend=True)
plt.show()

# Example metrics
patch_areas = ls.area()
total_patch_area = patch_areas.groupby("class_val").sum()
# Can also be done by class
ls.total_area(class_val=3)

# Edge metrics
ls.total_edge(class_val=1)
