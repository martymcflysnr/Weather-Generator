# Weather-Generator

This program simulates fake weather data for locations on Earth. It comes prepared with 2 input files located in the 'reference_data' subdirectory

- Capital cities for 200 countries and their corresponding latitude and longitude (world_capitals_lat_long.csv)
- A map of Earth containing elevation data(elevation_JB.BMP)

The program performs the following:
- The latitude and longitude are read and converted to x/y co-ordinates on the elevation map
- The elevation is read from the map at the x/y co-ordinates
- Random ISO8601 date time is generated
- Random weather data is generated for conditions, temperature, pressure and relative humidity

All the above data is output in a pipe (|) delimited format for 20 random locations selected from the capital city list

# Software requirements are :
Python 3.7
plus additional Python modules:

matplotlib

pandas

# Install using
pip install matplotlib

pip install pandas

# To run the program

1. Extract/copy GenerateWeather.py and the reference_data directory

2. Run 'python GenerateWeather.py'
