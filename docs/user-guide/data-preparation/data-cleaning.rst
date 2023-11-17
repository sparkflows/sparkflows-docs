Data Cleaning
==========

Fire Insights provides powerful capabilities for data cleanup.


Data Cleaning Processors in Fire Insights
----------------------------------------


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Data Cleansing
     - This node cleans incoming dataset by removing null rows, columns, by replacing missing values and by changing cases of the string data.
   * - Drop Rows With Null
     - This node creates a new DataFrame by dropping rows that contain null values.
   * - Find And Replace Using Regex
     - This node finds and replaces text in a column containing a string.
   * - Find And Replace Using Regex Advanced
     - This node finds and replaces text in a column containing a string.
   * - Dedup
     - This node is used for problems like entity resolution or data matching. Entity resolution or data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources.
   * - Drop Duplicate Rows
     - Returns a new dataset that contains the unique rows from this Dataset. When user selects columns in the node, it returns a new Dataset after removing the duplicate rows, considering uniques in the subset of column selected by user
   * - Remove Duplicate Rows
     - This node takes an array of fields and compares rows in those fields. If they match fully, then it considers it a match. From the matches, it would randomly take one row and drop the rest.
   * - Remove Unwanted Characters
     - This node removes unwanted characters.
   * - Remove Unwanted Characters Advanced
     - This node removes unwanted characters from multiple columns.
 

Data Cleansing
----------------------------------------

Below is a sample workflow which contains Data Cleansing processor in Fire Insights. It demonstrates the usage of Data Cleansing node to clean incoming dataset by removing rows/columns having null values, by replacing missing values with space or 0 for String and Integer data respectively, by removing unwanted characters, and by changing case of the incoming data.

It does the following processing of data:

*	Reads incoming dataset.
*	Changes String values to Title case, removes blank spaces from data, and replaces Null values in columns with Spaces or 0. 
* 	Output data is printed using the Print node.

**Data Cleansing Node Sample Workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/data-cleansing-wf.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/datacleansing-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 75%

**Data Cleansing Node configuration**

Data Cleansing node is configured as below.

*	Input of this node is the incoming dataset.
*	Output of this node would contain modified data as per the configuration.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/datacleansing-config.png
   :alt: datacleaning_userguide
   :width: 75%

*	**Select Columns** - Select the list of columns on which the data cleansing rules would be applicable to.
*  **Remove Null Rows** - This option would remove all rows from the dataset having null values in any of the columns.
*  **Remove Null Columns** - This option would remove columns from the dataset having null values.
*  **Replace With Blanks (String Fields)** - This option would replace missing or null values with blanks in the select String columns.
*  **Replace With 0 (Numeric Fields)** - This option would replace missing or null values with 0 in the select Numeric columns.
*  **All Whitespaces/Letters/Numbers/Punctuation** - Occurrences of the values as per the selected option would be removed from the selected columns.
*  **Modify Case** - Case of data in the selected columns would be changed as the option selected. Available options are Upper Case, Lower Case, Title Case and Default.


**Data Cleansing Node output**

Output of Data Cleansing node which displays modified values is shown below:

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/datacleansing-printnode-output.png
   :alt: datacleaning_userguide
   :width: 75% 



Drop Rows With Null
----------------------------------------

Below is a sample workflow which contains Drop Rows With Null processor in Fire Insights. It demonstrates the usage of Drop Rows With Null node to remove rows having null value in columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Remove rows from incoming dataset having Null value in columns using Drop Rows With Null processor. 
* 	Output data is printed using the Print node.

**Drop Rows with Null Node Sample workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropNullWF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/InputData.png
   :alt: datacleaning_userguide
   :width: 75%

**Drop Rows With Null Node configuration**

Drop Rows With Null node is configured as below.

*	Input of this node is the incoming dataset.
*	Output of this node would contain rows that don't have null values in columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropNUllConfig.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Drop Rows With Null Node output**

Output of Drop Rows With Null node which displays rows that don't have null values is shown below:

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropNullOutput.png
   :alt: datacleaning_userguide
   :width: 75% 
   
   
Find And Replace Using Regex
----------------------------------------

Below is a sample workflow which contains the Find And Replace Using Regex processor in Fire Insights. It demonstrates the usage of Find And Replace Using Regex node to replace a string pattern with another by the use of a Regex Expression.

It processes the dataset in the following ways:

*	Reads incoming dataset.
*	Replaces a string pattern with another by the use of Find And Replace Using Regex node. In the sample workflow shown below, date separator is replced from '-' to '/'. 
* 	Output data is printed by the use of the Print node.

**Find and Replace Using Regex Node Sample workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindWF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindInputData.png
   :alt: datacleaning_userguide
   :width: 75%

**Find And Replace Using Regex Node configuration**

Find And Replace Using Regex node is configured as below.

