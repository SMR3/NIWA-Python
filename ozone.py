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

dirnames=np.array(['u-ab642','niwa_update_NIWA-UKCA_refC1_2001-2010_zm','niwa_update_NIWA-UKCA_refC1_2001-2010','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010_zm','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010'])
fnames=np.array(['ab642'])

varnames=np.array([\
'air_temperature',\
])

for i in range(0,len(dirnames)):

    fname = '/home/williamsjh/cylc-run/'+dirnames[i]+'/share/data/History_Data/'+fnames[0]+'a.ps1981son'

    cube_all = iris.load(fname, varnames[0])
    cube=cube_all[0] 
   
    if i == 0:
        cube_control = cube
        plotthis = cube
    else:
        plotthis = cube - cube_control
         
    if i > 0:
        plt.subplot(2,2,i)
        qplt.pcolormesh(plotthis, cmap='RdBu_r')
        plt.title(dirnames[i])
        plt.gca().coastlines()

iplt.show()

