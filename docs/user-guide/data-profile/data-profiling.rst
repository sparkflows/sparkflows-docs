Data Profiling Processors
==========

Fire Insights provides a range of processors or nodes for exploring and analyzing data efficiently. These processors help in identifying data patterns, correlations, distributions, and outliers, enabling better decision-making. Below is a structured workflow that details the various data profiling processors available in Fire Insights.

.. figure:: ../../_assets/user-guide/data-quality/2_Data_Profiling_Workflow.png
   :alt: Data Profiling Workflow
   :width: 100%


Data Profiling Processors in Fire Insights
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - ColumnsCardinality
     - Distribution of categorical data. Calculates the count of records for each unique value for the column specified.
   * - Correlation
     - Computes and displays the correlation between two series of data.
   * - CrossTab
     - Displays distribution of data for all combination of categorical data series.
   * - DistinctValuesInColumn   
     - Displays distinct combinations of data present in the selected data series.
   * - Flag Outlier
     - Flags the outlier based on the selected column using Box-and-Whisker technique.
   * - Multiflag Outlier
     - Flags outlier on multiple columns using Box-and-Whisker technique.
   * - GraphMonthDistribution  
     - This node displays monthly distribution of data.
   * - GraphWeekDayDistribution  
     - This node displays weekday wise distribution of data.     
   * - GraphYearDistribution  
     - This node displays yearly distribution of data.     
   * - Histogram  
     - This node displays distribution of data spread across multiple bins.    
   * - NullValuesInColumn  
     - Number of Null Values in Selected Columns.
   * - Skewness And Kurtosis
     - Displays Skewness (measure of symmetry) and Kurtosis (measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution).
   * - Summary Statistics
     - Summary statistics provide useful information about sample data, e.g. measures of spread.
 
Columns Cardinality
----------------------------------------

Below is a sample workflow that contains Columns Cardinality processor in Fire Insights. It demonstrates the usage of Columns Cardinality node to display categorical distribution of data. It displays count of rows for each distinct values in the selected columns (Categories).

It does the following processing of data:

*	Reads incoming dataset.
*	Displays Categorical distribution of data using Columns Cardinality node. It displays count of rows for each distinct values in the selected columns (Categories). More than one column can be seclected to display distribution of data.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-workflow.png
      :alt: dataexploration_userguide
      :width: 60%
   
**Incoming Dataset**
++++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Columns Cardinality Node Configuration**
+++++++++++++++++++++++++++++++++++++++++++++++

Columns Cardinality node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**MAX VALUES TO DISPLAY:** It specifies the maximum categorical data to be displayed. It denotes maximum number of distinct values in the selected columns for which count needs to be displayed.
*	**COLUMN NAMES:** Select the columns for which distribution needs to be displayed. More than one column can be selected. Data for each columns would be displayed separately, as shown below.

   .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-config.png
      :alt: dataexploration_userguide
      :width: 75%

* Output of this node will contain count of each distinct values in the selected columns.

   
**Columns Cardinality Node output**
+++++++++++++++++++++++++++++++++++++++

The output of Columns Cardinality node displays the count of distinct values for each selected column and categorical data (count of distinct values) for each selected column in the node, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-printnode-output1.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   
  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-printnode-output2.png
     :alt: dataexploration_userguide
     :width: 75%       	 
   
  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/columnscardinality-printnode-output3.png
     :alt: dataexploration_userguide
     :width: 75%       	 
   
Correlation
----------------------------------------

Below is a sample workflow that contains Correlation processor in Fire Insights. It demonstrates the usage of Correlation node to display correlation between data of selected columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays correlation between data of selected columns using Correlation node. More than two columns can be selected to identify correlation. It displays correlation in color codes along with scale to read highly and less correlated data series.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Correlation Node Configuration**
++++++++++++++++++++++++++++++++++++++++++

The Correlation node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**TITLE:** Enter a title of the Correlation Matrix in the box.
*	**INPUT COLUMN FOR CORRELATION:** Selct All Numeric between which the correlation is to be identified in this list. 

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-config.png
     :alt: dataexploration_userguide
     :width: 75%
 
* Output of this node will display the correlation between all the selected columns.
   
**Correlation Node Output**
+++++++++++++++++++++++++++++++++

