#Set datasource
county_fn=r'C:\Users\dmuth\Downloads\Python Exam\QGIS\Shp\county.shp'

#Gets current or active selected layer
county_lyr=QgsVectorLayer(county_fn,'County','ogr')
#Checks if is polygon

#Extract centroid for each polygon
features= county_lyr.getFeatures()
pointsList = []
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
    # Create point feature
    point_feature=QgsGeometry.fromPointXY(QgsPointXY(float(x), float(y)))
    pointsList.append(point_feature)
    #print(x,y)
print(pointsList)
#Create a new point layer
mem_vectorLyr =  QgsVectorLayer('Point?crs=epsg:4326&field=name:string(25)&code=population:integer', 'centroid_points' , "memory")
prov = mem_vectorLyr.dataProvider()#get data provider

root = QgsProject.instance() #get layer root
feats = [ QgsFeature() for feature in range(len(pointsList)) ]

for feature, feat in enumerate(feats):
    feat.setAttributes([feature])
    feat.setGeometry(featureList[feature])

prov.addFeatures(feats) #Add points feature layer
root.addMapLayer(mem_vectorLyr) # Add layer to root
#Set symbology for the point layer

#save the layer

