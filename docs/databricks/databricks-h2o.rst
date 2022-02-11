Running H2O Job on Databricks
======================

Fire Insights comes up with different h2o processors.

Inorder to run those Jobs make sure to add Spark configurations in Advanced options of databricks cluster Configuration.

::

    spark.speculation false
    spark.dynamicAllocation.enabled false