The output of Correlation node displays correlation between all the selected columns along with the color code as shown below. It displays Correlation Matrix along with Color Code Scale, where green indicates a high correlation and red indicates a low correlation. From the output, we can identify that **Customer Service Calls** and **Churn** are correlated.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/correlation-printnode-output.png
     :alt: dataexploration_userguide
     :width: 60%       	    
   
Cross Tab
----------------------------------------

Below is a sample workflow that contains Cross Tab processor in Fire Insights. It demonstrates the usage of Cross Tab node to display distribution of data between all possible combinations of all distinct values of two series.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays distribution of data between all possible combinations of all distinct values of two series using Cross Tab node. Distribution can be displayed between any two Categorical columns from the incoming dataset.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Cross Tab Node Configuration**
+++++++++++++++++++++++++++++++++++++++

The Cross Tab node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**FIRSTCOLUMN & SECONDCOLUMN:** Select any two categorical columns from the incoming dataset in Firstcolumn and Secondcolumn respectively, as shown below. All distinct values from Firstcolumn will be displayed as rows, while all distinct values from Secondcolumn will be displayed as columns of the Table. The Row count of Row and Column value combination will be displayed as distribution.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display the table depicting distribution of data between the two series.

   
**Cross Tab Node Output**
++++++++++++++++++++++++++

The output of Cross Tab node displays the distribution between Firstcolumn and Secondcolumn in tabular format, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/crosstab-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   

Distinct Values In Column
----------------------------------------

Below is a sample workflow that contains Distinct Values In Column processor in Fire Insights. It demonstrates the usage of Distinct Values In Column node to display distinct combinations of values in the selected columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays distinct combinations of values in the selected columns using Distinct Values In Column node. If only one column is selected then it displays Distinct values present in that column. If more than one column is selected then it displays distinct combinations of values present in the selected columns.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
++++++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Distinct Values In Column Node Configuration**
+++++++++++++++++++++++++++++++++++++++++++++++++++

The Distinct Values In Column node is configured as follows.

*	**INPUT:** Incoming dataset is the input for this node.
*	**COLUMN NAMES:** Select the columns between which unique combination of data is to be identified. One or more columns can be selected, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display distinct combinations of values in the selected columns.

   
**Distinct Values In Column Node Output**
++++++++++++++++++++++++++++++++++++++++++++

The output of Distinct Values In Column node displays the distinct combination of values in the selected columns, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/distinctval-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   

Flag Outlier
----------------------------------------

Below is a sample workflow that contains Flag Outlier processor in Fire Insights. It demonstrates the usage of Flag Outlier node to identify whether a data point is outlier in a series or not based on the lower and upper quantile set.

It does the following processing of data:

*	Reads incoming dataset.
*	Identifies whether a data point is outlier in a series or not based on the lower and upper quantile set using Flag Outlier node. It can be checked against numeric columns only.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Flag Outlier Node Configuration**
+++++++++++++++++++++++++++++++++++++++++++

The Flag Outlier node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	** INPUT COLUMN TO FLAG THE OUTLIER:** Select a Numeric Column in which datapoints are to be identified as outlier from the dropdown.
*	**LOWER QUANTILE & UPPER QUANTILE:** Enter the values of lower and upper quantile in the respective boxes. Datapoint will be checked against these values to flag it as outlier, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display the outlier flag for the datapoint in the selected column.
   
**Flag Outlier Node Output**
++++++++++++++++++++++++++++++++++

The output of Flag Outlier node displays the Outlier Flag for datapoints in the selected column, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/flagoutlier-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   
Multiflag Outlier
----------------------------------------

Below is a sample workflow that contains Multiflag Outlier processor in Fire Insights. It demonstrates the usage of Multiflag Outlier node to identify whether a data point is outlier in a series or not based on the lower and upper quantile set. It can be used to identify outliers in multiple columns. 

It does the following processing of data:

*	Reads incoming dataset.
*	Identifies whether a data point is outlier in a series or not based on the lower and upper quantile set using Flag Outlier node. It can be checked against numeric columns only, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/multiflag-outlier-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
++++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/multiflag-outlier-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Multiflag Outlier Node Configuration**
+++++++++++++++++++++++++++++++++++++++++++++

