Data Exploration
==========

Fire Insights provide a number of features for Data Exploration


Data Exploration Processors in Fire Insights
----------------------------------------


.. list-table:: Data Exploration Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - ColumnsCardinality
     - Distribution of categorical data. Calculates the count of records for each unique value for the column specified
   * - Correlation
     - calculates the correlation between two series of data
   * - CrossTab
     - Displays distribution of data for all combination of Categorical data series
   * - DistinctValuesInColumn   
     - Displays distinct combination data present in the select data series
   * - Flag Outlier
     - Flag the outlier based on the selected column using Box-and-Whisker technique
   * - GraphMonthDistribution  
     - This node Finds the distribution of months from Date values
   * - NullValuesInColumn  
     - Number of Null Values in Selected Columns
   * - Skewness And Kurtosis
     - Need To Add
   * - Summary Statistics
     - Summary statistics provide useful information about sample data. eg: measures of spread
 
Columns Cardinality
----------------------------------------

Below is a sample workflow which contains ``Columns Cardinality`` processor in Fire Insights. It demonstrates usage of ``Columns Cardinality`` node to display Categorical distribution of data. It displays count of rows for each distinct values in the selected columns (Categories).

It does following processing of data:

*	Reads incoming Dataset
*	Displays Categorical distribution of data using ``Columns Cardinality`` node. It displays count of rows for each distinct values in the selected columns (Categories). More than one column can be seclected to display distribution of data.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-workflow.png
   :alt: dataexploration_userguide
   :width: 60%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-incoming-dataset.png
   :alt: dataexploration_userguide
   :width: 90%

**Columns Cardinality Node configuration**

*	``Columns Cardinality`` node is configured as below.
*	Input of this node is the incoming dataset.
*	``Max Values To Display`` specifies the maximum Categorical data to be displayed. It denotes maximum number of distinct values in the selected columns for which count needs to be displayed.
*	Columns for which distribution needs to be displayed is to be selected in ``Column Names`` list. More than one column can be selected. Data for each columns would be displayed separately.
*	Output of this node would contain count of each distinct values in the selected columns.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-config.png
   :alt: dataexploration_userguide
   :width: 90%
   
**Columns Cardinality Node output**

Output of ``Columns Cardinality`` node displaying count distinct values for each selected columns and categorical data (count of distinct values) for each selected columns in the node.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-printnode-output1.png
   :alt: dataexploration_userguide
   :width: 90%       	    
   
.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-printnode-output2.png
   :alt: dataexploration_userguide
   :width: 90%       	 
   
.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-printnode-output3.png
   :alt: dataexploration_userguide
   :width: 90%       	 
   
Correlation
----------------------------------------

Below is a sample workflow which contains ``Correlation`` processor in Fire Insights. It demonstrates usage of ``Correlation`` node to display correlation between data of selected columns.

It does following processing of data:

*	Reads incoming Dataset
*	Displays correlation between data of selected columns using ``Correlation`` node. More than two columns can be selected to identify correlation. It displays correlation in color codes along with scale to read highly and less correlated data series.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-workflow.png
   :alt: dataexploration_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-incoming-dataset.png
   :alt: dataexploration_userguide
   :width: 90%

**Correlation Node configuration**

*	``Correlation`` node is configured as below.
*	Input of this node is the incoming dataset.
*	All Numeric between whom correlation is to be identified are to be selected in ``Input Column For Correlation`` list.
*	Title of the Correlation Matrix needs to be entered in ``Title``.
*	Output of this node would display correlation between all the selected columns.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-config.png
   :alt: dataexploration_userguide
   :width: 90%
   
**Correlation Node output**

Output of ``Correlation`` node displaying correlation between all the selected columns along with the color code. Below output displays Correlation Matrix along with Color Code Scale. Green indicates highly correlated and Red less. From the below output we can identify that ``Customer Service Calls`` and ``Churn`` are correlated.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-printnode-output.png
   :alt: dataexploration_userguide
   :width: 90%       	    
   
