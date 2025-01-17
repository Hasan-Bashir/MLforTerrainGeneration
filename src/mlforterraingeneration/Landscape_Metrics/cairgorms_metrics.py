import pylandstats as pls
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap

input_filepath = "src/mlforterraingeneration/Landscape_Metrics/cairgormsrasternew.tif"


ls = pls.Landscape(input_filepath, res=(100,100))
ls.plot_landscape(legend=True)
plt.show()
df = ls.compute_patch_metrics_df(metrics=["area", "fractal_dimension", "core_area_index"])
min_area_threshold = 100  
df_filtered = df[df["area"] >= min_area_threshold]

print(df)

output_filepath = "patch_metrics.csv"
df.to_csv(output_filepath, index=False)
print(f"DataFrame exported to {output_filepath}")

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