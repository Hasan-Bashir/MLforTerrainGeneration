from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pylandstats as pls
import seaborn as sns
from noise import pnoise2

width = 500
height = 500
scale = 100.0
octaves = 8
persistence = 0.6
lacunarity = 2.5

terrain = np.zeros((width, height))

for i in range(width):
    for j in range(height):
        terrain[i][j] = pnoise2(i / scale,
                                j / scale,
                                octaves=octaves,
                                persistence=persistence,
                                lacunarity=lacunarity,
                                repeatx=1024,
                                repeaty=1024,
                                base=42)

terrain = (terrain - np.min(terrain)) / (np.max(terrain) - np.min(terrain))

plt.figure(figsize=(5, 5))
plt.imshow(terrain, cmap="terrain", origin="upper")
plt.axis("off")

output_dir = Path("data", "processed")
output_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename_unclassified = f"perlin_unclassified_{timestamp}.png"
output_path_unclassified = Path(output_dir, filename_unclassified)
plt.savefig(output_path_unclassified, format="png", bbox_inches="tight")
print(f"Unclassified plot saved to {output_path_unclassified}")

# Classify terrain into 4 categories
classified_terrain = np.zeros_like(terrain)
classified_terrain[terrain < 0.25] = 1
classified_terrain[(terrain >= 0.25) & (terrain < 0.5)] = 2
classified_terrain[(terrain >= 0.5) & (terrain < 0.75)] = 3
classified_terrain[terrain >= 0.75] = 4

plt.figure(figsize=(5, 5))
plt.imshow(classified_terrain, cmap="terrain", origin="upper")
plt.axis("off")

ls = pls.Landscape(classified_terrain, res=(100, 100))
ls.plot_landscape(legend=True)
plt.axis("off")

# Compute metrics on classified landscape
min_area_threshold = 12.5
metrics_df = ls.compute_patch_metrics_df(metrics=["core_area_index", "area", "fractal_dimension"])
large_metrics_df = metrics_df.query("area >= @min_area_threshold")
print(large_metrics_df)

# Save classified terrain plot
filename_classified = f"perlin_classified_{timestamp}.png"
output_path_classified = Path(output_dir, filename_classified)
plt.savefig(output_path_classified, format="png", bbox_inches="tight")
print(f"Classified plot saved to {output_path_classified}")

# Plot histogram of core area index using seaborn displot
plot = sns.displot(large_metrics_df, x="core_area_index", kind="hist", bins=20)
plt.xlabel("core_area_index", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.xlim(0, 100)
plot.set_axis_labels("Core Area Index", "Frequency")

filename_histogram_pdf = f"perlin_core_area_index_histogram_{timestamp}.pdf"
output_path_histogram_pdf = Path(output_dir, filename_histogram_pdf)
plot.savefig(output_path_histogram_pdf, format="pdf", bbox_inches="tight")
print(f"Histogram plot saved to {output_path_histogram_pdf}")

plot = sns.displot(large_metrics_df, x="fractal_dimension", kind="hist", bins=20)
plt.xlabel("fractal_dimension", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plot.set_axis_labels("Fractal Dimension", "Frequency")

filename_histogram_pdf = f"perlin_fractal_histogram_{timestamp}.pdf"
output_path_histogram_pdf = Path(output_dir, filename_histogram_pdf)
plot.savefig(output_path_histogram_pdf, format="pdf", bbox_inches="tight")
print(f"Histogram plot saved to {output_path_histogram_pdf}")

landscapemetrics_df = ls.compute_landscape_metrics_df(metrics=["total_area", "contagion", "shannon_diversity_index"])
print(landscapemetrics_df)
