# from http://gis.stackexchange.com/questions/27822/how-to-identify-duplicate-attributes-in-a-field
#Definition of inputs and outputs
# Written by: Gregor Skrt 
#==================================
##[Example scripts]=group
##input=vector
##unique_field=field input
##output=output vector

#Algorithm body
#==================================
from qgis.core import *
from PyQt4.QtCore import *
from processing.core.VectorWriter import VectorWriter

# "input" contains the location of the selected layer.
# We get the actual object, so we can get its bounds
layer = processing.getobject(input)
provider = layer.dataProvider()
fields = provider.fields()
writer = VectorWriter(output, None, fields, provider.geometryType(), layer.crs() )

inFeat = QgsFeature()
outFeat = QgsFeature()
inGeom = QgsGeometry()
nElement = 0
values = {}



value_field_index = layer.fieldNameIndex(unique_field)

feats = processing.getfeatures(layer)
nFeat = len(feats)

for inFeat in feats:
    progress.setPercentage(int((100 * nElement)/nFeat))
    nElement += 1
    inGeom = inFeat.geometry()
    attrs = inFeat.attributes()
    value = attrs[value_field_index]

    if value not in values:
    #to ne vem ce bo drzalo ???
        values[value]=[]
    outFeat.setGeometry(inGeom)
    outFeat.setAttributes(attrs)
    writer.addFeature(outFeat)
del writer