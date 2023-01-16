Data Preparation miscellaneous
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
   * - Sort By
     - It sorts incoming dataset on selected columns.
   * - Sort Columns
     - It changes order of columns in the output as per selection.
   * - Transpose
     - It transposes incoming dataset against on the selected column.
   * - Windows Analytics
     - It selects a value by application of windows functions such as first_val/last_val within a group of rows.
   * - Windows Ranking
     - It ranks rows within a group using a windows function.   
   * - Flatten
     - It adds new columns for each element of a struct present in a Column data.   
   * - Explode
     - It adds new rows for each value of an array data that is contained in a column data.
   * - Hive Incremental
     - It facilitates reading data from a Hive table incrementally using watermark data.
   * - Save Watermark
     - It facilitates saving updated status information so that new data are read during next cycle.
     
 
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
   
Sort By
----------------------------------------

Below is a sample workflow which contains ``Sort By`` processor in Fire Insights. It demonstrates usage of ``Sort By`` node to sort incoming dataset on selected columns.

It does following processing of data:

*	Reads incoming Dataset.
*	Sorts incoming dataset on selected columns using ``Sort By`` node.
*	Prints sorted dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/sortby-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/sortby-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Sort By Node configuration**

*	``Sort By`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Description of sorting operation needs to be entered in ``Description`` box.
*	Column used to sort incoming dataset is to be selected in ``Columns`` list.
*	Order in which output is to be displayed; either in ascending or descending order of selected column is to be selected in ``Sorting Order`` list.
*	Output would be a Sorted dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/sortby-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Sort By Node output**

Output of ``Sort By`` node would display a Sorted dataset.

.. figure:: ../../_assets/user-guide/data-preparation/others/sortby-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   

Sort Columns
----------------------------------------

Below is a sample workflow which contains ``Sort Columns`` processor in Fire Insights. It demonstrates usage of ``Sort Columns`` node to change order of columns in the output as per selection.

It does following processing of data:

*	Reads incoming Dataset.
*	Changes order of columns in the output as per selection using ``Sort Columns`` node.
*	Prints output dataset displaying columns sorted in the selected order.

.. figure:: ../../_assets/user-guide/data-preparation/others/sortcolumns-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/sortcolumns-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Sort Columns Node configuration**

*	``Sort Columns`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Action defines the column sorting pattern to be used.
*	``A-Z`` action is to be selected if columns need to be sorted in ascending order of column names.
*	``Z-A`` action is to be selected if columns need to be sorted in descending order of column names. Similarily other action needs to be selected based on need.
*	Output would be a dataset displaying columns sorted in the selected order.

.. figure:: ../../_assets/user-guide/data-preparation/others/sortcolumns-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Sort Columns Node output**

Output of ``Sort Columns`` node would display a dataset displaying columns sorted in the selected order.

.. figure:: ../../_assets/user-guide/data-preparation/others/sortcolumns-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   

Transpose
----------------------------------------

Below is a sample workflow which contains ``Transpose`` processor in Fire Insights. It demonstrates usage of ``Transpose`` node to transpose incoming dataset against on the selected column.

It does following processing of data:

*	Reads incoming Dataset.
*	Transpose incoming dataset against on the selected column using ``Transpose`` node. Incoming dataset needs to have all columns of same datatype.
*	Prints output dataset displaying transposed dataset against selected column.

.. figure:: ../../_assets/user-guide/data-preparation/others/transpose-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/transpose-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Transpose Node configuration**

*	``Transpose`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Column against which incoming dataset is to be transposed is to be selected in ``TransposeByColumn Name`` list.
*	Data of the selectd Column would be displayed in rows in the output and other columns data would be displayed in columns. 
*	Output would be a dataset displaying transposed dataset against selected column.

.. figure:: ../../_assets/user-guide/data-preparation/others/transpose-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Transpose Node output**

Output of ``Transpose`` node would display a dataset displaying transposed dataset against selected column.

.. figure:: ../../_assets/user-guide/data-preparation/others/transpose-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
   
Windows Analytics
----------------------------------------

Below is a sample workflow which contains ``Windows Analytics`` processor in Fire Insights. It demonstrates usage of ``Windows Analytics`` node to select a value by application of windows functions such as first_val / last_val within a group of rows.

It does following processing of data:

*	Reads incoming Dataset.
*	Selects a value by application of windows functions such as first_val / last_val within a group of rows using ``Windows Analytics`` node.
*	Prints output dataset with a value selected within a group using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/winanalytics-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/winanalytics-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Windows Analytics Node configuration**

*	``Windows Analytics`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Column that is used to define partition is to be entered in ``PartitionBy`` box.
*	Column used to order rows is to be entered in ``OrderBy`` box.
*	Windows function to be used is to be selected in ``Windows Function`` list.
*	Column that is used to compute output by application of Windows Function is to be selected in ``Analytics Column`` list.
*	Lead and Lag value to be used for selection is to be entered in ``Window Offset`` box.
*	Output would be a dataset with a value selected within a group using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/winanalytics-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Windows Analytics Node output**

Output of ``Windows Analytics`` node would display a dataset with a value selected within a group using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/winanalytics-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    

Windows Ranking
----------------------------------------

Below is a sample workflow which contains ``Windows Ranking`` processor in Fire Insights. It demonstrates usage of ``Windows Ranking`` node to rank rows within a group using a windows function.

It does following processing of data:

*	Reads incoming Dataset.
*	Ranks rows within a group using a windows function using ``Windows Ranking`` node.
*	Prints output dataset with rank value for each row computed using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/winrank-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/winrank-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Windows Ranking Node configuration**

