# Machine Learning for Terrain Generation and Landscape Metrics

This project was made using [uv](https://docs.astral.sh/uv/) --- you will need to install uv to use this package. To run the code, first clone the repository locally.

## Getting Started

You will need:

- uv, a Python project and package manager built in Rust.

Recommend:
[Ruff formatting linter](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff), [mypy type checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker), [pytest](https://docs.pytest.org/en/stable/) for testing.

Add the following to your settings.json (Press Cmd/Ctrl+Shift+P, type settings, click Preference: Open User Settins (JSON)):

```{json}
"[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.tabSize": 4
    },
```

Mypy type checker extension for VSCode.
I recommend enabling Format on Save in your settings for all file types.

After cloning the repo, run `uv sync` this should install all the dependencies required for the project.

## Generating Landscape Data and Calculating Metrics

This project aims to assess various methods of terrain generation for the use of evaluating landscape metrics. All of the code used to generate terrain/calculate metrics can be found in the src/mlforterraingeneration folder.

To calculate metrics/plot histograms for the categorical map of Cairngorms (found in [cairngorms.tif](.data/raw/cairngorms.tif)), run the [cairngorms_metrics.py](.src/mlforterraingeneration/Landscape_Metrics/cairngorms_metrics.py) file. Note that this code can be easily adapted to calculate metrics for any raster image by changing the input_filepath. Results are saved in [data/processed](.data/processed).

To generate the three examples of NLMs with the midpoint displacement algorithm, run the [NLMpy_metric_examples.py](.src/mlforterraingeneration/Landscape_Metrics/NLMpy_metric_examples.py) file. This also calculates metrics for these landscapes.

The [perlin_generation.py](.src/mlforterraingeneration/Perlin_Noise/perlin_generation.py) file generates a simulated landscape using the Perlin noise algorithm. This also creates a categorical map where the generated terrain is classified into four distinct categories based on the Perlin noise values. Additionally, this code calculates landscape metrics and saves histograms of the patch level metrics to [data/processed](.data/processed).

The [ProGAN_metrics.py](.src/mlforterraingeneration/Machine_Learning/ProGAN_metrics.py) file is a PyTorch implementation of ProGAN which is used to generate synthetic satellite images. The code used was adapted from [PyTorch_ProGAN](https://www.kaggle.com/code/tauilabdelilah/progan-implementation-from-scratch-pytorch) and a full breakdown from the author can be found at [PyTorch_ProGAN_explained](https://blog.paperspace.com/implementation-of-progan-from-scratch/). The dataset used is available at (https://huggingface.co/datasets/HasanBashir/satellite-gan) and some examples of generated images can be found in [ProGAN_saved_examples](.data/processed/ProGAN_saved_examples). 

Finally, to calculate metrics on these generated images, we can run the [ProGAN_metrics.py](.src/mlforterraingeneration/Machine_Learning/ProGAN_metrics.py) file. This code classifies the image into distinct classes by calculating the average value of each channel in the RGB image. To calculate metrics on a different image, change the input_filename.
