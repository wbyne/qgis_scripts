#from http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html

error = QgsVectorFileWriter.writeAsVectorFormat(inputLayer, "c:/mnt/gis/water_resources/storm/storm_sqlite/tmp/RR_diffs_swstructure.shp", \
  "utf-8", None, "ESRI Shapefile", 1) #boolean true is 1

if error == QgsVectorFileWriter.NoError:
  print "success!"

error = QgsVectorFileWriter.writeAsVectorFormat(layer, "my_json.json", \
  "utf-8", None, "GeoJSON")
if error == QgsVectorFileWriter.NoError:
  print "success again!"

#The third parameter specifies output text encoding. Only some drivers need
  #this for correct operation - shapefiles are one of those — however in
  #case you are not using international characters you do not have to care
  #much about the encoding. The fourth parameter that we left as None may
  #specify destination CRS — if a valid instance of QgsCoordinateReferenceSystem
  #is passed, the layer is transformed to that CRS.
#For valid driver names please consult the supported formats by OGR — you
  #should pass the value in `the “Code” column as the driver name. Optionally
  #you can set whether to export only selected features, pass further
  #driver-specific options for creation or tell the writer not to create
  #attributes — look into the documentation for full syntax.

  fields = [QgsField("facilityid", QVariant.String),
	QgsField("installdate", QVariant.String),
	QgsField("name" QVariant.String),
	QgsField("structtype" QVariant.String),
	QgsField("inletdim1" QVariant.float),
	QgsField("inletdim2" double precision),
	QgsField("accessdim1" double precision),
	QgsField("accessdim2" double precision),
	QgsField("accessmat" character varying(20)),
	QgsField("accesstype" character varying(20)),
	QgsField("cvcond" character varying(25)),
	QgsField("cvmatl" character varying(25)),
	QgsField("structshape" character varying(15)),
	QgsField("lined" character varying(3)),
	QgsField("highelev" double precision),
	QgsField("rimelev" double precision),
	QgsField("invertelev" double precision),
	QgsField("invert" double precision),
	QgsField("flowdir" character varying(5)),
	QgsField("enabled" character varying (2)),
	QgsField("activeflag" character varying(2)),
	QgsField("ownedby" smallint),
	QgsField("maintby" smallint),
	QgsField("lastupdate" character varying(8)),
	QgsField("lasteditor" character varying(25)),
	QgsField("gpsdate" character varying(8)),
	QgsField("locdesc" character varying(200)),
	QgsField("rotation" character varying(8)),
	QgsField("comments" character varying(200)),
	QgsField("scansrc" character varying(69)),
	QgsField("ancillaryrole" smallint),
	QgsField("accesscond" character varying(25)),
	QgsField("structmatl" character varying(25)),
	QgsField("structcond" character varying(25)),
	QgsField("facilid_2" character varying(20)),
	QgsField("basin" character varying(25)),
	QgsField("tile_no" character varying(8)]
