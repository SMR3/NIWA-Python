import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import iris
import iris.plot as iplt
import iris.quickplot as qplt

fname = '/home/williamsjh/cylc-run/u-ab642/share/data/History_Data/ab642a.pd1981sep'

cube_all = iris.load(fname, 'specific_humidity')

cube=cube_all[0]
print(cube)
print('All times :\n') 
print(cube.coord('time'))

day_1 = iris.Constraint(time=lambda cell: cell.point.day == 1)

with iris.FUTURE.context(cell_datetime_objects=True):
    cube_1 = cube.extract(day_1)

print(cube_1)

fig = plt.figure()
# plt.subplot(121)
qplt.pcolor(cube_1, cmap='RdBu')
plt.gca().coastlines()
# plt.subplot(122)
# qplt.pcolormesh(cube_1)
# plt.gca().coastlines()
iplt.show()

