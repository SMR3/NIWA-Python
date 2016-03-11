import os

def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import iris
import iris.plot as iplt
import iris.quickplot as qplt
import numpy as np

fig = plt.figure()

dirnames=np.array(['u-ab642','16x16_niwa_update'])
fnames=np.array(['ab642','16x16'])

varnames=np.array(['surface_downwelling_shortwave_flux_in_air_assuming_clear_sky',\
'surface_net_downward_shortwave_flux',\
'surface_upwelling_shortwave_flux_in_air_assuming_clear_sky'\
])

for i in range(0,3):

    fname = '/home/williamsjh/cylc-run/'+dirnames[0]+'/share/data/History_Data/'+fnames[0]+'a.pd1981sep'

    cube_all = iris.load(fname, varnames[i])
    
    print(cube_all)
    
#    pause()
#    
#    
    cube=cube_all[0]
#    print(cube)
#    print('All times :\n') 
#    print(cube.coord('time'))

    day_1 = iris.Constraint(time=lambda cell: cell.point.day == 1)

    with iris.FUTURE.context(cell_datetime_objects=True):
        cube_1 = cube.extract(day_1)

#    print(cube_1)
    
    print(i+1)

    plt.subplot(1,3,i+1)
    qplt.pcolor(cube_1, cmap='RdBu')
    plt.gca().coastlines()

iplt.show()

