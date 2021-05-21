#Set datasource
county_fn=r'C:\Users\dmuth\Downloads\Python Exam\QGIS\Shp\county.shp'

#Gets current or active selected layer
county_lyr=QgsVectorLayer(county_fn,'County','ogr')
#Checks if is polygon

#Extract centroid for each polygon
features= county_lyr.getFeatures()
for feature in features:
    geom= str(feature.geometry().centroid().asPoint())
    #get coordinates
    str1=geom[19:]
    coordinates=str1[:-2]
    #split at space
    cordArra=coordinates.split()
    #get x, and get Y
    x=cordArra[0]
    y=cordArra[1]
    print(x,y)
    #print(cordArra)
#Create a new point layer

#Set symbology for the point layer

#save the layer