Cross Tab
----------------------------------------

Below is a sample workflow which contains ``Cross Tab`` processor in Fire Insights. It demonstrates usage of ``Cross Tab`` node to display distribution of data between all possible combination of all distinct values of two series.

It does following processing of data:

*	Reads incoming Dataset
*	Displays distribution of data between all possible combination of all distinct values of two series using ``Cross Tab`` node. Distribution can be displayed between any two Categorical columns from incoming dataset.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-workflow.png
   :alt: dataexploration_userguide
   :width: 60%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-incoming-dataset.png
   :alt: dataexploration_userguide
   :width: 90%

**Cross Tab Node configuration**

*	``Cross Tab`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Any two categorical columns from incoming dataset can be selected as ``Firstcolumn`` and ``Secondcolumn``. All distinct values from ``Firstcolumn`` would be displayed as rows and all distinct values from ``Secondcolumn`` would be displayed as columns of the Table. Row count of Row and Column value combination would be displayed as distribution.
*	Output of this node would display table depicting distribution of data between two series.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-config.png
   :alt: dataexploration_userguide
   :width: 90%
   
**Cross Tab Node output**

Output of ``Cross Tab`` node displaying distribution between ``Firstcolumn`` and ``Secondcolumn`` in tabular format.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-printnode-output.png
   :alt: dataexploration_userguide
   :width: 90%       	    
   

Distinct Values In Column
----------------------------------------

Below is a sample workflow which contains ``Distinct Values In Column`` processor in Fire Insights. It demonstrates usage of ``Distinct Values In Column`` node to display distinct combination of values in the selected columns.

It does following processing of data:

*	Reads incoming Dataset
*	Displays distinct combination of values in the selected columns using ``Distinct Values In Column`` node. If only one column is selected then it displays Distinct values present in that column. If more than one column is selected then it displays distinct combination of values present in the selected columns.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-workflow.png
   :alt: dataexploration_userguide
   :width: 60%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-incoming-dataset.png
   :alt: dataexploration_userguide
   :width: 90%

**Distinct Values In Column Node configuration**

*	``Distinct Values In Column`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Columns between which unique combination of data is to be identified are to be selected in ``Column Names`` list. One or more columns can be selected.
*	Output of this node would display distinct combination of values in the selected columns.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-config.png
   :alt: dataexploration_userguide
   :width: 90%
   
**Distinct Values In Column Node output**

Output of ``Distinct Values In Column`` node displaying distinct combination of values in the selected columns.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-printnode-output.png
   :alt: dataexploration_userguide
   :width: 90%       	    
   

Flag Outlier
----------------------------------------

Below is a sample workflow which contains ``Flag Outlier`` processor in Fire Insights. It demonstrates usage of ``Flag Outlier`` node to identify whether a data point is outlier in a series or not based on the lower and upper quantile set.

It does following processing of data:

*	Reads incoming Dataset
*	Identifies whether a data point is outlier in a series or not based on the lower and upper quantile set using ``Flag Outlier`` node. It can be checked agaist a numeric column only.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-workflow.png
   :alt: dataexploration_userguide
   :width: 60%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-incoming-dataset.png
   :alt: dataexploration_userguide
   :width: 90%

**Flag Outlier Node configuration**

*	``Flag Outlier`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Numeric Column in which datapoints are to be identified as outlier needs to be selected in ``Input Column To Flag The Outlier`` list.
*	``Lowerquantile`` and ``Upperquantile`` values need to be entered in the respective boxes. Datapoint would be checked against these values to flag it as outlier.
*	Output of this node would display Outlier flag for the datapoint in the selected column.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-config.png
   :alt: dataexploration_userguide
   :width: 90%
   
**Flag Outlier Node output**

Output of ``Flag Outlier`` node displaying Outlier flag for datapoints in the selected column.

.. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-printnode-output.png
   :alt: dataexploration_userguide
   :width: 90%       	    
   
