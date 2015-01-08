
uri = QgsDataSourceURI()
#uri.setDatabase('c:/mnt/gis/water_resources/storm/storm_sqlite/aed_storm.sqlite')
uri.setDatabase('/mnt/gis/water_resources/storm/storm_sqlite/aed_storm.sqlite')
schema = ''
table = 'swstructure'
geom_column = 'geometry'
uri.setDataSource(schema, table, geom_column)

display_name = 'swstructure_base'
inputLayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
QgsMapLayerRegistry.instance().addMapLayer(inputLayer)

uri = QgsDataSourceURI()
#uri.setDatabase('c:/mnt/gis/water_resources/storm/storm_sqlite/John/aed_storm_john_2014-09-05_4pm.sqlite')
uri.setDatabase('/mnt/gis/water_resources/storm/storm_sqlite/John/aed_storm_john_2014-09-05_4pm.sqlite')
schema = ''
table = 'swstructure'
geom_column = 'geometry'
uri.setDataSource(schema, table, geom_column)

display_name = 'swstructure_JB'
inputLayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
QgsMapLayerRegistry.instance().addMapLayer(inputLayer)