*	Input of this node is the incoming dataset.
*	Columns in which data needs to be replaced is selected as ``Input Columns``. More than one column can be selected.
*	String Pattern that needs to be searched is to be entered in ``Find`` box.
*	String Pattern that replaces matched values in the output is to be entered in ``Replace`` box.
*	Output of this node would contain replaced values for the matches found.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindConfig1.png
   :alt: datacleaning_userguide
   :width: 75%
   
.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindConfig2.png
   :alt: datacleaning_userguide
   :width: 75%   
   
**Find And Replace Using Regex Node output**

Output of Find And Replace Using Regex node displaying values replaced for the matches found is shown below. In the sample workflow shown above, Date Separator in Date Of Joining has been changed from '-' to '/'.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindOutput.png
   :alt: datacleaning_userguide
   :width: 75%    
   
Find And Replace Using Regex Advanced
----------------------------------------

Below is a sample workflow which contains Find And Replace Using Regex Advanced processor in Fire Insights. It demonstrates the usage of Find And Replace Using Regex Advanced node to replace a string pattern with another using Regex Expression. This node facilitates multiple transformations in one go.

It does the following processing of data:

*	Reads incoming Dataset.
*	Replaces a string pattern with another using Find And Replace Using Regex Advanced node. In the sample workflow shown below, date separator is replced from '-' to '.' in Date Of Joining column and replaced HR with Human Resource in DEPT column. 
* 	Output data after replacement is printed using the Print node.

**Find and Replace Using Regex Advanced Node Sample workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/Find-Advanced-WF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindInputData.png
   :alt: datacleaning_userguide
   :width: 75%

**Find And Replace Using Regex Advanced Node configuration**

Find And Replace Using Regex Multiple node is configured as below.

*	Input of this node is the incoming dataset.
*	In the ``Variables List``, Column in which data needs to be replaced is to be selected as ``Input Columns``. 
*	String Pattern that needs to be searched is to be entered in ``Find`` box.
*	String Pattern that replaces matched values in the output is to be entered in ``Replace`` box.
*	Multiple transformation for different columns can be entered as separate rows.
*	Output of this node would contain replaced values for the matches found.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindAdvancedConfig.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Find And Replace Using Regex Advanced Node output**

Output of Find And Replace Using Regex Advanced node displaying values replaced for the matches found.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/FindAdvancedOutput.png
   :alt: datacleaning_userguide
   :width: 75%       
   
Dedup
----------------------------------------

Below is a sample workflow which contains Dedup processor in Fire Insights. It demonstrates  the usage of Dedup node to compare data of an entity from multiple sources to identify whether they are same or not.

It does following processing of data:

*	Reads incoming Base Dataset and Dedup Dataset.
*	Joins Base and Dedup datasets into single dataset to facilitate comparison using ``Join Using SQL`` node.
*	Base and Dedup datasets are compared using ``Dedup`` node. ``ConfidenceScore`` is calculated as a result of comparison which indicates extent to which both datasets match.
* 	Output data listing ``Confidence Score`` is printed using  the Print node.

**Dedup Node Sample Workflow**


.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup_WF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming datasets**

*	Base Dataset against which other dataset is compared for accuracy.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup_data1.png
   :alt: datacleaning_userguide
   :width: 75%
   
*	Dedup Dataset which needs to be checked for accuracy.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup_data2.png
   :alt: datacleaning_userguide
   :width: 75%

**Dedup Node configuration**

Dedup node is configured as below.

*	Input of this node are the incoming datasets.
*	Column name that lists ``ConfidenceScore`` in the output needs to be entered in the ``ConfidenceScore`` box.
*	Columns that are used for comparison need to be selected as ``LHS Variables`` and ``RHS Variables`` respectively. 
*	Algorithm to be used for comparison needs to be selected in ``Algorithm To Use`` drop down.
*	Weightage of each column that contributes to final ConfidenceScore calculation needs to be entered in ``Weights`` box.
*	Column name displaying the result of each column comaprison needs to be entered in ``Output Column`` box.
*	Output of this node would contain final ConfidenceScore computed.


.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup_config.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Dedup Node output**

Output of Dedup node displaying Confidence Score value is shown as below:

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup_output.png
   :alt: datacleaning_userguide
   :width: 75%       
   
Drop Duplicate Rows
----------------------------------------

Below is a sample workflow which contains Drop Duplicate Rows processor in Fire Insights. It demonstrates the usage of Drop Duplicate Rows node to drop duplicate rows having same values in the selected columns.

It does the following processing of data:

*	Reads incoming Dataset.
*	Drops duplicate rows from incoming dataset having same values in the selected columns using Drop Duplicate Rows node.
* 	Output data containing only unique rows is printed using the Print node.

**Drop Duplicate Rows Workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropDuplicateWF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropDuplicateInput.png
   :alt: datacleaning_userguide
   :width: 75%

**Drop Duplicate Rows Node configuration**

Drop Duplicate Rows node is configured as below.

