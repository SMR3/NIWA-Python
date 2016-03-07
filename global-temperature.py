import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import iris
import iris.plot as iplt
import iris.quickplot as qplt

fname = '/home/williamsjh/cylc-run/niwa_update/share/data/History_Data/niwa_a.pd1981sep'

cube_all = iris.load(fname, 'air_temperature')

cube=cube_all[0]
print(cube)
print('All times :\n') 
print(cube.coord('time'))

day_1 = iris.Constraint(time=lambda cell: cell.point.day == 1)

with iris.FUTURE.context(cell_datetime_objects=True):
    cube_1 = cube.extract(day_1)

print(cube_1)





fig = plt.figure()
qplt.contour(cube_1)
plt.gca().coastlines()
iplt.show()

