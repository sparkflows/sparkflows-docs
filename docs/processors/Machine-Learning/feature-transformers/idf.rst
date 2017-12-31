
IDF
========== 

Compute the Inverse Document Frequency (IDF) given a collection of documents.

Type
---------- 

ml-transformer

Class
---------- 

fire.nodes.ml.NodeIDF

Fields
---------- 

+------------+---------------+---------------------------------------------------------+
| Name       | Title         | Description                                             |
+============+===============+=========================================================+
| inputCol   | Input Column  | Input Column Name                                       |
+------------+---------------+---------------------------------------------------------+
| outputCol  | Output Column | Output column name                                      |
+------------+---------------+---------------------------------------------------------+
| minDocFreq | MinDocFreq    | The minimum of documents in which a term should appear. |
+------------+---------------+---------------------------------------------------------+