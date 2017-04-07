"""
@author: Wenchang Yang (yang.wenchang@uci.edu)
"""

# ######## data paths on the IRI data library.

# surface
pr_cmap = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.CPC/.Merged_Analysis/.monthly/.latest/.ver2/.prcp_est'
cmap = pr_cmap
pr_gpcc = 'http://iridl.ldeo.columbia.edu/SOURCES/.WCRP/.GCOS/.GPCC/.FDP/.version6/.0p5/.prcp/30/div//units/%28mm/day%29def'
gpcc = pr_gpcc
pr_gpcp = 'http://iridl.ldeo.columbia.edu/SOURCES/.NASA/.GPCP/.V2p2/.satellite-gauge/.prcp'
gpcp = pr_gpcp
pr_cru = 'http://iridl.ldeo.columbia.edu/SOURCES/.UEA/.CRU/.TS3p21/.monthly/.pre/30/div'
cru = pr_cru
pr_echam5 = 'http://iridl.ldeo.columbia.edu/SOURCES/.IRI/.FD/.ECHAM5/.T42/.History/.ensemble24/.MONTHLY/.surface/.prec/24/mul/3600/mul'
pr_echam4p5 = 'http://iridl.ldeo.columbia.edu/SOURCES/.IRI/.FD/.ECHAM4p5/.History/.MONTHLY/.surface/.prcp/1000/mul/24/mul/3600/mul'
pr_ncep2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.dg3/.dg3/.pratesfc/24/mul/3600/mul'
pr_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.surface/.prate/24/mul/3600/mul'

# ocean surface
sst_ersst = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.ERSST/.version3b/.sst%5Bzlev%5Daverage'
ersst = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.ERSST/.version3b/.sst[zlev]average'
ersst4 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.ERSST/.version4/.sst[zlev]average'
oisst = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCDC/.OISST/.version2/.AVHRR/.sst%5Bzlev%5Daverage/lon/%28X%29renameGRID/lat/%28Y%29renameGRID/T/%28T%29%28days%20since%201960-01-01%29ordered/7933.5/1/20144.5/NewEvenGRID/replaceGRID'

# atmosphere internal
omega_echam5 = 'http://iridl.ldeo.columbia.edu/SOURCES/.IRI/.FD/.ECHAM5/.T42/.History/.ensemble24/.MONTHLY/.PressureLevel/.omg'
omega_echam4p5 = 'http://iridl.ldeo.columbia.edu/SOURCES/.IRI/.FD/.ECHAM4p5/.History/.MONTHLY/.PressureLevel-SF/.omega'
omega_era40 = 'http://iridl.ldeo.columbia.edu/SOURCES/.ECMWF/.ERA-40/.MONTHLY/.PressureLevel/.wa'
omega_ncep2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.vvelprs'
omega_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel/.vvel'
omega_ncep_daily = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.DAILY/.Intrinsic/.PressureLevel/.vvel'
omega_r2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.vvelprs'
phi_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel/.phi'
phi_r2 = 'http://iridl.ldeo.columbia.eduhttp://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.hgtprs'
phis_ncep2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.hgtsfc'
pr_era40 = 'http://iridl.ldeo.columbia.edu/SOURCES/.ECMWF/.ERA-40/.MONTHLY/.surface/.prc/SOURCES/.ECMWF/.ERA-40/.MONTHLY/.surface/.prl/add/1000/mul/4/mul'
ps_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.surface/.pressure'
ps_r2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.pressfc'
q_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel/.qa'
qs_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.above_ground/.qa%5BZ%5Daverage'
ssta_rsoi = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.EMC/.CMB/.GLOBAL/.Reyn_SmithOIv2/.monthly/.ssta'
ta_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel/.temp'
tas_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.above_ground/.temp%5BZ%5Daverage'
ta_r2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.tmpprs'
trmm_daily = 'http://iridl.ldeo.columbia.edu/SOURCES/.NASA/.GES-DAAC/.TRMM_L3/.TRMM_3B42/.v7/.daily/.precipitation'
trmm = trmm_daily
u_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel/.u'
u_r2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.ugrdprs'
us_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.above_ground/.u%5BZ%5Daverage'
v_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel/.v'
v_r2 = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-DOE/.Reanalysis-2/.Monthly/.pgb/.pgb/.vgrdprs'
vs_ncep = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Diagnostic/.above_ground/.v%5BZ%5Daverage'

# topo and land-sea mask
land_sea_mask = 'http://iridl.ldeo.columbia.edu/SOURCES/.NASA/.ISLSCP/.GDSLAM/.Miscellaneous/.land_sea_mask'
topo = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NGDC/.GLOBE/.topo'
topo_worldbath = 'http://iridl.ldeo.columbia.edu/SOURCES/.WORLDBATH/.bath'
topo_Peltier = 'http://iridl.ldeo.columbia.edu/SOURCES/.PELTIER/.topography/T/0/VALUE%5BT%5Daverage'
