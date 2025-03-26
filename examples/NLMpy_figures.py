import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap
from nlmpy import nlmpy

import pylandstats as pls

nRow = 50  # Number of rows
nCol = 50  # Number of columns
np.random.seed(0)
landscape1 = nlmpy.random(nRow, nCol)
landscape1 = nlmpy.classifyArray(landscape1, [1, 1, 1, 1])

landscape2 = nlmpy.mpd(nRow, nCol, 0.9)
landscape2 = nlmpy.classifyArray(landscape2, [1, 1, 1, 1])


landscape3 = nlmpy.randomRectangularCluster(nRow, nCol, 4, 8)
landscape3 = nlmpy.classifyArray(landscape3, [1, 1, 1, 1])

cmapClas = mpl.colors.ListedColormap(["#2E86C1", "#DFFF00", "#E59866", "#008000"])
cmap = ListedColormap(['cyan', 'purple', 'pink', 'yellow'])

fig = plt.figure(1)
mpl.rc("axes", linewidth=0.5)

# Plot classified NLMs
qualNLMs = [landscape1, landscape2, landscape3]
labels = ["(a)", "(b)", "(c)"]
subplot = [
    (0, 0),
    (0, 1),
    (0, 2),
]
for n in range(len(qualNLMs)):
    plt.subplot2grid((1, 3), subplot[n], rowspan=2)
    plt.xticks(np.arange(0))
    plt.yticks(np.arange(0))
    plt.imshow(qualNLMs[n], interpolation="none", cmap=cmapClas)
    plt.title(labels[n], fontsize=8)

# Plot classified legend
plt.subplot2grid((9, 13), (7, 4), colspan=5)
x = np.array([np.array(np.repeat(range(4), 5))])
plt.imshow(x, interpolation="none", aspect=1, cmap=cmapClas)
plt.yticks(np.arange(0))
plt.xticks([2, 7, 12, 17], [0, 1, 2, 3], fontsize=8)
plt.tick_params(direction="out", length=3, width=0.5, top="off")
plt.title("Classed value", fontsize=8)


plt.savefig("nlmpy_example.pdf", format="pdf", dpi=300, bbox_inches="tight")
plt.show()

l1 = pls.Landscape(landscape1, res=(100, 100))
l2 = pls.Landscape(landscape2, res=(100, 100))
l3 = pls.Landscape(landscape3, res=(100, 100))

df = l1.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
dg = l2.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
dh = l3.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
print(df)
print(dg)
print(dh)
print(l1.compute_landscape_metrics_df(metrics=["total_area"]))

plot = sns.displot(dh, x="core_area_index", kind="hist", bins=20)
plot.set_axis_labels("Core Area Index", "Frequency")
plot.figure.suptitle("Histogram of Core Area Index")
plt.show()




