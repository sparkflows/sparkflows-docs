Imputing
==========

Fire Insights provides various processors for Imputing data.


Imputing Processors in Fire Insights
----------------------------------------


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Impute Advanced
     - It imputes missing value as per strategy defined for the selected columns. A particular data in the dataset can be replaced with Mean, Median or Mode value. It can also be configured to replace missing values with a constant. Strategy can be defined for multiple columns in single go.
   * - Imputing With Constant
     - It imputes missing value with a constant value. It fills missing values (None) in selected columns with a given constant value for the corresponding column, in the incoming        DataFrame.
   * - Imputing With Mean Value
     - Imputing the missing values by column mean.
   * - Imputing With Median
     - Imputing with missing value with median value. It fills missing values (None) in selected columns with a median value in the corresponding column, in the incoming                 DataFrame.
   * - Imputing With Mode Value
     - Imputing with the most frequently observed value. It fills missing values (None) in selected columns with the most frequently observed value in the corresponding column, in       the incoming DataFrame.

 
Impute Advanced
----------------------------------------

Below is a sample workflow which contains Impute Advanced processor in Fire Insights. It demonstrates the usage of Impute Advanced node to replace missing values with constant values as per strategy defined for the selected columns. A particular data in the dataset can be replaced with Mean, Median or Mode value. It can also be configured to replace missing values with a constant. Strategy can be defined for multiple columns in single go.

It does the following processing of data:

*	Reads incoming dataset.
*  Replaces a value in the incoming dataset with mean value.
*	Replaces missing values with constant values using Impute Advanced node.
*	Prints output dataset containing replaced values using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/imputeadv-workflow.png
   :alt: imputing_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/imputing/imputeadv-incoming-dataset.png
   :alt: imputing_userguide
   :width: 75%

**Impute Advanced Node Configuration**

Impute Advanced node is configured as below.

*	Input of this node is the incoming dataset.
*	Each row in the ``Variables List`` specifies imputing details for each columns.
*	Column in which missing values need to be replaced with Constant value or a particular value to be replaced with either Mean/Median/Mode value is to be selected in ``Columns`` list.
*  ``Impute Strategy`` needs to be selected. It can have either Constant/Mean/Median/Mode value.
*  Enter a value in ``Replace Value`` box. If Strategy has been selected as Mean/Median/Mode then entered value in the column would be replaced as per the selected Strategy. 
*	Constant value that needs to be used to replace missing value is to be entered in ``Constants`` box. It would be used if Strategy has been selected as ``Constant``.
*	Additional rows need to be added for each imputing requirement.
*	Output of this node would display transformed values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/imputeadv-config.png
   :alt: imputing_userguide
   :width: 75%
   
**Impute Advanced Node Output**

Output of Impute Advanced node displaying transformed values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/imputeadv-printnode-output.png
   :alt: imputing_userguide
   :width: 75%       	    

 
Imputing With Constant
----------------------------------------

Below is a sample workflow which contains Imputing With Constant processor in Fire Insights. It demonstrates the usage of Imputing With Constant node to replace missing values with constant values.

It does the following processing of data:

*	Reads incoming dataset.
*	Replaces missing values with constant values using Imputing With Constant node.
*	Prints output dataset containing replaced values using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-constant-wf.png
   :alt: imputing_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-constant-input.png
   :alt: imputing_userguide
   :width: 75%

**Imputing With Constant Node Configuration**

Imputing With Constant node is configured as below.

*	Input of this node is the incoming dataset.
*	Each row in the ``Variables List`` specifies imputing details for each columns.
*	Column in which missing values need to be replaced with Constant value is to be selected in ``Columns`` list.
*	Constant value that needs to be used to replace missing value is to be entered in ``Constants`` box.
*	Additional rows need to be added for each imputing requirement.
*	Output of this node would display misssing values replaced with Constant values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-constant-config.png
   :alt: imputing_userguide
   :width: 75%
   
**Imputing With Constant Node Output**

Output of Imputing With Constant node displaying misssing values replaced with Constant values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-constant-output.png
   :alt: imputing_userguide
   :width: 75%       	    


Imputing With Mean Value
----------------------------------------

Below is a sample workflow which contains Imputing With Mean Value processor in Fire Insights. It demonstrates the usage of Imputing With Mean Value node to replace missing values with Mean value of the column.

It does the following processing of data:

*	Reads incoming dataset.
*	Replace missing values with Mean value of the column using Imputing With Mean Value node.
*	Prints output dataset containing missing values replaced with Mean values using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mean-wf.png
   :alt: imputing_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mean-input.png
   :alt: imputing_userguide
   :width: 75%

**Imputing With Mean Value Node Configuration**

Imputing With Mean Value node is configured as below.

*	Input of this node is the incoming dataset.
*	Numeric columns in which missing values are to be replaced with Mean values need to be selected in ``Column Names`` list.
*	Multiple numeric columns can be selected.
*	Output of this node would display dataset containing missing values replaced with Mean values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mean-config.png
   :alt: imputing_userguide
   :width: 75%
   
**Imputing With Mean Value Node Output**

Output of Imputing With Mean Value node displaying missing values replaced with Mean values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mean-output.png
   :alt: imputing_userguide
   :width: 75%       	    
   
Imputing With Median
----------------------------------------

Below is a sample workflow which contains Imputing With Median processor in Fire Insights. It demonstrates the usage of Imputing With Median node to replace missing values with Meadian value.

It does the following processing of data:

*	Reads incoming dataset.
*	Replaces missing values with Median value using Imputing With Median node.
*	Prints output dataset containing missing values replaced with Median values using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-median-wf.png
   :alt: imputing_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mean-input.png
   :alt: imputing_userguide
   :width: 75%

**Imputing With Median Node Configuration**

Imputing With Median node is configured as below.

*	Input of this node is the incoming dataset.
*	Numeric columns in which missing values are to be replaced with Median values need to be selected in ``Column Names`` list.
*	Multiple numeric columns can be selected.
*	Output of this node would display dataset containing missing values replaced with Median values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-median-config.png
   :alt: imputing_userguide
   :width: 75%
   
**Imputing With Median Node Output**

Output of Imputing With Median node displaying missing values replaced with Median values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-median-output.png
   :alt: imputing_userguide
   :width: 75%       	    
   
Imputing With Mode Value
----------------------------------------

Below is a sample workflow which contains Imputing With Mode Value processor in Fire Insights. It demonstrates the usage of Imputing With Mode Value node to replace missing values with Mode value.

It does the following processing of data:

*	Reads incoming dataset.
*	Replaces missing values with Mode value using Imputing With Mode Value node.
*	Prints output dataset containing missing values replaced with Mode values using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mode-wf.png
   :alt: imputing_userguide
   :width: 75%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-constant-input.png
   :alt: imputing_userguide
   :width: 75%

**Imputing With Mode Value Node Configuration**

Imputing With Mode Value node is configured as below.

*	Input of this node is the incoming dataset.
*	Columns in which missing values are to be replaced with Mode values need to be selected in ``Columns`` list.
*	Multiple columns can be selected.
*	Output of this node would display dataset containing missing values replaced with Mode values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mode-config.png
   :alt: imputing_userguide
   :width: 75%
   
**Imputing With Mode Value Node Output**

Output of Imputing With Mode Value node displaying missing values replaced with Mode values.

.. figure:: ../../_assets/user-guide/data-preparation/imputing/impute-mode-output.png
   :alt: imputing_userguide
   :width: 75%       	    
