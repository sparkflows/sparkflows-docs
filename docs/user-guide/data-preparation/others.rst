Data Preparation Others
==========

Fire Insights provide processors for Data Preparation


Data Preparation Processors in Fire Insights
----------------------------------------


.. list-table:: Data Preparation Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Columns Rename
     - It renames incoming dataset columns.
   * - Round Value
     - It converts incoming value to a decimal value of specified precision.
   * - Count
     - It fetches and prints row count of incoming dataset.
   * - Moving Windows Function
     - It computes moving values such as average/max/min by application of specified function on the windows of rows defined.
   * - Multi Windows Analytics
     - It selects a value by application of windows functions such as first_val/last_val on a group of rows.
   * - Multi Windows Ranking
     - It ranks rows within a group using a windows function.
   * - Sample
     - It selects a sample dataset out of incoming dataset.
     
 
Columns Rename
----------------------------------------

Below is a sample workflow which contains ``Columns Rename`` processor in Fire Insights. It demonstrates usage of ``Columns Rename`` node to rename incoming dataset columns.

It does following processing of data:

*	Reads incoming Dataset.
*	Renames incoming dataset columns using ``Columns Rename`` node.
*	Prints output dataset with incoming columns renamed to new values.

.. figure:: ../../_assets/user-guide/data-preparation/others/colsrename-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/colsrename-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Columns Rename Node configuration**

*	``Columns Rename`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Incoming columns that needs to be renamed is to be selected in ``Current Column Names`` list.
*	New column name is to be entered in ``Columns New Name`` box.
*	A new ``Variables List`` row needs to be added for additional renaming requirement.	
*	Output of this node would be a dataset with incoming columns renamed to new values.

.. figure:: ../../_assets/user-guide/data-preparation/others/colsrename-config.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Columns Rename Node output**

Output of ``Columns Rename`` node would be a dataset with incoming columns renamed to new values.

.. figure:: ../../_assets/user-guide/data-preparation/others/colsrename-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    

Round Value
----------------------------------------

Below is a sample workflow which contains ``Round Value`` processor in Fire Insights. It demonstrates usage of ``Round Value`` node to convert incoming value to a decimal value of specified precision.

It does following processing of data:

*	Reads incoming Dataset.
*	Converts incoming value to a decimal value of specified precision using ``Round Value`` node.
*	Prints output dataset with incoming values converted to decimal values of specified precision.

.. figure:: ../../_assets/user-guide/data-preparation/others/roundvalue-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/roundvalue-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Round Value Node configuration**

*	``Round Value`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Columns whose values are to be rounded off are to be selected in ``Input Column`` list.
*	Precision expected in the output rounded value is to be entered in ``Precision`` box.
*	Output of this node would be a dataset with incoming values converted to decimal values of specified precision.

.. figure:: ../../_assets/user-guide/data-preparation/others/roundvalue-config1.png
   :alt: dataprepothers_userguide
   :width: 90%

.. figure:: ../../_assets/user-guide/data-preparation/others/roundvalue-config2.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Round Value Node output**

Output of ``Round Value`` node would be a dataset with incoming values converted to decimal values of specified precision.

.. figure:: ../../_assets/user-guide/data-preparation/others/roundvalue-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    

Count
----------------------------------------

Below is a sample workflow which contains ``Count`` processor in Fire Insights. It demonstrates usage of ``Count`` node to fetch and print row count of incoming dataset.

It does following processing of data:

*	Reads incoming Dataset.
*	Fetches and prints row count of incoming dataset using ``Count`` node.
*	Prints row count of incoming dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/count-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/count-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Count Node configuration**

