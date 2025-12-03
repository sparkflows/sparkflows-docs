Custom Node Development in Python
===================================

Custom Nodes in Sparkflows can be exported as zip files and then subsequently imported into Sparkflows.


Execution Code
--------------


.. code-block:: python
   :linenos:
   
    from pyspark.sql import DataFrame, SparkSession
    from fire.workflowcontext import WorkflowContext
    import scorecardpy as sc

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, parameters: dict):
        # Write your code here by using input dataframe i.e inDF and pass the output result as outDF dataframe.

        pandas_df = inDF.toPandas()
        variables = ["purpose"]
        stopLimit = 0.1
        countDistrLimit = 0.05
        binNumLimit = 8
        method = "tree"
        positive = "bad|1"
        workflowContext.outStr(id, "Method: " + parameters['method'] + ", Positive:" + parameters['positive'])

        bins = sc.woebin(pandas_df, y="creditability", x=variables, stop_limit=float(stopLimit),
                     count_distr_limit=float(countDistrLimit),
                     bin_num_limit=int(binNumLimit), method=method, positive=positive)
        bins_ply = sc.woebin_ply(pandas_df, bins)
        spark_df = spark.createDataFrame(bins_ply)
        outDF = spark_df
        return outDF
    
   

Schema Propagation Code
-----------------------

.. code-block:: python
   :linenos:
   
    from fire.workflowengine.workflow import JobContext
    from fire.workflowengine.fireschema import FireSchema

    def schema(inputSchema: FireSchema, parameters: dict):
        #to add new column
        #inputSchema.append("house_type", "string")

        #to drop a column
        #inputSchema.drop("id")
        inputSchema.append('purpose_woe', 'double')

        return inputSchema
    


