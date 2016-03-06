"""
Quickplot of a 2d cube on a map
===============================

This example demonstrates a contour plot of global air temperature.
The plot title and the labels for the axes are automatically derived from the metadata.

"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import iris
import iris.plot as iplt
import iris.quickplot as qplt


fname = iris.sample_data_path('air_temp.pp')
temperature = iris.load_cube(fname)

# contourf with axes longitude from -180 to 180
fig = plt.figure(figsize=(12, 5))
qplt.contourf(temperature, 15)
plt.gca().coastlines()
iplt.show()

