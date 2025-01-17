import pylandstats as pls
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap

input_filepath = "src/mlforterraingeneration/Landscape_Metrics/cairgorms_zoomnew.tif"


with rasterio.open(input_filepath) as src:
    raster_array = src.read(1)

# Define the bins for 10 discrete categories based on equal intervals
min_value = raster_array.min()
max_value = raster_array.max()
bins = np.linspace(min_value, max_value, 11) 
classified_array = np.digitize(raster_array, bins, right=False)


classified_array = np.clip(classified_array, 1, 10)

cmapClas = mpl.colors.ListedColormap(["#000000", "#31f6dc", "#5d95ff", "#77da75",  "#E59866", "#2E86C1", "#DFFF00", "#fdffd3", "#e51aca", "#ffd22d"])

# Plot the classified array
plt.imshow(classified_array, cmap=cmapClas)  
plt.colorbar(label='Categories')
plt.title("Classified Map into 10 Discrete Categories")
plt.show()

# Compute patch metrics on the classified map
ls_classified = pls.Landscape(classified_array, res=(100,100))
df = ls_classified.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
min_area_threshold = 100  # Set an appropriate threshold
df_filtered = df[df["area"] >= min_area_threshold]
print(df_filtered)
ls_classified.plot_landscape(legend=True)
plt.show()


# Extract fractal dimensions and core area index
fractal_dimensions = df_filtered['fractal_dimension']
core_area_index = df_filtered['core_area_index']

# Plot histogram of fractal dimensions
plt.figure(figsize=(8, 6))
plt.hist(fractal_dimensions, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Fractal Dimension')
plt.ylabel('Frequency')
plt.title('Histogram of Fractal Dimensions for Each Patch')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot histogram of core area index
plt.figure(figsize=(8, 6))
plt.hist(core_area_index, bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('Core Area Index')
plt.ylabel('Frequency')
plt.title('Histogram of Core Area Index for Each Patch')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()