*	Input of this node is the incoming dataset.
*	Columns in which data needs to be checked for duplicate values is to be selected in ``Columns``. More than one column can be selected.
*	Output of this node would contain unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropDuplicateConfig.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Drop Duplicate Rows Node output**

Output of Drop Duplicate Rows node displaying rows having unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropDuplicateOutput.png
   :alt: datacleaning_userguide
   :width: 75%       
   
Remove Duplicate Rows
----------------------------------------

Below is a sample workflow which contains Remove Duplicate Rows processor in Fire Insights. It demonstrates usage of Remove Duplicate Rows node to remove duplicate rows having same data in the selected columns and retain one rows as per the selection.

It does the following processing of data:

*	Reads incoming Dataset.
*	Removes duplicate rows from incoming dataset having same values in the selected columns using Remove Duplicate Rows node. It retains one of the duplicate rows in the output either first or last based on the selection.
* 	Output data containing only unique rows is printed using the Print node.

**Remove Duplicate Rows Node Sample workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveDuplicateWF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/DropDuplicateInput.png
   :alt: datacleaning_userguide
   :width: 75%

**Remove Duplicate Rows Node configuration**

Remove Duplicate Rows node is configured as below.

*	Input of this node is the incoming dataset.
*	A Row from the duplicate set of rows, that needs to be retained in the output, is to be selected in ``Order`` dropdown. It allows to select either ``first`` or ``last``.
*	Columns in which data needs to be checked for duplicate values is to be selected in ``Columns``. More than one column can be selected.
*	Output of this node would contain unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveDuplicateConfig.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Remove Duplicate Rows Node output**

Output of Remove Duplicate Rows node displaying rows having unique combination of values in the selected Columns is shown below:

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveDuplicateOutput.png
   :alt: datacleaning_userguide
   :width: 75%       
   
Remove Unwanted Characters
----------------------------------------

Below is a sample workflow which contains Remove Unwanted Characters processor in Fire Insights. It demonstrates the usage of Remove Unwanted Characters node to remove White Spaces, Letters, Digits, Signs and Commas from the selected columns.

It does the following processing of data:

*	Reads incoming Dataset.
*	Removes White Spaces, Letters, Digits, Signs and Commas from the selected columns using Remove Unwanted Characters node. 
* 	Output data containing transformed data is printed using the Print node.

**Remove Unwanted Characters Sample workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveUnwantedWF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveUnwantedInput.png
   :alt: datacleaning_userguide
   :width: 75%

**Remove Unwanted Characters Node configuration**

Remove Unwanted Characters node is configured as below.

*	Input of this node is the incoming dataset.
*	Columns from which unwanted characters need to be removed are to be selected in ``Input Columns`` list.
*	Based on the requirement of character removal, White Spaces, Letters, Digits, Signs and Commas dropdown need to be selected as ``True``.
*	Output of this node would contain transformed data based on the selection.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveUnwantedConfig1.png
   :alt: datacleaning_userguide
   :width: 75%
   
.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveUnwantedConfig2.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Remove Unwanted Characters Node output**

Output of Remove Unwanted Characters node displaying transformed data after removal of selected characters from selected columns is shown below:

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveUnwantedOutput.png
   :alt: datacleaning_userguide
   :width: 75%       
   
Remove Unwanted Characters Advanced
----------------------------------------

Below is a sample workflow which contains Remove Unwanted Characters Advanced processor in Fire Insights. It demonstrates  the usage of Remove Unwanted Characters Advanced node to remove White Spaces, Letters, Digits, Signs and Commas from the selected columns. This node can be configured to remove different set of characters for different columns in one go.

It does the following processing of data:

*	Reads incoming dataset.
*	Removes White Spaces, Letters, Digits, Signs and Commas from the selected columns using Remove Unwanted Characters Advanced node. Different columns are configured to remove different set of characters.
* 	Output data containing transformed data is printed using the Print node.

**Remove Unwanted Characters Advanced Sample workflow**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/UnwantedAdvWF.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/RemoveUnwantedInput.png
   :alt: datacleaning_userguide
   :width: 75%

**Remove Unwanted Characters Advanced Node configuration**

Remove Unwanted Characters Advanced node is configured as below.

*	Input of this node is the incoming dataset.
*	In the ``Variables List``, columns from which unwanted characters need to be removed are to be selected in ``Input Columns`` list.
*	Based on the requirement of character removal, White Spaces, Letters, Digits, Signs and Commas dropdown need to be selected as ``True``.
*	Multiple transformations for different columns can be added as separate rows.
*	Output of this node would contain transformed data based on the selection.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/UnwantedAdvConfig.png
   :alt: datacleaning_userguide
   :width: 75%
   
**Remove Unwanted Characters Advanced Node output**

Output of Remove Unwanted Characters Advanced node displaying transformed data after removal of selected characters from selected columns is shown below:

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/UnwantedAdvOutput.png
   :alt: datacleaning_userguide
   :width: 75%       