*	``Windows Ranking`` node is configured as below.
*	Input of this node are the incoming dataset.
*	Column that is used to define partition is to be entered in ``PartitionBy`` box.
*	Column used to order rows is to be entered in ``OrderBy`` box.
*	Windows function to be used is to be selected in ``Window Function`` list.
*	Output would be a dataset with rank value for each row computed using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/winrank-config.png
   :alt: dataprepothers_userguide
   :width: 90%

**Windows Ranking Node output**

Output of ``Windows Ranking`` node would display a dataset with rank value for each row computed using windows function.

.. figure:: ../../_assets/user-guide/data-preparation/others/winrank-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    

Flatten
----------------------------------------

Below is a sample workflow which contains ``Flatten`` processor in Fire Insights. It demonstrates usage of ``Flatten`` node to add new columns for each element of a struct present in a Column data.   

It does following processing of data:

*	Reads incoming Dataset.
*	Adds new columns for each element of a struct present in a Column data using ``Flatten`` node.
*	Prints output dataset with new columns added to it.

.. figure:: ../../_assets/user-guide/data-preparation/others/flatten-workflow.png
   :alt: dataprepothers_userguide
   :width: 60%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/flatten-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 90%
   
.. figure:: ../../_assets/user-guide/data-preparation/others/flatten-incoming-dataset1.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Flatten Node configuration**

*	``Flatten`` node is configured as below.
*	Input of this node is an incoming dataset i.e. a json data.
*	Struct whose elements needs to be added as new column is to be selected in the ``Schema`` section. In this example ``Address`` column contains struct data.
*	Elements that need to be added as columns is to be selected.
*	Output of this node would be a dataset with new columns added to it.

.. figure:: ../../_assets/user-guide/data-preparation/others/flatten-config.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Flatten Node output**

Output of ``Flatten`` node would be a dataset with new columns added to it.

.. figure:: ../../_assets/user-guide/data-preparation/others/flatten-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
	 
Explode
----------------------------------------

Below is a sample workflow which contains ``Explode`` processor in Fire Insights. It demonstrates usage of ``Explode`` node to add new rows for each value of an array data that is contained in a column data.

It does following processing of data:

*	Reads incoming Dataset.
*	Adds new rows for each value of an array data that is contained in a column data using ``Explode`` node.
*	Prints output dataset with new rows added to it.

.. figure:: ../../_assets/user-guide/data-preparation/others/explode-workflow.png
   :alt: dataprepothers_userguide
   :width: 60%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/others/explode-incoming-dataset.png
   :alt: dataprepothers_userguide
   :width: 30%
   
**Explode Node configuration**

*	``Explode`` node is configured as below.
*	Input of this node is an incoming dataset i.e. a complex json data.
*	Array data whose elements needs to be added as new rows is to be selected in the ``Input Columns`` section. In this example ``Members`` column contains Array data.
*	After inserting rows using values from Array data ``Flatten`` is used to extract elements values.
*	Output of this node would be a dataset with new rows added to it.

.. figure:: ../../_assets/user-guide/data-preparation/others/explode-config.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Explode Node output**

Output of ``Explode`` node would be a dataset with new rows added to it.

*	Array Data from the input as displayed in the output.

.. figure:: ../../_assets/user-guide/data-preparation/others/explode-printnode-output.png
   :alt: dataprepothers_userguide
   :width: 90%       	    
	 
*	Array Data from the input added as new rows using ``Explode`` node and further data from each array element is added as new column using ``Flatten`` node.

.. figure:: ../../_assets/user-guide/data-preparation/others/explode-printnode-output1.png
   :alt: dataprepothers_userguide
   :width: 90%       	    

Hive Incremental
----------------------------------------

Below is a sample workflow which contains ``Hive Incremental`` processor in Fire Insights. It demonstrates usage of ``Hive Incremental`` node to read data from a Hive table incrementally using watermark data.

It does following processing of data:

*	Reads incoming data from a Hive table incremenatlly using ``Hive Incremental`` node.
*	Saves data to the target table and update watermark data using ``Save Watermark`` node.

.. figure:: ../../_assets/user-guide/data-preparation/others/hiveincremental-workflow.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Hive Incremental Node configuration**

*	``Hive Incremental`` node is configured as below.
*	Hive DB information needs to be entered in ``Hive Database`` field. ``Browse Hive DB`` button can be used to selected Hive Database based on the Hive connection defined.
*	Hive Table information needs to be entered in ``Hive Table`` field. ``Browse Hive Table`` button can be used to selected Hive Table.
*	Path of the watermark data needs to be entered in ``Path`` field. Browse buttons can be used to selected the path.
*	Columns that are used to filter incoming data based on Watermark information needs to be entered in ``Filterfields`` field. Multiple columns can be entered separated by comma.
* 	Click on ``Refresh Schema`` button to fetch schema information from the table selected.

.. figure:: ../../_assets/user-guide/data-preparation/others/hiveincremental-config.png
   :alt: dataprepothers_userguide
   :width: 90%
   
**Save Watermark Node to save status**

*	Updated Watermark status information is saved using ``Save Watermark`` node.
*	During next cycle of execution updated status information is used to read new Hive data.

**Save Watermark Node Configuration**

*	``Save Watermark`` node is configured as below.
*	Path of the watermark data needs to be entered in ``Path`` field. Browse buttons can be used to selected the path.

.. figure:: ../../_assets/user-guide/data-preparation/others/hiveincremental-savewatermark.png
   :alt: dataprepothers_userguide
   :width: 90%
