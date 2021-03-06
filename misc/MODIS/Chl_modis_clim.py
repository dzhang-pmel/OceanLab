# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import netCDF4
import matplotlib.patheffects as PathEffects
import matplotlib
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
from glob import glob
import pandas as pd

def split_datetime(time):
    '''
    'time': datetime list
    '''
    year,month,day = [],[],[]
    
    for date in time:
        year.append(date.year)
        month.append(date.month)
        day.append(date.day)
        
    year  = np.array(year)
    month = np.array(month)
    day   = np.array(day)
    
    return year,month,day
    

        
def AVISO_geo_monthly(pathADT,pathUV,yr,mo):

    AVISO = Dataset(pathADT)
    
    time = netCDF4.num2date(AVISO.variables['time'][:],AVISO.julian_day_unit)
    
    yearADT,monthADT,dayADT = split_datetime(time)
    
    ind = np.argwhere((yearADT==yr)&(monthADT==mo)).ravel().tolist()
    
    LON,LAT = np.meshgrid(AVISO.variables['lon'][:],AVISO.variables['lat'][:])
    LON -= 360
    ADT = np.squeeze(AVISO.variables['adt'][ind,:,:])
    
    ADT = np.squeeze(np.nanmean(ADT,axis=0))
    PSI = ADT*9.82*-1
    PSI -= PSI.mean()
    
    #lendo dados da AVISO de U e V Geostrófico
    AVISOuv = Dataset(pathUV)
    
    time = netCDF4.num2date(AVISOuv.variables['time'][:],AVISOuv.julian_day_unit)
    
    yearuv,monthuv,dayuv = split_datetime(time)
    
    ind = np.argwhere((yearuv==yr)&(monthuv==mo)).ravel().tolist()
    
    LONuv,LATuv = np.meshgrid(AVISOuv.variables['lon'][:],AVISOuv.variables['lat'][:])
    LONuv -= 360
    
    U = np.squeeze(AVISOuv.variables['u'][ind,:,:])
    V = np.squeeze(AVISOuv.variables['v'][ind,:,:])
    
    U = np.squeeze(np.nanmean(U,axis=0))
    V = np.squeeze(np.nanmean(V,axis=0))
    
    return LON,LAT,PSI,U,V

def MODIS_nc(path,prop,lnd,lnu,ltd,ltu):
    MODIS = Dataset(path)
    
    lon,lat = MODIS.variables['lon'][:],MODIS.variables['lat'][:]
    
    condlon = (lon>=lnd)&(lon<=lnu)
    condlat = (lat>=ltd)&(lat<=ltu)
    
    LONprop,LATprop = np.meshgrid(lon[condlon],lat[condlat])
    PROP = MODIS.variables[prop][condlat,:][:,condlon]
    return LONprop,LATprop,PROP,MODIS

#Lendo funções
%run /data0/iury_data/Copy/ocean/ADCP/misc.py
%run /data0/iury_data/Copy/ocean/AO/err_corrlen.py
%run /data0/iury_data/Copy/ocean/deprecated/seaplot.py


pathfig = '/data0/iury_data/Copy/Dados/MODIS/'

base = '/data0/iury_data/Copy/Dados/MODIS/CHL/A/'


lnd,lnu = -41,-29
ltd,ltu = -16,-9
yr = 2009
mo = 9
not_already_bat = False
chlmax = 0.1
fsize = (18, 7)

def ext_modis_aviso_data(lnd,lnu,ltd,ltu,
                yr,mo,base):
                
    lista = glob(base+'*%.4i*'%(yr))
    lista.sort()
    
    if yr == 2002:
        path = lista[mo-7]
    else:
        path = lista[mo-1]

    #lendo dados da AVISO
    path1 = '/data0/iury_data/Copy/Dados/AVISO/'
    #allsat
    fname1 = 'dataset-duacs-dt-global-allsat-madt-h_1443100227463.nc'
    
    path2 = '/data0/iury_data/Copy/Dados/AVISO/'
    fname2 = 'dataset-duacs-dt-global-allsat-madt-uv_1443099343920.nc'
        
    #Extracting MODIS data
    LONchl,LATchl,CHL,MODIS = MODIS_nc(path,'chlor_a',lnd,lnu,ltd,ltu)

    LON,LAT,PSI,U,V = AVISO_geo_monthly(path1+fname1,path2+fname2,yr,mo)

    maskchl = CHL.mask
    CHL = CHL.data
    CHL[maskchl] = np.nan
    
    PSI = PSI.data
    U = U.data
    V = V.data
    return LONchl,LATchl,CHL,LON,LAT,PSI,U,V


