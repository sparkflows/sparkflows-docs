MinMaxScaler
=========== 

MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1])

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeMinMaxScaler

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column 
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - max
        - Max
        - The upper bound after transformation, shared by all features
      * - min
        - Min
        - The lower bound after transformation, shared by all features




