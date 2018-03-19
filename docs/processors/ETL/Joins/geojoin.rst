
GeoJoin
========== 

This node joins the incoming dataframes

Input
---------- 

This node takes in 2 DataFrames as input and produces one DataFrame as output

Type
---------- 

join

Class
---------- 

fire.nodes.etl.NodeGeoJoin

Fields
---------- 

+--------------+------------------+---------------------------------------+
| Name         | Title            | Description                           |
+==============+==================+=======================================+
| latitudeCol  | Latitude Column  | Latitude Column from first DataFrame  |
+--------------+------------------+---------------------------------------+
| longitudeCol | Longitude Column | Longitude Column from first DataFrame |
+--------------+------------------+---------------------------------------+
| polygonCol   | Polygon Column   | Polygon Column from second DataFrame  |
+--------------+------------------+---------------------------------------+