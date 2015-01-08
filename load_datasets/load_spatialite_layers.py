layernames = ["swstructure","swgravitymain","swopendrain"]
for i in layernames:
    uri = QgsDataSourceURI()
    uri.setDatabase('C:/mnt/gis/water_resources/storm/storm_sqlite/aed_storm.sqlite')
    schema = ''
    table = i
    geom_column = 'geometry'
    uri.setDataSource(schema, table, geom_column)
    display_name = i+"_base"
    vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
    QgsMapLayerRegistry.instance().addMapLayer(vlayer)

layernames = ["swstructure","swgravitymain","swopendrain"]
for i in layernames:
    uri = QgsDataSourceURI()
    uri.setDatabase('C:/mnt/gis/water_resources/storm/storm_sqlite/Ryan/aed_storm_rr_26aug14_0341.sqlite')
    schema = ''
    table = i
    geom_column = 'geometry'
    uri.setDataSource(schema, table, geom_column)
    display_name = i+"_RR"
    vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
    QgsMapLayerRegistry.instance().addMapLayer(vlayer)

