
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import scipy as sp
import numpy as np
import glob
import pandas
import seawater as sw
import matplotlib.colors as mcolors
from netCDF4 import Dataset
import cmocean


plt.close('all')

#
# settings
#

## mapping
lonplot = (155,175)
latplot = (25, 40)
#
# Dataset: Argo climatology
#
argopath='RG_ArgoClim_p5xp5_099_2015_annual.nc'


argo = Dataset(argopath)

lona = np.array(argo.variables['LONGITUDE'][:])
lata = np.array(argo.variables['LATITUDE'][:])

lat = lata[(lata > latplot[0]) & (lata < latplot[1])]
lon = lona[(lona > lonplot[0]) & (lona < lonplot[1])]

flat = (lata > latplot[0]) & (lata < latplot[1])
flon = (lona > lonplot[0]) & (lona < lonplot[1])


Tm =  np.array(argo.variables['ARGO_TEMPERATURE_MEAN'][:,flat,flon])
Sm =  np.array(argo.variables['ARGO_SALINITY_MEAN'][:,flat,flon])
Pm =  np.array(argo.variables['PRESSURE'][:])

Ta =  np.array(argo.variables['ARGO_TEMPERATURE_ANNUAL_ANOMALY'][:,:,flat,flon])
Sa =  np.array(argo.variables['ARGO_SALINITY_ANNUAL_ANOMALY'][:,:,flat,flon])

lona = lona[(lona > lonplot[0]) & (lona < lonplot[1]+7)]
lata = lata[(lata > latplot[0]) & (lata < latplot[1])]

T = Tm[np.newaxis,...]+Ta
S = Sm[np.newaxis,...]+Sa


# A transect at 165
ilon = 19

lon = lon[ilon]

T = T[...,ilon]
S = S[...,ilon]


D = np.empty_like(S)

for i in range(12):
    D[i] = sw.pden(S[i],T[i],Pm[...,np.newaxis],pr=0)-1000



cs = np.array([22.,22.5,23.,23.5,24.,24.5,25.,25.5,26.,26.5])


def plot_dens(month=0):
    plt.contourf(lat,Pm,D[month],cs,vmin=22.,vmax=26.5,cmap=cmocean.cm.dense,extend='both')
    plt.contour(lat,Pm,D[month],cs,colors='k')
    plt.ylim(450,0)


# plotting
yticks = [0, 100, 200, 300, 400]

fig = plt.figure(figsize=(18,10))


plt.subplot(431)
plot_dens(month=0)
plt.ylabel('Depth [m]')
plt.title('January')
plt.xticks([])
plt.yticks(yticks)

plt.subplot(432)
plt.ylim(450,0)
plot_dens(month=1)
plt.title('February')
plt.yticks([])
plt.xticks([])

plt.subplot(433)
plt.ylim(450,0)
plot_dens(month=2)
plt.title('March')
plt.yticks([])
plt.xticks([])

plt.subplot(434)
plot_dens(month=3)
plt.ylabel('Depth [m]')
plt.title('April')
plt.xticks([])
plt.yticks(yticks)

plt.subplot(435)
plt.ylim(450,4)
plot_dens(month=1)
plt.title('May')
plt.yticks([])
plt.xticks([])

plt.subplot(436)
plt.ylim(450,5)
plot_dens(month=2)
plt.title('June')
plt.yticks([])
plt.xticks([])

plt.subplot(437)
plot_dens(month=6)
plt.ylabel('Depth [m]')
plt.title('July')
plt.xticks([])
plt.yticks(yticks)

plt.subplot(438)
plt.ylim(450,4)
plot_dens(month=7)
plt.title('August')
plt.yticks([])
plt.xticks([])

plt.subplot(439)
plt.ylim(450,7)
plot_dens(month=8)
plt.title('Setember')
plt.yticks([])
plt.xticks([])

plt.subplot(4,3,10)
plot_dens(month=9)
plt.ylabel('Depth [m]')
plt.title('October')
plt.xlabel('Latitude')
plt.yticks(yticks)

plt.subplot(4,3,11)
plt.ylim(450,4)
plot_dens(month=10)
plt.title('November')
plt.yticks([])
plt.xlabel('Latitude')

plt.subplot(4,3,12)
plt.ylim(450,7)
month=11
cps = plt.contourf(lat,Pm,D[month],cs,vmin=22.,vmax=26.5,cmap=cmocean.cm.dense,extend='both')
plt.contour(lat,Pm,D[month],cs,colors='k')

plt.title('December')
plt.yticks([])
plt.xlabel('Latitude')


fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.825, 0.1, 0.01, 0.8])
fig.colorbar(cps, cax=cbar_ax,label=r'Potential density, $\sigma_0$ [kg m$^{-3}]$')


