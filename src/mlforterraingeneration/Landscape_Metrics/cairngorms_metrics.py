from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import pylandstats as pls
import seaborn as sns


def landscape_input(filepath):
    ls = pls.Landscape(filepath)
    ls.plot_landscape(legend=True)
    plt.show()
    return ls

def compute_patch_metrics(landscape, metrics, output_filepath):
    patch_metrics = landscape.compute_patch_metrics_df(metrics=metrics)
    patch_metrics.to_csv(output_filepath, index=False)
    print(f"DataFrame exported to {output_filepath}")
    return patch_metrics

def plot_histogram(data, column, output_dir, prefix, input_stem, bins=20):
    plot = sns.displot(data, x=column, kind="hist", bins=bins)
    filepath = Path(output_dir, f"{input_stem}_{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.svg")
    plot.savefig(filepath)
    plt.show()
    print(f"{prefix}_plot saved to {filepath}")

def main():
    # Filepaths
    input_filepath = Path("data", "raw", "cairngorms.tif")
    input_stem = input_filepath.stem
    metrics_output_filepath = Path("data", "processed", f"{input_stem}_patch_metrics.csv")
    plot_output_dir = Path("data", "processed")
    plot_output_dir.mkdir(parents=True, exist_ok=True)

    # Input landscape filepath
    landscape = landscape_input(input_filepath)

    # Compute patch metrics
    metrics = ["area", "fractal_dimension", "core_area_index"]
    patch_metrics = compute_patch_metrics(landscape, metrics, metrics_output_filepath)

    # Plot histograms
    plot_histogram(
        patch_metrics,
        "fractal_dimension",
        plot_output_dir,
        "fractal_dimensions_hist",
        input_stem
    )
    plot_histogram(
        patch_metrics,
        "core_area_index",
        plot_output_dir,
        "core_area_index_hist",
        input_stem
    )

if __name__ == "__main__":
    main()
