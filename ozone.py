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

dirnames=np.array(['u-ab642','niwa_update_NIWA-UKCA_refC1_2001-2010_zm'])
fnames=np.array(['ab642'])

varnames=np.array([\
'air_temperature',\
])

for i in range(0,len(dirnames)):

    fname = '/home/williamsjh/cylc-run/'+dirnames[i]+'/share/data/History_Data/'+fnames[0]+'a.ps1981son'

    cube_all = iris.load(fname, varnames[0])
    cube=cube_all[0] 
    
    plt.subplot(1,2,i+1)
    qplt.pcolormesh(cube, cmap='RdBu_r')
    plt.title('' )
    plt.gca().coastlines()

iplt.show()

