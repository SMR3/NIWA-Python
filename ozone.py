fig = plt.figure(figsize=(10,10))

dirnames = np.array(['u-ab642','niwa_update_NIWA-UKCA_refC1_2001-2010_zm','niwa_update_NIWA-UKCA_refC1_2001-2010','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010_zm','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010'])
fnames = np.array(['ab642'])
titles=['control','UKCA refC1 zm - control','UKCA refC1 - control','anqdg zm - control','anqdg - control']

varnames = np.array([\
'air_temperature',\
])

for i in range(0,len(dirnames)):

    fname = '/home/williamsjh/cylc-run/'+dirnames[i]+'/share/data/History_Data/'+fnames[0]+'a.ps1983jja'

    cube_all = iris.load(fname, varnames[0])
    cube=cube_all[0] 
   
    if i == 0:
        cube_control = cube
        plotthis = cube
        vmin = 240
        vmax = 310
        lat=cube.coord('latitude').points
        lon=cube.coord('longitude').points
        lonplot,latplot=np.meshgrid(lon,lat)
    else:
        plotthis = cube - cube_control
        vmin = -5
        vmax = 5

    plt.subplot(3,2,i + 1 + (i > 0))

# 1 - Plot with Iris qplot
    qplt.pcolormesh(plotthis, cmap='RdBu_r', vmin=vmin, vmax=vmax)
    plt.gca().coastlines()

# 2 - Plot with standard Matplotlib 
#    plt.pcolormesh(lonplot,latplot,plotthis.data, cmap='RdBu_r', vmin=vmin, vmax=vmax)
#    plt.axis([0,360,-90,90])
#    plt.colorbar()

    plt.title(titles[i], size='small')

iplt.show()

# addtional bits to get at data values only
coord_names = [coord.name() for coord in cube[0].coords()]
print coord_names

coord = cube[0].coord('longitude')
print coord.points
print coord.units
print coord.standard_name

print coord.points[3]

