import rasterio

input_filepath = "/Users/hasanbashir/Library/Mobile Documents/com~apple~CloudDocs/Level 5 Project/pylandstats/cairgorms_25.tif"
output_filepath = "/Users/hasanbashir/Library/Mobile Documents/com~apple~CloudDocs/Level 5 Project/pylandstats/cairgorms_25new.tif"

with rasterio.open(input_filepath) as src:
    profile = src.profile
    profile.update(nodata=0)  # Set NoData value

    with rasterio.open(output_filepath, "w", **profile) as dst:
        for i in range(1, src.count + 1):
            dst.write(src.read(i), i)