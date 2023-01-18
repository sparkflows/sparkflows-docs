Run H2O Job on Databricks
======================

Fire Insights comes with a number of H2O processors.

In order to run the H2O jobs, make sure to add the below given Spark configurations in Advanced options of databricks cluster Configuration.

::

    spark.speculation false
    spark.dynamicAllocation.enabled false

.. note:: Make sure to change the default value of above parameters to false.