*	``Count`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Column in the output to display count is to be entered in ``Variable Name`` box.
*	If count is to be displayed in the output then True needs to be selected in ``PrintCount`` list.
*	Output of this node would display row count of incoming dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/count-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Count Node output**

Output of ``Count`` node would display row count of incoming dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/count-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    

Moving Windows Function
----------------------------------------

Below is a sample workflow which contains ``Moving Windows Function`` processor in Fire Insights. It demonstrates usage of ``Moving Windows Function`` node to compute moving values such as average/max/min by application of specified function on the windows of rows defined.

It does following processing of data:

*	Reads incoming Dataset.
*	Computes moving values such as average/max/min by application of specified function on the windows of rows defined using ``Moving Windows Function`` node.
*	Prints output dataset with computed moving average calculated in the windows defined.

.. figure:: ../../_assets/user-guide/data-preparation/others/movwinfn-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/movwinfn-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Moving Windows Function Node configuration**

*	``Moving Windows Function`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Number of rows above the current row that needs to be included in the windows is to be entered in ``Window Start`` box. If it contains -2 then window for row would start at 2 rows above.
*	Number of rows below the current row that needs to be included in the windows is to be entered in ``Window End`` box. If it contains 2 then window for row would end at 2 rows below.
*	Partition defines boudary of windows definition. Column that is used to define partition is to be selected in ``Partition Column Name`` list.
*	Column used to order rows within a partition is to be selected in ``Order Column Name`` list.
*	Column that is used to compute output by application of Windows Function is to be selected in ``Input Columns`` list.
*	Windows function to be used is to be selected in ``Functions`` list.
*	A new row needs to be added for each additional computation requirement. 
*	Output would be a dataset with computed moving average calculated in the windows defined.

.. figure:: ../../_assets/user-guide/data-preparation/others/movwinfn-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Moving Windows Function Node output**

Output of ``Moving Windows Function`` node would display a dataset with computed moving average calculated in the windows defined.

.. figure:: ../../_assets/user-guide/data-preparation/others/movwinfn-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   

Multi Windows Analytics
----------------------------------------

Below is a sample workflow which contains ``Multi Windows Analytics`` processor in Fire Insights. It demonstrates usage of ``Multi Windows Analytics`` node to select a value by application of windows functions such as first_val / last_val within a group of rows.

It does following processing of data:

*	Reads incoming Dataset.
*	Selects a value by application of windows functions such as first_val / last_val within a group of rows using ``Multi Windows Analytics`` node.
*	Prints output dataset with a value selected within a group using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinanalytics-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinanalytics-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Multi Windows Analytics Node configuration**

*	``Multi Windows Analytics`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Column that is used to compute output by application of Windows Function is to be selected in ``AnalyticsColumn`` list.
*	Windows function to be used is to be selected in ``Windows Function`` list.
*	Column that is used to define partition is to be entered in ``PartitionBy`` box.
*	Column used to order rows is to be entered in ``OrderBy`` box.
*	Column name in the output to list computed value is to be entered in ``OutputColumn`` box.
*	Output would be a dataset with a value selected within a group using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinanalytics-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Multi Windows Analytics Node output**

Output of ``Multi Windows Analytics`` node would display a dataset with a value selected within a group using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinanalytics-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   

Multi Windows Ranking
----------------------------------------

Below is a sample workflow which contains ``Multi Windows Ranking`` processor in Fire Insights. It demonstrates usage of ``Multi Windows Ranking`` node to rank rows within a group using a windows function.

It does following processing of data:

*	Reads incoming Dataset.
*	Ranks rows within a group using a windows function using ``Multi Windows Ranking`` node.
*	Prints output dataset with rank value for each row computed using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinrank-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinrank-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Multi Windows Ranking Node configuration**

*	``Multi Windows Ranking`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Windows function to be used is to be selected in ``WindowsFunction`` list.
*	Column that is used to define partition is to be entered in ``PartitionBy`` box.
*	Column used to order rows is to be entered in ``OrderBy`` box.
*	Column name in the output to list computed value / rank is to be entered in ``OutputColumn`` box.
*	Output would be a dataset with rank value for each row computed using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinrank-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Multi Windows Ranking Node output**

Output of ``Multi Windows Ranking`` node would display a dataset with rank value for each row computed using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/mulwinrank-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   

Sample
----------------------------------------

Below is a sample workflow which contains ``Sample`` processor in Fire Insights. It demonstrates usage of ``Sample`` node to select a sample dataset out of incoming dataset.

It does following processing of data:

*	Reads incoming Dataset.
*	Selects a sample dataset out of incoming dataset using ``Sample`` node.
*	Prints Sample dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/sample-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/sample-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Sample Node configuration**

*	``Sample`` node is configured as below.
*	Input of this node are the incoming dataset.
*	If selected sample can be picked again in subsequent sampling run then ``Replacement Values`` is to be selected as true.
*	Fraction of incoming dataset that needs to be selected as sample is to be entered in ``Fraction`` box.
*	Seed value of the sample selected is to be entered in ``OrderBy`` box. Same sample would be picked if same seed value is entered for multiple runs. 
*	Output would be a Sample dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/sample-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Sample Node output**

Output of ``Sample`` node would display a Sample dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/sample-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   