The Multilag Outlier node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**INPUT COLUMN TO FLAG THE OUTLIER:** Select a Numeric Column in which datapoints are to be identified as outlier needs to be selected from the dropdown. 
*	**LOWER QUANTILE & UPPER QUANTILE:** Enter the values of lower and upper quantile in the respective boxes. Datapoint will be checked against these values to flag it as outlier.
*  This node can be configured to check for Outliers in multiple columns. Lower and Upper Quantile values can be set individually for each column, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/multiflag-outlier-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display the Outlier flag for the datapoint in the selected column.
   
**Multiflag Outlier Node Output**
++++++++++++++++++++++++++++++++++++++

The output of Multiflag Outlier node displays the Outlier Flag for datapoints in the selected columns. The Outlier information for each column will be displayed in separate tab, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/multiflag-outlier-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   


Graph Month Distribution
----------------------------------------

Below is a sample workflow that contains Graph Month Distribution processor in Fire Insights. It demonstrates the usage of Graph Month Distribution node to display monthly distribution of data.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays monthly distribution of data using Graph Month Distribution node. In the workflow shown below, the Graph Month Distribution node displays monthly distribution of count of trade executed.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphmthdist-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphmthdist-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Graph Month Distribution Node Configuration**
++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Graph Month Distribution node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**CHART TYPE:** Select a chart type from the dropdown based on the representation needed.
*	**Y COLUMNS:** Select string columns that represent Date Values from the list. More than one value can be selected, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphmthdist-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display monthly distribution of data present in the selected columns.

   
**Graph Month Distribution Node Output**
+++++++++++++++++++++++++++++++++++++++++++++

The output of Graph Month Distribution node displays the monthly distribution of selected columns i.e. number of trades executed, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphmthdist-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   
Graph Weekday Distribution
----------------------------------------

Below is a sample workflow that contains Graph Weekday Distribution processor in Fire Insights. It demonstrates the usage of Graph Weekday Distribution node to display weekday wise distribution of data.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays weekday wise distribution of data using Graph Weekday Distribution node. In the workflow shown below, the Graph Weekday Distribution node displays weekday wise distribution of count of trade executed.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphwkdaydist-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphwkdaydist-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Graph Weekday Distribution Node Configuration**
++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Graph Weekday Distribution node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**TITLE:** Enter a title of the output graph in the box.
*	**CHART TYPE:** Select a chart type from the dropdown based on the representation needed.
*	**Y COLUMNS:** Select string columns representing Date Values from the list, as shown below.


  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphwkdaydist-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display weekday wise distribution of data present in the selected columns.
   
**Graph Weekday Distribution Node Output**
++++++++++++++++++++++++++++++++++++++++++++++++

The output of Graph Weekday Distribution node displays the weekday wise distribution of selected columns i.e. number of trades executed, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphwkdaydist-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   

Graph Year Distribution
----------------------------------------

Below is a sample workflow that contains Graph Year Distribution processor in Fire Insights. It demonstrates the usage of Graph Year Distribution node to display yearly distribution of data.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays yearly distribution of data using Graph Year Distribution node. In the workflow shown below, the Graph Year Distribution displays yearly distribution of count of trade executed.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphyeardist-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
++++++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphyeardist-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Graph Year Distribution Node Configuration**
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Graph Year Distribution node is configured as below.

*	**INPUT:** Incoming dataset is the input for this node.
*	**TITLE:** Enter a title of the output graph in the box.
*	**CHART TYPE:** Select a chart type from the list based on the representation needed.
*	**Y COLUMNS:** Select string columns representing Date Values from the list, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphyeardist-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display yearly distribution of data present in the selected columns.
   
**Graph Year Distribution Node Output**
++++++++++++++++++++++++++++++++++++++++++++++

The output of Graph Year Distribution node displays the yearly distribution of selected columns i.e. number of trades executed, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/graphyeardist-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   
Histogram
----------------------------------------

Below is a sample workflow that contains Histogram processor in Fire Insights. It demonstrates the usage of Histogram node to display distribution of data spread across multiple bins.

It does the following processing of data:

