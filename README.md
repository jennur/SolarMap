# Solar Map

## Technologies used
- MapBox
- HTML
- CSS
- JavaScript
- Python, xarray

## How to generate maxHmax.js
The maxHmax file is generated from the `generateMaxHmaxJSFromNetCDF` function defined in `max_wave_heights.py`. The function is assuming the dataset contains a `hmax` DataArray with dimensions `time`, `longitude` and `latitude`. It will iterate over all the longitude and latitude coordinates and find the max `hmax` value from the time coordinates. `NaN` values are set to `0`. The max `hmax` value is then paired with the given `lngLat` coordinate in the JSON object like the following: 

```JSON
{
    "(-180.0,56.5)": 7.574447445123362,
}
``` 

The reason for generating a js file instead of a JSON file is to simplify the import of the data for this case. 

To generate the file run the following in a python environment:

```python
from max_wave_heights import generateMaxHmaxJSFromNetCDF
generateMaxHmaxJSFromNetCDF("filename.nc")
```

As of now, the function is not handling cases where the dataset differs from what assumed above.

## How markers are added
The markers are added in a click event handler in `index.js`. Since the `lngLat` values from the dataset are iterated by `0.5`, the clicked `lngLat` value is rounded to the nearest half in order to be matched with the closest defined coordinate in the dataset.

## How to run

Simply open the `index.html` file!
