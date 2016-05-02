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

dirnames=np.array(['u-ab642'])
fnames=np.array(['ab642'])

varnames=np.array([\
'air_temperature',\
])

for i in range(0,len(varnames)):

    fname = '/home/williamsjh/cylc-run/'+dirnames[0]+'/share/data/History_Data/'+fnames[0]+'a.ps1981son'

    cube_all = iris.load(fname, varnames[i])
    cube=cube_all(0) 
    print(cube_all)
    
#    pause()
#    
#    
#    cube=cube_all[0]
#    print(cube)
#    print('All times :\n') 
#    print(cube.coord('time'))

#    day_1 = iris.Constraint(time=lambda cell: cell.point.day == 1)

#    with iris.FUTURE.context(cell_datetime_objects=True):
#        cube_1 = cube.extract(day_1)

#    print(cube_1)
    
 #   print(i+1)
#
    #plt.subplot(1,len(varnames),i+1)
   # qplt.pcolor(cube_all, cmap='RdBu')
  #  plt.title('' )
 #   plt.gca().coastlines()

#iplt.show()

