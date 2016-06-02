fig = plt.figure(figsize=(10,10))

dirnames = np.array(['dummy','u-ab642','niwa_update_NIWA-UKCA_refC1_2001-2010_zm','niwa_update_NIWA-UKCA_refC1_2001-2010','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010_zm','niwa_update_NIWA-ozone-forcing-from-anqdg-2001-2010'])
fnames = np.array(['ab642'])
titles=['MO ctrl - years 10-20','NIWA ctrol - MO ctrl','UKCA refC1 zm - NIWA ctrl','UKCA refC1 - NIWA ctrl','anqdg zm - NIWA ctrl','anqdg - NIWA ctrl']

varnames = np.array([\
'air_temperature',\
])

for j in range(0,len(varnames)):# loop over different variables

    for i in range(0,len(dirnames)):# loop over different suites

        if i == 0:
            fname = '/hpcf/data/williamsjh/MASS/ab642a.px20011201.pp'
        elif 1 == 1: 
            fname = '/home/williamsjh/cylc-run/'+dirnames[i]+'/share/data/History_Data/'+fnames[0]+'a.px20011201'
        else: 
            fname = '/home/williamsjh/cylc-run/'+dirnames[i]+'/share/data/History_Data/'+fnames[0]+'a.px20011201'

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
            vmin = -1
            vmax = 1

        plt.subplot(3,2,i + 1)

    # 1 - Plot with Iris qplot
        qplt.pcolormesh(plotthis, cmap='RdBu_r', vmin=vmin, vmax=vmax)
        plt.gca().coastlines()

    # 2 - Plot with standard Matplotlib 
    #    plt.pcolormesh(lonplot,latplot,plotthis.data, cmap='RdBu_r', vmin=vmin, vmax=vmax)
    #    plt.axis([0,360,-90,90])
    #    plt.colorbar()

        plt.title(titles[i], size='small')
        plt.suptitle('Years 10 -20 of the simulations, 1991-2001')

iplt.show()

# addtional bits to get at data values only
# coord_names = [coord.name() for coord in cube[0].coords()]
# print coord_names

# coord = cube[0].coord('longitude')
# print coord.points
# print coord.units
# print coord.standard_name

# print coord.points[3]

