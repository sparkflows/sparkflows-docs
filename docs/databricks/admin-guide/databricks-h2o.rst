Run H2O Job on Databricks
======================

Fire Insights provides a range of H2O processors. 

To run H2O jobs effectively in Fire Insights, follow the steps given below:

#. Access the **Advanced options** of your **Databricks cluster configuration**.
#. Within the configuration, locate and modify the following Spark parameters, setting their values to **false**:

   ::

        spark.speculation false
        spark.dynamicAllocation.enabled false


