#**AUD working version
from qgis.core import *
import qgis.utils
from subprocess import Popen
import os

####################################*********************************#####################
### Be sure to mark the Action as a Python action or you'll waste Friday afternoon.
####################################*********************************#####################
mylist=[]

path1 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath1" %]"
mylist.append(path1)
path2 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath2" %]"
mylist.append(path2)
path3 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath3" %]"
mylist.append(path3)
path4 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath4" %]"
mylist.append(path4)
path5 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath5" %]"
mylist.append(path5)
path6 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath6" %]"
mylist.append(path6)
path7 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath7" %]"
mylist.append(path7)
path8 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath8" %]"
mylist.append(path8)
path9 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath9" %]"
mylist.append(path9)
path10 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath10" %]"
mylist.append(path10)
path11 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath11" %]"
mylist.append(path11)
path12 = "P:\\mnt\\gis\\raster\\assets\\tile[% "image_list.11dec14_1726_IPath12" %]"
mylist.append(path12)

listlen = len(mylist)
for i in range(listlen):
        fauxpath = mylist[i]
        if os.path.isfile(fauxpath): 
            args2 = ("c:\\workspace\\load_rasters\\src\\pythons_little_helper.bat Record " + fauxpath)
            #call Popen with Record as the second argument to invoke the start command native.
            pid2=Popen(args2, shell=False, stdin=None, stdout=None, stderr=None,close_fds=True)
