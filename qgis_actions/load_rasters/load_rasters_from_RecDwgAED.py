#**working version
from qgis.core import *
import qgis.utils
fileName1 = """[% "FullPath" %]""" #add quotes otherwise it chokes on the / assignment!  + for concats doesn't seem to work in this console....
print fileName1
tmpFile = fileName1.lstrip('.') #remove the leftmost . to make ./ / in the file pathname
fileName1 = tmpFile
print tmpFile
#fileName = "C:/mnt/project_archives/working/res_com%s" % fileName1 #original line, removed res_com due to change in the directory where i ran the setup script
fileName = "C:/mnt/project_archives/working%s" % fileName1
mylist=[]
mylist = fileName.split ('/')
print fileName
lastitem = len(mylist[:])-1
#print len(mylist[:])
#print len(mylist[:])-1
#print mylist[lastitem]
#print mylist[lastitem+1]
rlayer = QgsRasterLayer(fileName, mylist[lastitem])
if not rlayer.isValid():
	print "Not found in res_com, checking network...."
	fileName = "P:/project_archives/working%s" % fileName1 #changed the order around some 
	rlayer = QgsRasterLayer(fileName, mylist[lastitem])
	if not rlayer.isValid():
		print "I dont know where you found this one..."
QgsMapLayerRegistry.instance().addMapLayer(rlayer)
