Data Cleaning
==========

Fire Insights provide powerful capabilities for data cleanup.


Data Cleaning Processors in Fire Insights
----------------------------------------


.. list-table:: Data Cleaning Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Drop Rows With Null
     - This node creates a new DataFrame by dropping rows containing null values
   * - Find And Replace Using Regex
     - This node finds and replaces text in a column containing a string
   * - Find And Replace Using Regex Multiple
     - This node finds and replaces text in a column containing a string
   * - Dedup
     - This node is used for problems like entity resolution or data matching. Entity resolution or Data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources
   * - Drop Duplicate Rows
     - When the user doesn't select any column, returns a new dataset that contains only the unique rows from this Dataset. Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
   * - Remove Duplicate Rows
     - This node takes an array of fields, compares rows in those fields. If they full match, then it's a match. From the matches, it would randomly take one row and drop the rest.
   * - Remove Unwanted Characters
     - This node removes unwanted characters
   * - Remove Unwanted Characters Multiple
     - This node removes unwanted characters multiple columns
 

Drop Rows With Null
----------------------------------------

Below is a sample workflow which contains ``Drop Rows With Null`` processor in Fire Insights. It demonstrates usage of ``Drop Rows With Null`` node to remove rows having null value in columns.

It does following processing of data:

*	Reads incoming Dataset
*	Remove rows from incoming dataset having Null value in columns using ``Drop Rows With Null`` processor. 
* 	Output data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/droprowsnull-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/droprowsnull-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Drop Rows With Null Node configuration**

*	``Drop Rows With Null`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Output of this node would contain rows that don't have null values in columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/droprowsnull-config.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Drop Rows With Null Node output**

Output of ``Drop Rows With Null`` node displaying rows that don't have null values.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/droprowsnull-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90% 
   
   
Find And Replace Using Regex
----------------------------------------

Below is a sample workflow which contains ``Find And Replace Using Regex`` processor in Fire Insights. It demonstrates usage of ``Find And Replace Using Regex`` node to replace a string pattern with another using Regex Expression.

It does following processing of data:

*	Reads incoming Dataset
*	Replaces a string pattern with another using ``Find And Replace Using Regex`` node. In this workflows date separator is replced from '-' to '\/' 
* 	Output data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregex-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregex-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Find And Replace Using Regex Node configuration**

*	``Find And Replace Using Regex`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Columns in which data needs to be replaced is selected as ``Input Columns``. More than one column can be selected.
*	String Pattern that needs to be searched is to be entered in ``Find`` box.
*	String Pattern that replaces matched values in the output is to be entered in ``Replace`` box.
*	Output of this node would contain replaced values for the matches found.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregex-config1.png
   :alt: datacleaning_userguide
   :width: 90%
   
.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregex-config2.png
   :alt: datacleaning_userguide
   :width: 90%   
   
**Find And Replace Using Regex Node output**

Output of ``Find And Replace Using Regex`` node displaying values replaced for the matches found. In this example Date Separator in ``Date Of Joining`` has been changed from '-' to '\/'

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregex-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%    
   
Find And Replace Using Regex Multiple
----------------------------------------

Below is a sample workflow which contains ``Find And Replace Using Regex Multiple`` processor in Fire Insights. It demonstrates usage of ``Find And Replace Using Regex Multiple`` node to replace a string pattern with another using Regex Expression. This node facilitates multiple transformations in one go.

It does following processing of data:

*	Reads incoming Dataset
*	Replaces a string pattern with another using ``Find And Replace Using Regex Multiple`` node. In this workflows date separator is replced from '-' to '\/' in ``Date Of Joining``, spaces in ``Salary`` is replaced with a comma, 'BAD' in ``Performance`` is replaced with 'NOT SO GOOD'.  
* 	Output data after replacement is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregexmulti-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregexmulti-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Find And Replace Using Regex Multiple Node configuration**

*	``Find And Replace Using Regex Multiple`` node is configured as below.
*	Input of this node is the incoming dataset.
*	In the ``Variables List``, Column in which data needs to be replaced is to be selected as ``Input Columns``. 
*	String Pattern that needs to be searched is to be entered in ``Find`` box.
*	String Pattern that replaces matched values in the output is to be entered in ``Replace`` box.
*	Multiple transformation for different columns can be entered as a separate rows.
*	Output of this node would contain replaced values for the matches found.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregexmulti-config.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Find And Replace Using Regex Multiple Node output**

Output of ``Find And Replace Using Regex Multiple`` node displaying values replaced for the matches found.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/fnrregexmulti-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%       
   
Dedup
----------------------------------------

Below is a sample workflow which contains ``Dedup`` processor in Fire Insights. It demonstrates usage of ``Dedup`` node to compare data of an entity from multiple sources to identify whether they are same or not.

It does following processing of data:

*	Reads incoming Base Dataset and Dedup Dataset
*	Joins Base and Dedup datasets into single dataset to facilitate comparison using ``Join Using SQL`` node.
*	Base and Dedup datasets are compared using ``Dedup`` node. ``Confidence Score`` is calculated as a result of comparison which indicates extent to which both datasets match.
* 	Output data listing ``Confidence Score`` is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming datasets**

*	Base Dataset against which other dataset is compared for accuracy.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup-incoming-dataset1.png
   :alt: datacleaning_userguide
   :width: 90%
   
*	Dedup Dataset which needs to be checked for accuracy.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup-incoming-dataset2.png
   :alt: datacleaning_userguide
   :width: 90%

**Dedup Node configuration**

