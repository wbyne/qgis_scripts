from qgis.core import *
import qgis.utils
MyName = "[% "Name" %]"
print MyName
#fileName1 = "GARICH008019OrthoSectorTile3%s" % ".tif"
fileName1 = MyName+".tif"

print fileName1
path1 = "Z:/GARICH11-GEO-TILES-4INCH/%s" % fileName1
print path1
rlayer = QgsRasterLayer(path1, fileName1)
if not rlayer.isValid():
	print "Not found anywhere, looks like a Tommy special!::::"

mycrs=QgsCoordinateReferenceSystem(2239) #qgis incorrectly tries to set the crs wrong
rlayer.setCrs(mycrs)
QgsMapLayerRegistry.instance().addMapLayer(rlayer)