plt.savefig('Argo_density_climatology.pdf')

#plt.tight_layout()


# now compare argo vs. llc
llc_april = np.load('../outputs/dens_4320_April.npz')
llc_october = np.load('../outputs/dens_4320_October.npz')
llc2160_april = np.load('../outputs/dens_2160_April.npz')
llc2160_october = np.load('../outputs/dens_2160_October.npz')


# calculate MLD
def calculate_mld(dens,depth,pden_diff = 0.03):
    """ calculates MLD based on 0.03 km/m3 difference
        to density at 5 m. """
    diff =  dens - dens[0][np.newaxis,...]
    iz,iy = dens.shape
    mld = []
    for i in range(iy):  
        mld.append(depth[np.abs(diff[4:,i]-pden_diff).argmin()+4])
    
    return np.array(mld)


#depth = -llc2160_april['z'][:]
#mld_2160_april = calculate_mld(llc2160_april['rho'],depth,pden_diff = 0.03)

fig = plt.figure(figsize=(14,8))

plt.subplot(321)
plot_dens(month=3)
plt.ylabel('Depth [m]')
plt.xticks([])
plt.yticks(yticks)
plt.text(32.25,-10,r'Argo Climatology, April',fontsize=14)

plt.text(25.25,-20,'(a)',fontsize=14)

plt.subplot(322)
plot_dens(month=9)
plt.xticks([])
plt.yticks([])
plt.text(31.,-10,r'Argo Climatology, October',fontsize=14)
plt.text(25.25,-20,'(b)',fontsize=14)

plt.subplot(323)
plt.contourf(llc2160_april['lat'],-llc2160_april['z'][:],llc2160_april['rho']-1000,cs,vmin=22.,vmax=26.5,cmap=cmocean.cm.dense,extend='both')
plt.contour(llc2160_april['lat'],-llc2160_april['z'][:],llc2160_april['rho']-1000,cs,colors='k')

plt.ylim(450,0)
plt.xticks([])
plt.yticks(yticks)
plt.ylabel('Depth [m]')
plt.text(32,-10,r'1/24$^\circ$ simulation, April',fontsize=14)
plt.text(25.25,-20,'(c)',fontsize=14)

plt.subplot(324)
plt.contourf(llc2160_october['lat'],-llc2160_october['z'][:],llc2160_october['rho']-1000,cs,vmin=22.,vmax=26.5,cmap=cmocean.cm.dense,extend='both')
plt.contour(llc2160_october['lat'],-llc2160_october['z'][:],llc2160_october['rho']-1000,cs,colors='k')
plt.ylim(450,0)
plt.xticks([])
plt.yticks([])
plt.text(31.,-10,r'1/24$^\circ$ simulation, October',fontsize=14)
plt.text(25.25,-20,'(d)',fontsize=14)

plt.subplot(325)
plt.contourf(llc_april['lat'],-llc_april['z'][:-1],llc_april['rho']-1000,cs,vmin=22.,vmax=26.5,cmap=cmocean.cm.dense,extend='both')
plt.contour(llc_april['lat'],-llc_april['z'][:-1],llc_april['rho']-1000,cs,colors='k')
plt.ylim(450,0)
plt.yticks(yticks)
plt.ylabel('Depth [m]')
plt.text(32,-10,r'1/48$^\circ$ simulation, April',fontsize=14)
plt.text(25.25,-20,'(e)',fontsize=14)
xticks = [25,30,35,40]
xticklabels = [r'25$\!^\circ$N',r'30$\!^\circ$N',r'35$\!^\circ$N',r'40$\!^\circ$N']
plt.xticks(xticks,xticklabels)


plt.subplot(326)
plt.contourf(llc_october['lat'],-llc_october['z'][:-1],llc_october['rho']-1000,cs,vmin=22.,vmax=26.5,cmap=cmocean.cm.dense,extend='both')
plt.contour(llc_october['lat'],-llc_october['z'][:-1],llc_october['rho']-1000,cs,colors='k')
plt.ylim(450,0)
plt.yticks([])
plt.text(31.,-10,r'1/48$^\circ$ simulation, October',fontsize=14)
plt.text(25.25,-20,'(f)',fontsize=14)
xticks = [25,30,35,40]
xticklabels = [r'25$\!^\circ$N',r'30$\!^\circ$N',r'35$\!^\circ$N',r'40$\!^\circ$N']
plt.xticks(xticks,xticklabels)




fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.825, 0.1, 0.02, 0.8])
fig.colorbar(cps, cax=cbar_ax,label=r'Potential density, $\sigma_0$ [kg m$^{-3}]$')


plt.savefig('Argo_LLC_density_climatology.pdf')

