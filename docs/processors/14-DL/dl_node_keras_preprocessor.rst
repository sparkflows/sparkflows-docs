Keras Preprocessor
=========== 



Type
--------- 

pyspark

Class
--------- 

fire.nodes.dl.NodeKerasPreprocessor

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - PreprocessorCode
        - PreprocessorCode
      * - preprocessorCode
        - PreprocessorCode
        - PySpark code to be run. Input dataframe : "inDF", SparkContext : "sc", SQLContext : "sqlContext",  Output/Result dataframe should be registered as a temporary table - df.registerTempTable("outDF")




