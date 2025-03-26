import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pylandstats as pls
from matplotlib.colors import ListedColormap
from nlmpy import nlmpy

nRow = 50  # Number of rows
nCol = 50  # Number of columns
np.random.seed(0)
landscape1 = nlmpy.mpd(nRow, nCol, 0.2)
landscape1 = nlmpy.classifyArray(landscape1, [0.3, 1, 1])

landscape2 = nlmpy.mpd(nRow, nCol, 10)
landscape2 = nlmpy.classifyArray(landscape2, [0.1, 0.2, 1])


landscape3 = nlmpy.mpd(nRow, nCol, 1)
landscape3 = nlmpy.classifyArray(landscape3, [1, 1, 1, 1, 1])

cmap = ListedColormap(["yellow", "red", "blue", "purple", "green"])

fig = plt.figure(1)
mpl.rc("axes", linewidth=0.5)

# Plot classified NLMs
qualNLMs = [landscape1, landscape2, landscape3]
labels = ["(a)", "(b)", "(c)"]
subplot = [
    (0, 0),
    (0, 1),
    (0, 2)
]
for n in range(len(qualNLMs)):
    plt.subplot2grid((1, 3), subplot[n], rowspan=2)
    plt.xticks(np.arange(0))
    plt.yticks(np.arange(0))
    plt.imshow(qualNLMs[n], interpolation="none", cmap=cmap)
    plt.title(labels[n], fontsize=8)

# Save the figure as a PDF
plt.savefig("landscape_figure.pdf", format="pdf", bbox_inches="tight")

plt.show()

l1 = pls.Landscape(landscape1, res=(100, 100))
l2 = pls.Landscape(landscape2, res=(100, 100))
l3 = pls.Landscape(landscape3, res=(100, 100))

patchmetrics_a = l1.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
patchmetrics_b = l2.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
patchmetrics_c = l3.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])

# Save patch metrics to CSV files
patchmetrics_a.to_csv("landscape_a_patch_metrics.csv", index=False)
patchmetrics_b.to_csv("landscape_b_patch_metrics.csv", index=False)
patchmetrics_c.to_csv("landscape_c_patch_metrics.csv", index=False)

landmetrics_a = l1.compute_landscape_metrics_df(metrics=["total_area", "contagion", "shannon_diversity_index"])
landmetrics_b = l2.compute_landscape_metrics_df(metrics=["total_area", "contagion", "shannon_diversity_index"])
landmetrics_c = l3.compute_landscape_metrics_df(metrics=["total_area", "contagion", "shannon_diversity_index"])
print(landmetrics_a)
print(landmetrics_b)
print(landmetrics_c)


classmetrics_a = l1.compute_class_metrics_df(metrics=["total_area", "proportion_of_landscape", "number_of_patches"])
print(classmetrics_a)
classmetrics_b = l2.compute_class_metrics_df(metrics=["total_area", "proportion_of_landscape", "number_of_patches"])
print(classmetrics_b)
classmetrics_c = l3.compute_class_metrics_df(metrics=["total_area", "proportion_of_landscape", "number_of_patches"])
print(classmetrics_c)