*	``Dedup`` node is configured as below.
*	Input of this node are the incoming datasets.
*	Column name that lists ``Confidence Score`` in the output needs to be entered in the ``Confidence Score`` box.
*	Columns that are used for comparison need to be selected as ``LHS Variables`` and ``RHS Variables`` respectively. 
*	Algorithm to be used for comparison needs to be selected in ``Algorithm To Use`` drop down.
*	Weightage of each column that contributes to final Confidence Score calculation needs to be entered in ``Weights`` box.
*	Column name displaying result of each column comaprison needs to be entered in ``Output Column`` box.
*	Output of this node would contain final Confidence Score computed.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup-config.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Dedup Node output**

Output of ``Dedup`` node displaying Confidence Score value.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dedup-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%       
   
Drop Duplicate Rows
----------------------------------------

Below is a sample workflow which contains ``Drop Duplicate Rows`` processor in Fire Insights. It demonstrates usage of ``Drop Duplicate Rows`` node to drop duplicate rows having same values in the selected columns.

It does following processing of data:

*	Reads incoming Dataset
*	Drops duplicate rows from incoming dataset having same values in the selected columns using ``Drop Duplicate Rows`` node.
* 	Output data containing only unique rows is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dropduprows-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dropduprows-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Drop Duplicate Rows Node configuration**

*	``Drop Duplicate Rows`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Columns in which data needs to be checked for duplicate values is to be selected in ``Columns``. More than one column can be selected.
*	Output of this node would contain unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dropduprows-config.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Drop Duplicate Rows Node output**

Output of ``Drop Duplicate Rows`` node displaying rows having unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/dropduprows-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%       
   
Remove Duplicate Rows
----------------------------------------

Below is a sample workflow which contains ``Remove Duplicate Rows`` processor in Fire Insights. It demonstrates usage of ``Remove Duplicate Rows`` node to remove duplicate rows having same data in the selected columns and retain one rows as per the selection.

It does following processing of data:

*	Reads incoming Dataset
*	Removes duplicate rows from incoming dataset having same values in the selected columns using ``Remove Duplicate Rows`` node. It retains one of the duplicate rows in the output either first or last based on the selection.
* 	Output data containing only unique rows is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remduprows-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remduprows-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Remove Duplicate Rows Node configuration**

*	``Remove Duplicate Rows`` node is configured as below.
*	Input of this node is the incoming dataset.
*	A Row from the duplicate set of rows that needs to be retained in the output is to be selected in ``Order`` dropdown. It allows to select either ``first`` or ``last``.
*	Columns in which data needs to be checked for duplicate values is to be selected in ``Columns``. More than one column can be selected.
*	Output of this node would contain unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remduprows-config.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Remove Duplicate Rows Node output**

Output of ``Remove Duplicate Rows`` node displaying rows having unique combination of values in the selected Columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remduprows-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%       
   
Remove Unwanted Characters
----------------------------------------

Below is a sample workflow which contains ``Remove Unwanted Characters`` processor in Fire Insights. It demonstrates usage of ``Remove Unwanted Characters`` node to remove White Spaces, Letters, Digits, Signs and Commas from the selected columns.

It does following processing of data:

*	Reads incoming Dataset
*	Removes White Spaces, Letters, Digits, Signs and Commas from the selected columns using ``Remove Unwanted Characters`` node. 
* 	Output data containing transformed data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchr-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchr-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Remove Unwanted Characters Node configuration**

*	``Remove Unwanted Characters`` node is configured as below.
*	Input of this node is the incoming dataset.
*	Columns from which unwanted characters need to be removed are to be selected in ``Input Columns`` list.
*	Based on the requirement of character removal, White Spaces, Letters, Digits, Signs and Commas dropdown need to be selected as ``True``.
*	Output of this node would contain transformed data based on the selection.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchr-config1.png
   :alt: datacleaning_userguide
   :width: 90%
   
.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchr-config2.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Remove Unwanted Characters Node output**

Output of ``Remove Unwanted Characters`` node displaying transformed data after removal of selected characters from selected columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchr-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%       
   
Remove Unwanted Characters Multiple
----------------------------------------

Below is a sample workflow which contains ``Remove Unwanted Characters Multiple`` processor in Fire Insights. It demonstrates usage of ``Remove Unwanted Characters Multiple`` node to remove White Spaces, Letters, Digits, Signs and Commas from the selected columns. This node can be configured to remove different set of characters for different columns in one go.

It does following processing of data:

*	Reads incoming Dataset
*	Removes White Spaces, Letters, Digits, Signs and Commas from the selected columns using ``Remove Unwanted Characters Multiple`` node. Different columns are configured to remove different set of characters.
* 	Output data containing transformed data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchrmul-workflow.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchrmul-incoming-dataset.png
   :alt: datacleaning_userguide
   :width: 90%

**Remove Unwanted Characters Multiple Node configuration**

*	``Remove Unwanted Characters Multiple`` node is configured as below.
*	Input of this node is the incoming dataset.
*	In the ``Variables List``, columns from which unwanted characters need to be removed are to be selected in ``Input Columns`` list.
*	Based on the requirement of character removal White Spaces, Letters, Digits, Signs and Commas dropdown need to be selected as ``True``.
*	Multiple transformations for different columns can be added as separate rows.
*	Output of this node would contain transformed data based on the selection.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchrmul-config.png
   :alt: datacleaning_userguide
   :width: 90%
   
**Remove Unwanted Characters Multiple Node output**

Output of ``Remove Unwanted Characters Multiple`` node displaying transformed data after removal of selected characters from selected columns.

.. figure:: ../../_assets/user-guide/data-preparation/datacleaning/remunwantedchrmul-printnode-output.png
   :alt: datacleaning_userguide
   :width: 90%       