*	Reads incoming dataset.
*	Displays distribution of data spread across multiple bins using Histogram node. In the workflow shown below, the Histogram processor displays the distribution of traded volume spread across multiple bins.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/histogram-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/histogram-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Histogram Node Configuration**
+++++++++++++++++++++++++++++++++++++++

The Histogram node is configured as follows:

*  **INPUT:** Incoming dataset is the input for this node.
*	**TITLE:** Enter a title of the output graph in the box.
*	**COLUMN NAME:** Select an Input Column from the dropdown for which distribution needs to be displayed.
*	**NUMBER OF BINS:** Enter the number of equally spaced bins that need to be created, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/histogram-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display distribution of data present in the selected column spread across multiple bins.

   
**Histogram Node Output**
++++++++++++++++++++++++++++++

The output of Histogram node displays the distribution of data present in the selected column spread across multiple bins, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/histogram-printnode-output1.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   
  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/histogram-printnode-output2.png
     :alt: dataexploration_userguide
     :width: 75%       	    

Null Values In Column
----------------------------------------

Below is a sample workflow that contains Null Values In Column processor in Fire Insights. It demonstrates the usage of Null Values In Column node identify the number of Null values and its percentage against the total data length in the selected columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Identifies number of Null values and its percentage against the total data length in the selected columns using Null Values In Column node. 

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/nullvalincol-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/nullvalincol-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Null Values In Column Node configuration**
++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Null Values In Column node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**COLUMN NAMES:** Select the columns from the list for which the null values need to be identified. Multiple columns can be selected, as shwon below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/nullvalincol-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display number of Null values and its percentage for the selected columns.

   
**Null Values In Column Node Output**
++++++++++++++++++++++++++++++++++++++++++

The output of Null Values In Column node displays the number of Null values and its percentage for the selected columns, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/nullvalincol-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   

Skewness And Kurtosis
----------------------------------------

Below is a sample workflow that contains Skewness And Kurtosis processor in Fire Insights. It demonstrates the usage of Skewness And Kurtosis node to identify Skewness (measure of symmetry) and Kurtosis (measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution) in the selected columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Identifies Skewness and Kurtosis in the selected columns using Skewness And Kurtosis node. 

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/skewness-wf.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/skewness-input.png
     :alt: dataexploration_userguide
     :width: 75%

**Skewness And Kurtosis Node Configuration**
++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Skewness And Kurtosis node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**COLUMN NAMES:** Select the columns from the list for which Skewness And Kurtosis need to be computed. Multiple columns can be selected, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/skewness-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display Skewness And Kurtosis values for the selected columns.

   
**Skewness And Kurtosis Node Output**
++++++++++++++++++++++++++++++++++++++++++++

The output of Skewness And Kurtosis node displays the Skewness And Kurtosis values for the selected columns, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/skewness-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   

Summary Statistics
----------------------------------------

Below is a sample workflow that contains Summary Statistics processor in Fire Insights. It demonstrates the usage of Summary Statistics node to compute Statistical Summary such as count, mean, min, max, etc. for the selected columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Computes Statistical Summary such as count, mean, min, max, etc. for the selected columns using Summary Statistics node. 

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/summarystats-workflow.png
     :alt: dataexploration_userguide
     :width: 60%
   
**Incoming Dataset**
+++++++++++++++++++++++++++++

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/summarystats-incoming-dataset.png
     :alt: dataexploration_userguide
     :width: 75%

**Summary Statistics Node Configuration**
++++++++++++++++++++++++++++++++++++++++++++++++++++

The Summary Statistics node is configured as follows:

*	**INPUT:** Incoming dataset is the input for this node.
*	**TITLE:** Enter a title of the output.
*	**COLUMN NAMES:** Select the columns from the list for which summary need to be computed. Multiple columns can be selected, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/summarystats-config.png
     :alt: dataexploration_userguide
     :width: 75%

*	Output of this node will display Statistical Summary of the columns selected.
   
**Summary Statistics Node Output**
++++++++++++++++++++++++++++++++++++++++

The output of Summary Statistics node displays the Statistical Summary of the columns selected, as shown below.

  .. figure:: ../../_assets/user-guide/data-exploration/data-exploration/summarystats-printnode-output.png
     :alt: dataexploration_userguide
     :width: 75%       	    
   
