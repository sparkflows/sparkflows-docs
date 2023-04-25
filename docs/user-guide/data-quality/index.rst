Data Quality
------

Fire Insights provides powerful capabilities for monitoring data quality. It provides for various processors that aid in validation of data to ensure that only high quality, reliable, and accurate data is fed into the process of analysis, reporting, and decision-making.

Data Quality Processors in Fire Insights
------

.. list-table:: Great Expectations based Data Quality Processors in Fire Insights
   :widths: 30 50
   :header-rows: 1

   * - Title
     - Description
   * - ExpectColumnValuesToBeInBetween
     - This node is used to define an expectation that the values in a particular column of a dataset should fall within a specified range.  
     
   * - ExpectColumnValuesToBeNull
     - This node is used to define an expectation that the values in a particular column of a dataset should be null or None.  
   
   * - ExpectColumnValuesToBeUnique
     - This node is used to define an expectation that the values in a particular column of a dataset should be unique, i.e., there should be no duplicate values in the column.
     
   * - ExpectColumnValuesToNotBeNull
     - This node is used to define an expectation that the values in a particular column of a dataset should not be null or None.
	
   * - ExpectTableRowCountToBeBetween
     - This node is used to define an expectation that the number of rows in a dataset should fall within a specified range.
	

Expect Column Values To Be In Between
--------

Below is a sample workflow which contains **ExpectColumnValuesToBeInBetween processor** in Fire Insights. It demonstrates the usage of ExpectColumnValuesToBeInBetween node to validate whether the selected column entries lie between the specified range (i.e., between specified minimum and maximum values).

It does the following processing of data:

* Reads the incoming dataset.
* Validates the columns with entries to be between the specified range.
* Prints the output using the print node.

ExpectColumnValuesToBeInBetween Node Sample Workflow
=========

.. figure:: ../../_assets/user-guide/data-quality/expect-col-val-in-betwn-WF.png
   :alt: datacleaning_userguide
   :width: 75%
   
Incoming Dataset
=======

.. figure:: ../../_assets/user-guide/data-quality/input-data.png
   :alt: datacleaning_userguide
   :width: 75%

ExpectColumnValuesToBeInBetween Node Configuration
=======

**Configuration Details:**

* Input of this node is the incoming dataset.
* Column(s) for which the values need to be checked against the specified range is to be selected in the variables column.
* Range of values against which each column entry needs to be checked is to be entered in min and max columns respectively for each selected column.        


.. figure:: ../../_assets/user-guide/data-quality/expect-col-val-in-between-config.png
   :alt: datacleaning_userguide
   :width: 75%
   
ExpectColumnValuesToBeInBetween Node Output
=======

Output of this node would produce the following results:

* If the expectation is met (i.e., all values in the column are within the specified range), then the node will return value of the sucess column as **True**.
* If the expectation is not met (i.e., at least one value in the column falls outside of the specified range), then the node will return the value of the success column as **False**.

.. figure:: ../../_assets/user-guide/data-quality/expect-col-val-in-between-output.png
   :alt: datacleaning_userguide
   :width: 75% 
   



























