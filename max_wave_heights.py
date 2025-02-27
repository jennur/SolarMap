import xarray as xr
import numpy as np
import json

def printMaxHmaxAtLngLat0(filename):
    """Find and print the max hmax value at lngLat (0.000, 0.000)"""
    dataset = xr.open_dataset(filename, engine="netcdf4")

    # Get the DataArray for hmax values
    hmax_array = dataset["hmax"]

    # Get hmax values for all time coords at longitude=0.000 latitude=0.000
    hmax_values_0 = hmax_array.sel(latitude=0.000, longitude=0.000).values

    # Get the max hmax for these coords
    max_hmax_0 = hmax_values_0.max()

    print("Max hmax at (0.000, 0.000):", max_hmax_0)
    dataset.close()


def generateMaxHmaxJSFromNetCDF(filename):
    """Generate maxHmax.js containing JSON data with lngLat coords and corresponding max hmax"""
    dataset = xr.open_dataset(filename, engine="netcdf4")
    hmax_array = dataset["hmax"]
    maxHmax = {}

    for long in hmax_array["longitude"].values:
        for lat in hmax_array["latitude"].values:
            
            # Get hmax values for all time coords at the given lngLat
            hmax_values = hmax_array.sel(longitude=long, latitude=lat).values

            # Replace NaN values with 0
            no_nan_hmax_values = np.nan_to_num(hmax_values)

            # Find the max hmax value
            max_hmax = no_nan_hmax_values.max()

            # Write the coords max value pair to the maxHmax object
            maxHmax[f"({long},{lat})"] = max_hmax

    # Generate JSON data from the object
    json_data = json.dumps(maxHmax, indent=2)

    # Write the content to the maxHmax.js file
    js_code = f"const maxHmax = {json_data};"

    with open("maxHmax.js", "w") as js_file:
        js_file.write(js_code)

    print("maxHmax.js generated successfully")
    dataset.close()