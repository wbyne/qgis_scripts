*******Load_image
#**AUD working version
from qgis.core import *
import qgis.utils
from subprocess import Popen
import os
fileName1 = """[% "GEO_CD" %]/[% "FILENAME" %]""" #add quotes otherwise it chokes on the / assignment!  + for concats doesn't seem to work in this console....
fileName2 = """[% "CD" %]/[% "FILENAME" %]""" #add quotes otherwise it chokes on the / assignment!  + for concats doesn't seem to work in this console....
path1 = "c:/mnt/project_archives/rectified/aud/%s" % fileName1
path2 = "c:/mnt/project_archives/rectified/aud/%s" % fileName2
path3 = "P:/project_archives/rectified/aud/%s" % fileName1
path4 = "P:/project_archives/rectified/aud/%s" % fileName2
if os.path.isfile(path1): 
	fileName = path1
elif os.path.isfile(path2): 
	fileName = path2
elif os.path.isfile(path3): 
	fileName = path3
elif os.path.isfile(path4): 
	fileName = path4
else:
	fileName = "C:/temp/"

mylist=[]
mylist = fileName.split ('/')
print fileName
lastitem = len(mylist[:])-1
rlayer = QgsRasterLayer(fileName, mylist[lastitem])
if not rlayer.isValid():
	print "Not found anywhere, looks like a Tommy special!::::"
	mylist=[]
	mylist = fileName.split ('/')
	print fileName
	lastitem = len(mylist[:])-1
	mylist2 = lastitem.split('_')
	lastitem = len(mylist2[:])-1
	PICK_A_DIR = "audsids_"+mylist2[lastitem]
	print PICK_A_DIR
	fileName1 = """PICK_A_DIR"/[% "FILENAME" %]""" #add quotes otherwise it chokes on the / assignment!  + for concats doesn't seem to work in this console....
	print fileName1
	path1 = "c:/mnt/project_archives/rectified/aud/%s" % fileName1
	path3 = "P:/project_archives/rectified/aud/%s" % fileName1
	if os.path.isfile(path1): 
		fileName = path1
	elif os.path.isfile(path3): 
		fileName = path3
	else:
		fileName = "C:/temp/"


	rlayer = QgsRasterLayer(fileName, mylist[lastitem])
	if not rlayer.isValid():
		print "I dont know where you found this one..."

QgsMapLayerRegistry.instance().addMapLayer(rlayer)


************Load_Paper_Map
#**AUD working version
from subprocess import Popen
import os
from qgis.core import *
import qgis.utils
fileName = "[% "FILENAME" %]"
fileName1 = """[% "CD" %]/[% "FILENAME" %]""" #add quotes otherwise it chokes on the / assignment!  + for concats doesn't seem to work in this console....
print fileName
print fileName1
mylist=[]
mylist = fileName.split ('/')
lastitem = len(mylist[:])-1
fileNameStub = mylist[lastitem].split('.')
fileNameStubpdf = fileNameStub[0]+".pdf"
fileNameStubjpg = fileNameStub[0]+".jpg"
print fileNameStubpdf
print fileNameStubjpg

path1 = "p:\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubpdf
path2 = "p:\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubpdf
path3 = "p:\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubjpg
path4 = "p:\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubjpg

if os.path.isfile(path1): #pdf
	fileName = "p:\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubpdf
elif os.path.isfile(path2):
	fileName = "p:\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubpdf
elif os.path.isfile(path3):
	fileName = "p:\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubjpg
elif os.path.isfile(path4):
	fileName = "p:\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubjpg
else:
	print "Cannot find file"

#fileName = "p:/project_archives/prints/aud/%s" % fileName1

args2 = ("c:\\workspace\\load_rasters\\src\\pythons_little_helper.bat Record " + fileName)

pid2=Popen(args2, shell=False, stdin=None, stdout=None, stderr=None,close_fds=True)

#print fileName
#mylist = fileName.split ('/')
#lastitem = len(mylist[:])-1
#print len(mylist[:])
#print len(mylist[:])-1
#print mylist[lastitem]
#print mylist[lastitem+1]
#rlayer = QgsRasterLayer(fileName, mylist[lastitem])
#if not rlayer.isValid():
#	print "Not found in res_com, checking stormwater...."
#	fileName = "p:/project_archives/working/stormwater%s" % fileName1
#	rlayer = QgsRasterLayer(fileName, mylist[lastitem])
#	if not rlayer.isValid():
#		print "I dont know where you found this one..."
#QgsMapLayerRegistry.instance().addMapLayer(rlayer)


*************Load_Paper_Map_Local
#**AUD working version
from subprocess import Popen
import os
from qgis.core import *
import qgis.utils
fileName = "[% "FILENAME" %]"
fileName1 = """[% "CD" %]/[% "FILENAME" %]""" #add quotes otherwise it chokes on the / assignment!  + for concats doesn't seem to work in this console....
print fileName
print fileName1
mylist=[]
mylist = fileName.split ('/')
lastitem = len(mylist[:])-1
fileNameStub = mylist[lastitem].split('.')
fileNameStubpdf = fileNameStub[0]+".pdf"
fileNameStubjpg = fileNameStub[0]+".jpg"
print fileNameStubpdf
print fileNameStubjpg

path1 = "C:\\mnt\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubpdf
path2 = "C:\\mnt\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubpdf
path3 = "C:\\mnt\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubjpg
path4 = "C:\\mnt\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubjpg

if os.path.isfile(path1): #pdf
	fileName = "C:\\mnt\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubpdf
elif os.path.isfile(path2):
	fileName = "C:\\mnt\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubpdf
elif os.path.isfile(path3):
	fileName = "C:\\mnt\\project_archives\\prints\\aud\\[% "CD" %]\\"+fileNameStubjpg
elif os.path.isfile(path4):
	fileName = "C:\\mnt\\project_archives\\prints\\aud\\[% "GEO_CD" %]\\"+fileNameStubjpg
else:
	print "Cannot find file"

#fileName = "p:/project_archives/prints/aud/%s" % fileName1

args2 = ("c:\\workspace\\load_rasters\\src\\pythons_little_helper.bat Record " + fileName)

pid2=Popen(args2, shell=False, stdin=None, stdout=None, stderr=None,close_fds=True)

#print fileName
#mylist = fileName.split ('/')
#lastitem = len(mylist[:])-1
#print len(mylist[:])
#print len(mylist[:])-1
#print mylist[lastitem]
#print mylist[lastitem+1]
#rlayer = QgsRasterLayer(fileName, mylist[lastitem])
#if not rlayer.isValid():
#	print "Not found in res_com, checking stormwater...."
#	fileName = "p:/project_archives/working/stormwater%s" % fileName1
#	rlayer = QgsRasterLayer(fileName, mylist[lastitem])
#	if not rlayer.isValid():
#		print "I dont know where you found this one..."
#QgsMapLayerRegistry.instance().addMapLayer(rlayer)

