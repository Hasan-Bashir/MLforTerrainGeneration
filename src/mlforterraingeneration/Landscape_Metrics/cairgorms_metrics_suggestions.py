# Ruff linter should automatically sort your imports into a standard order
# It will also remove unused imports for tidoer code.
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import pylandstats as pls
import seaborn as sns

# Use the Path object for file paths, which is more readable and avoids differences in
# file separators on mac vs windows.  Also use relative file paths where possible within
# the repo: my file structure will be different from yours.
input_filepath = Path(
    "data",
    "raw",
    "rasterized_cairgorms10x10 copy.tif",
)


ls = pls.Landscape(input_filepath, res=(100, 100))
ls.plot_landscape(legend=True)
plt.show()
# Use meaningful variable names, e.g.
cg_patch_metrics = ls.compute_patch_metrics_df(
    metrics=["area", "fractal_dimension", "core_area_index"],
)
min_area_threshold = 100
df_filtered = cg_patch_metrics[cg_patch_metrics["area"] >= min_area_threshold]
# Alternative way of doing the same. Above is called Boolean indexing/masking,
# below is a Pandas version.
cg_large_patch_metrics = cg_patch_metrics.query("area >= @min_area_threshold")
# Just double checking that the results are the same
assert cg_large_patch_metrics.equals(df_filtered)
# Rather than the `print` statement, we can use the `head` method. This prevents
# us from accidentally a massive dataframe, instead we specify how many rows we want to
# see
cg_large_patch_metrics.head(20)
# Suggest adding a data directory with raw and processed subfolders
output_filepath = Path("data", "processed", "patch_metrics.csv")
cg_large_patch_metrics.to_csv(output_filepath, index=False)
print(f"DataFrame exported to {output_filepath}")

# Extract fractal dimensions and core area index
fractal_dimensions = cg_large_patch_metrics["fractal_dimension"]
core_area_index = cg_large_patch_metrics["core_area_index"]

# Plot histogram of fractal dimensions
plt.figure(figsize=(8, 6))
plt.hist(fractal_dimensions, bins=20, color="skyblue", edgecolor="black")
plt.xlabel("Fractal Dimension")
plt.ylabel("Frequency")
plt.title("Histogram of Fractal Dimensions for Each Patch")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# The seaborn library is a higher-level interface to matplotlib, and
# can give simple good-looking plots with less code. Sometimes it is necessary
# to use matplotlib directly though!
fig = sns.displot(cg_large_patch_metrics, x="fractal_dimension", kind="hist", bins=20)

# I'd add in an automatic save, or write a function with your default layout
#  (e.g. figsize = (8,6)). That way all your plots look the same and neat in the report.
#  I'd also save as svg or pdf for simple plots, for images use png.
# Always save at a higher resolution than you think. SVG plots don't have a resolution
#  and always look sharp -- they can also be edited in vector graphics software like
#  Inkscape. It could also be useful to add a parameter for the file name or a timestamp
#  so you don't overwrite the same file.
# (Timestamp here is a bit unwieldy but just for demo)
plt.savefig(
    Path(
        "data",
        "processed",
        f"fractal_dimensions_dist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.svg",
    ),
)
plt.show()

# Plot histogram of core area index
plt.figure(figsize=(8, 6))
plt.hist(core_area_index, bins=20, color="lightgreen", edgecolor="black")
plt.xlabel("Core Area Index")
plt.ylabel("Frequency")
plt.title("Histogram of Core Area Index for Each Patch")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
