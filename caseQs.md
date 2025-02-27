# Case Qs

1. The highest wave height on 2019-01-01 at coords (0.000, 0.000) was **2.3259899543172153 m**
    - See `printMaxHmaxAtLngLat0()` in `max_wave_heights.py`
2. https://jennur.github.io/SolarMap/
3. If we want to use data from every day since 1950, it means we will have another dimension in the dataset (date). If we assume the dataset otherwise stays the same, with a time array of hourly hmax values, it means we would need to add another iteration – over the date coordinates. 
    
    Procedure:

    1. Predefine an object (`lngLatHmax`) that will hold the lngLat coordinates and the max hmax for the given location.
    2. Iterate over the longitude
    3. Iterate over the latitude
    4. Iterate over the date
    5. Now we can read the hourly hmax values at a given longitude, latitude and date, then extract the max hmax value (`maxHmax`) from this array and store it in the `lngLatHmax` object, `lngLatHmax[f"({long},{lat})"] = maxHmax`. 
    6. Since we want to know the max hmax at a given location since 1950, it means we will need to check on each date iteration if the new `maxHmax` value is greater than the existing `lngLatHmax[f"({long},{lat})"]`. If the new `maxHmax` value is greater than the existing one, we can update the value. 
    
    **Concerns:**
    Iterating through data of 70+ years will be quite time consuming and heavy. In the current given case where the data contained values only from a single day, two for loops were sufficient (+ the `.max()` function [`O(k)`] within the inner for loop), giving `O(m * n * k)` (which is already quite heavy). However with the new dimension (date), another for loop would be needed, and the time complexity would then be `O(m * n * k * p)`. Assuming the dataset will contain all the same coordinates as the current one, we can find the exact number of operations needed to complete this task: 
    
    The length of the current coordinates (`<xarray.DataArray 'hmax' (time: 24, latitude: 261, longitude: 720)>`) and the number of days in 70 years (`days: 365*70 = 25550`) will give a total of `24*261*720*25550 = 115,232,544,000`, i.e. ~115 billion operations. Given the time it takes for my (average+) computer to run the `24*261*720 = 4,510,080` operations, I'd likely need to buy a new one to run the updated script :-)

