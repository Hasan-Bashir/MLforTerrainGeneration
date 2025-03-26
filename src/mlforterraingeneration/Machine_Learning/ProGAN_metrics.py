from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pylandstats as pls
import rasterio
import seaborn as sns

# Define input file
input_filename = "img_65"
input_filepath = f"data/processed/ProGAN_saved_examples/step5/{input_filename}.png"

# Read the raster file using rasterio
with rasterio.open(input_filepath) as src:
    raster_array = src.read().mean(axis=0)  # Compute mean across all bands


# Define the bins for n discrete classes based on equal intervals
number_of_classes = 4
min_value = raster_array.min()
max_value = raster_array.max()
bins = np.linspace(min_value, max_value, number_of_classes + 1)  # n classes = n + 1 bin edges
classified_array = np.digitize(raster_array, bins, right=False)  # Assign values to bins

# Adjust bin edges to create discrete classes (ensure no out-of-bounds errors)
classified_array = np.clip(classified_array, 1, number_of_classes)

# Create output directory
output_dir = Path("data", "processed")
output_dir.mkdir(parents=True, exist_ok=True)

ls_classified = pls.Landscape(classified_array, res=(128,128))

# Save classified landscape plot
classified_plot_path = output_dir / f"ProGAN_{input_filename}_classified.png"
ls_classified.plot_landscape(legend=True)
plt.axis("off")
plt.savefig(classified_plot_path, format="png", bbox_inches="tight")
plt.close()

# Compute and save patch metrics on the classified landscape
patch_metrics = ls_classified.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
min_area_threshold = 12
large_patch_metrics = patch_metrics[patch_metrics["area"] >= min_area_threshold]
patch_metrics_path = output_dir / f"ProGAN_{input_filename}_patchmetrics.csv"
large_patch_metrics.to_csv(patch_metrics_path, index=False)


# Extract fractal dimensions and core area index
fractal_dimensions = large_patch_metrics["fractal_dimension"]
core_area_index = large_patch_metrics["core_area_index"]


# Save histogram of fractal dimensions
fractal_plot_path = output_dir / f"ProGAN_{input_filename}_fractal_dimension_hist.png"
sns.displot(x=fractal_dimensions, kind="hist", bins=20)
plt.xlabel("Fractal Dimension", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig(fractal_plot_path, format="png", bbox_inches="tight")
plt.close()

# Save histogram of core area index
core_area_plot_path = output_dir / f"ProGAN_{input_filename}_core_area_hist.png"
sns.displot(x=core_area_index, kind="hist", bins=20)
plt.xlabel("Core Area Index", fontsize=20)
plt.ylabel("Frequency", fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(0, 100)
plt.savefig(core_area_plot_path, format="png", bbox_inches="tight")
plt.close()

# Print landscape metric values
land_metrics = ls_classified.compute_landscape_metrics_df(metrics=["total_area", "contagion", "shannon_diversity_index"])
print(land_metrics)

# Print class metric values
class_metrics = ls_classified.compute_class_metrics_df(metrics=["total_area", "proportion_of_landscape"])
print(class_metrics)
