Running H2O Job on Databricks
======================

Sparkflows comes with a number of H2O processors.

In order to run the J2O jobs, make sure to add the below Spark configurations in Advanced options of databricks cluster Configuration.

::

    spark.speculation false
    spark.dynamicAllocation.enabled false

.. note:: Make sure to change the default value of above parameters to false
