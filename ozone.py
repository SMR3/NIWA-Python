fig = plt.figure()

dirnames = np.array(['u-ab642','niwa_update_NIWA-UKCA_refC1_2001-2010_zm','niwa_update_NIWA-UKCA_refC1_2001-2010','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010_zm','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010'])
fnames = np.array(['ab642'])

varnames = np.array([\
'air_temperature',\
])

for i in range(0,len(dirnames)):

    fname = '/home/williamsjh/cylc-run/'+dirnames[i]+'/share/data/History_Data/'+fnames[0]+'a.ps1981son'

    cube_all = iris.load(fname, varnames[0])
    cube=cube_all[0] 
   
    if i == 0:
        cube_control = cube
        plotthis = cube
        vmin = 250
        vmax = 310
    else:
        plotthis = cube - cube_control
        vmin = -5
        vmax = 5

    plt.subplot(3,2,i + 1 + (i > 0))
    qplt.contourf(plotthis, 20, cmap='RdBu_r', vmin=vmin, vmax=vmax)
    plt.title(dirnames[i])
    plt.gca().coastlines()
    plt.tight_layout()

iplt.show()