months = ['Jan','Feb','Mar','Apr',
        'May','Jun','Jul','Ago',
        'Sep','Oct','Nov','Dez']

mo = 2
yini,yfin = 2003,2015
CHLs = []
PSIs = []
Us = []
Vs = []


for yr in np.arange(yini,yfin):
    
    LONchl,LATchl,CHL,LON,LAT,PSI,U,V = ext_modis_aviso_data(lnd,lnu,
                                            ltd,ltu,yr,mo,base)
                
    CHLs.append(CHL)
    PSIs.append(PSI)
    Us.append(U)
    Vs.append(V)

CHLs = np.dstack(CHLs)
PSIs = np.dstack(PSIs)
Us = np.dstack(Us)
Vs = np.dstack(Vs)

CHLs = np.nanmean(CHLs,axis=2)
PSIs = np.nanmean(PSIs,axis=2)
Us = np.nanmean(Us,axis=2)
Vs = np.nanmean(Vs,axis=2)


months = ['Jan','Feb','Mar','Apr',
        'May','Jun','Jul','Ago',
        'Sep','Oct','Nov','Dez']

#PLOTANDO PSI
fig,m = make_map(llcrnrlon=lnd, urcrnrlon=lnu,
        llcrnrlat=ltd, urcrnrlat=ltu, 
        projection='merc', resolution='i', 
        figsize=fsize, inset=True, steplat=1, 
        steplon=2, inloc=2,continentcolor='0.0')


levels = np.arange(0,chlmax+0.01,0.01)
C = m.contourf(LONchl,LATchl,CHLs,levels,vmin=0,vmax=chlmax,latlon=True)

stp = 1
cmap = 'RdBu_r'
vmax = 2
shelfbreak=-100
#vmax = np.int(np.ceil(np.max(np.abs(PSI/10000))*10))/10.
levels = np.arange(-vmax,vmax+.1,.1)


#C = m.contourf(LON,LAT,PSI,levels,cmap=cmap,latlon=True)
m.contour(LON,LAT,PSIs,levels,colors='k',latlon=True,alpha=0.5)


m.quiver(LON[::stp,::stp],LAT[::stp,::stp],
                Us[::stp,::stp],Vs[::stp,::stp],
                latlon=True,scale=3,linewidths=0.9,zorder=4)
cbar = plt.colorbar(C)


C2 = m.contourf(LONchl,LATchl,CHLs,[chlmax,100],
        colors='w',zorder=20,latlon=True)

#stepbat = 1
#m.contourf(bLON[::stepbat,::stepbat],bLAT[::stepbat,::stepbat],
#            topoin[::stepbat,::stepbat],
#            [shelfbreak,10000],colors='0.9',latlon=True,zorder=20)
#Cr = m.contour(bLON[::stepbat,::stepbat],bLAT[::stepbat,::stepbat],
#                topoin[::stepbat,::stepbat],
#                [shelfbreak,10000],
#                colors='k',latlon=True,
#                linewidths=1.5,zorder=20)
#clabels = m.ax.clabel(Cr,fontsize=15,
#fmt='%.i m',inline=True,inline_spacng=-5,
#zorder=30,fontweight='bold')
#for t in clabels:
#    t.set_zorder(30)
#plt.draw()
#plt.setp(clabels, path_effects=[
#        PathEffects.withStroke(linewidth=3, foreground="w")])

date = months[mo-1]+'   %.4i to %.4i'%(yini,yfin-1)
long_name = MODIS.variables['chlor_a'].long_name
unit = MODIS.variables['chlor_a'].units
m.ax.set_title(date+'  '+long_name+'  '+unit)
plt.savefig(pathfig+'%.2i'%(mo)+months[mo-1]+'%.4i_to_%.4i.png'%(yini,yfin-1),
            dpi=200)




