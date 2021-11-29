String
==========

Fire Insights provide processors for performing String functions on a row or text.


String Processors in Fire Insights
----------------------------------------


.. list-table:: String Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - String Functions
     - This node performs a specified String function on a row
   * - String Functions Multiple
     - This node creates a new Dataframe by transforming data of multiple columns using specified string functions.
   * - Text Case Transformer
     - This node converts text to upper or lower case

String Functions
----------------------------------------

Below is a sample workflow which contains ``String Functions`` processor in Fire Insights. It demonstrates usage of String Functions node to transform String value using various String Functions.

It does following processing of data:

*	Reads incoming Dataset
*	Transforms String column data (Location and Dept) using String Functions node to change case to lower
* 	Transformed data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfunctions-demo-workflow.png
   :alt: string_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfunctions-incoming-dataset.png
   :alt: string_userguide
   :width: 90%


**String Functions Node configuration**

Input Columns are selected as below to perform transformation on.

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfunctions-inputcol-selection.png
   :alt: string_userguide
   :width: 90%

String function selection to transform data to lower case is done as below

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfunctions-function-definition.png
   :alt: string_userguide
   :width: 90%

**String Functions Node output**

Output of Print node displaying transformed data in lower case using String Functions node

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfunctions-printnode-output.png
   :alt: string_userguide
   :width: 90%
   
String Functions Multiple
----------------------------------------

Below is a sample workflow which contains ``String Functions Multiple`` processor in Fire Insights. It demonstrates usage of String Functions Multiple node to transform multiple String columns data in one go using various String Functions.

It does following processing of data:

*	Reads incoming Dataset
*	It removes white spaces from Location data and transforms Department values to lower case using String Functions Multiple node
* 	Transformed data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfnmulti-demo-workflow.png
   :alt: string_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfnmulti-incoming-dataset.png
   :alt: string_userguide
   :width: 90%


**String Functions Multiple Node configuration**

String Functions Multiple node is configured as below to remove white spaces from Location data and to transform Department values to lower case.

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfnmulti-configuration.png
   :alt: string_userguide
   :width: 90%

**String Functions Multiple Node output**

Output of Print node displaying transformed data using String Functions Multiple node

.. figure:: ../../_assets/user-guide/data-preparation/string/stringfnmulti-printnode-output.png
   :alt: string_userguide
   :width: 90%
   
Text Case Transformer
----------------------------------------

Below is a sample workflow which contains ``Text Case Transformer`` processor in Fire Insights. It demonstrates usage of Text Case Transformer node to change case of a String column data to either Upper case or Lower case.

It does following processing of data:

*	Reads incoming Dataset
*	It changes case of Location data to lower case and append it as a new column to the output dataset
* 	Transformed data is printed using Print node

.. figure:: ../../_assets/user-guide/data-preparation/string/casetrans-demo-workflow.png
   :alt: string_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/string/casetrans-incoming-dataset.png
   :alt: string_userguide
   :width: 90%


**Text Case Transformer Node configuration**

Text Case Transformer node is configured as below to transform Location values to lower case and append it as new output column.

.. figure:: ../../_assets/user-guide/data-preparation/string/casetrans-configuration.png
   :alt: string_userguide
   :width: 90%

**Text Case Transformer Node output**

Output of Print node displaying transformed data using Text Case Transformer node

.. figure:: ../../_assets/user-guide/data-preparation/string/casetrans-printnode-output.png
   :alt: string_userguide
   :width: 90%
