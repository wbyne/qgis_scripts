# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# fTools
# Copyright (C) 2008-2011  Carson Farmer
# EMAIL: carson.farmer (at) gmail.com
# WEB  : http://www.ftools.ca/fTools.html
#
# A collection of data management and analysis tools for vector data
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ftools_utils
from qgis.core import *

uri = QgsDataSourceURI()
uri.setDatabase('c:/mnt/gis/water_resources/storm/storm_sqlite/aed_storm.sqlite')
schema = ''
table = 'swstructure'
geom_column = 'geometry'
uri.setDataSource(schema, table, geom_column)

display_name = 'swstructure_base'
selectLayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
QgsMapLayerRegistry.instance().addMapLayer(selectLayer)

uri = QgsDataSourceURI()
uri.setDatabase('c:/mnt/gis/water_resources/storm/storm_sqlite/Ryan/aed_storm_rr_8sept14_1120.sqlite')
schema = ''
table = 'swstructure'
geom_column = 'geometry'
uri.setDataSource(schema, table, geom_column)

display_name = 'swstructure_RR'
inputLayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
QgsMapLayerRegistry.instance().addMapLayer(inputLayer)

#def compute(self, inPoly, inPts, modify, selection):
##inputLayer = ftools_utils.getVectorLayerByName(inPoly)
##selectLayer = ftools_utils.getVectorLayerByName(inPts)
inputProvider = inputLayer.dataProvider()
selectProvider = selectLayer.dataProvider()
feat = QgsFeature()
infeat = QgsFeature()
geom = QgsGeometry()
selectedSet = []
index = ftools_utils.createIndex(inputProvider)
#dedented this whole region
###if selection:
###    features = selectLayer.selectedFeatures()
###   self.progressBar.setMaximum(len(features))
###for feat in features:
###    geom = QgsGeometry(feat.geometry())
###intersects = index.intersects(geom.boundingBox())
###    for id in intersects:
###        inputProvider.getFeatures( QgsFeatureRequest().setFilterFid( int(id) ) ).nextFeature( infeat )
###        tmpGeom = QgsGeometry(infeat.geometry())
###        if geom.intersects(tmpGeom):
###            selectedSet.append(infeat.id())
###    self.progressBar.setValue(self.progressBar.value()+1)
###else:
#self.progressBar.setMaximum(selectProvider.featureCount())
selectFit = selectProvider.getFeatures()
while selectFit.nextFeature(feat):
    geom = QgsGeometry(feat.geometry())
    intersects = index.intersects(geom.boundingBox())
    for id in intersects:
        inputProvider.getFeatures( QgsFeatureRequest().setFilterFid( int(id) ) ).nextFeature( infeat )
        tmpGeom = QgsGeometry( infeat.geometry() )
        if geom.intersects(tmpGeom):
            selectedSet.append(infeat.id())
 #       self.progressBar.setValue(self.progressBar.value()+1)
###if modify == self.tr("adding to current selection"):
###    selectedSet = list(set(inputLayer.selectedFeaturesIds()).union(selectedSet))
###elif modify == self.tr("removing from current selection"):
###    selectedSet = list(set(inputLayer.selectedFeaturesIds()).difference(selectedSet))
inputLayer.setSelectedFeatures(selectedSet)
####inputLayer.invertSelection()
