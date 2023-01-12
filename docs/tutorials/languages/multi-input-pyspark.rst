Multi-Input Pyspark Examples
==========================

This workflow reads in dataset's and pass the multiple input's MultiInputpyspark node.
-------

The below workflow:

* Reads the data.
* In MultiInputpyspark, read data from multiple input's and do the join.
* Prints the result.

.. figure:: ../../_assets/tutorials/languages/multi-input-pyspark/1.png
   :alt: MultiInputpyspark
   :width: 90%
   
Reading CSV file
---------------------

.. figure:: ../../_assets/tutorials/languages/multi-input-pyspark/2.png
   :alt: MultiInputpyspark
   :width: 90%



MultiInputPySpark
---------------------
Custom code by using the multiple inputs.

Example code to join the 2 input dataframe.

::

    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *
    from fire.workflowcontext import WorkflowContext 
    
    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDFs:[DataFrame], cust_dict:dict):
      df1 = inDFs[0]  #get the first dataframe
      df2 = inDFs[1]	#get the second dataframe
      outdf = df1.join(df2, ['id'])
      return outdf
      


.. figure:: ../../_assets/tutorials/languages/multi-input-pyspark/3.png
   :alt: MultiInputpyspark
   :width: 90%
   
   

