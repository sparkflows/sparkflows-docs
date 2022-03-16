Data Validation
==========

Fire Insights provide processors for Data Validation


Data Validation Processors in Fire Insights
----------------------------------------


.. list-table:: Data Validation Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Compare Datasets
     - It compares incoming datasets and creates 3 output datasets - Present in 1st but not in 2nd, present in 2nd but not in 1st and Common rows in both.
   * - Node Schema Validation
     - It validates incoming dataset schema against defined schema validation rules. It also imputes missing values as per rules definition.
   * - Validate Address
     - It validates address data value against a valid address format. Some of the valid address formats are '123 xyx avenue' and '1/1 block-D street'

	 
Compare Datasets
----------------------------------------

Below is a sample workflow which contains ``Compare Datasets`` processor in Fire Insights. It demonstrates usage of ``Compare Datasets`` node to compare incoming datasets and create 3 output datasets - Present in 1st but not in 2nd, present in 2nd but not in 1st and Common rows in both.

It does following processing of data:

*	Reads incoming Datasets.
*	Compares incoming datasets and create 3 output datasets using ``Compare Datasets`` node - Present in 1st but not in 2nd, present in 2nd but not in 1st and Common rows in both.
*	Prints output datasets created after comparing incoming datasets.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-workflow.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Incoming datasets**

* First incoming dataset

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-incoming-dataset1.png
   :alt: datavalidation_userguide
   :width: 90%
   
* Secong incoming dataset

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-incoming-dataset2.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Compare Datasets Node configuration**

*	``Compare Datasets`` node is configured as below.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-config.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Compare Datasets Node output**

Output of ``Compare Datasets`` node would be datasets created by comparing incoming datasets.

*	Various comparison results printed as below

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-printnode-output1.png
   :alt: datavalidation_userguide
   :width: 90%       	    

*	Rows present in 1st but not in 2nd

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-printnode-output2.png
   :alt: datavalidation_userguide
   :width: 90%       	    

*	Rows present in 2nd but not in 1st

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-printnode-output3.png
   :alt: datavalidation_userguide
   :width: 90%       	    

*	Rows common in both the incoming datasets

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/compdatasets-printnode-output4.png
   :alt: datavalidation_userguide
   :width: 90%       	    

Node Schema Validation
----------------------------------------

Below is a sample workflow which contains ``Node Schema Validation`` processor in Fire Insights. It demonstrates usage of ``Node Schema Validation`` node to validate incoming dataset schema against defined schema validation rules. It also imputes missing values as per rules definition.

It does following processing of data:

*	Reads incoming Datasets.
*	Validates incoming dataset schema against defined schema validation rules using ``Node Schema Validation`` node. It also imputes missing values as per rules definition.
*	Prints output dataset after imputing missing values.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/schemavalidation-workflow.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/schemavalidation-incoming-dataset.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Node Schema Validation Node configuration**

*	``Node Schema Validation`` node is configured as below.
*	Validation rule needs to be entered in the ``Validation`` box. Validation rule needs to be entered in the format - Column_Name, Data_Type, Required (true/false), Value_To_ImputeMissingValue. Each rule needs to be entered in a separate row.
*	Output would be a dataset after imputing missing values.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/schemavalidation-config.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Node Schema Validation Node output**

Output of ``Node Schema Validation`` node would be a dataset after imputing missing values.

*	Various validations results printed as below

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/schemavalidation-printnode-output1.png
   :alt: datavalidation_userguide
   :width: 90%       	    

*	Schema Validation result

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/schemavalidation-printnode-output2.png
   :alt: datavalidation_userguide
   :width: 90%       	    

*	Dataset after imputing missing values

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/schemavalidation-printnode-output3.png
   :alt: datavalidation_userguide
   :width: 90%       	    


Validate Address
----------------------------------------

Below is a sample workflow which contains ``Validate Address`` processor in Fire Insights. It demonstrates usage of ``Validate Address`` node to validate address data value against a valid address format. Some of the valid address formats are '123 xyx avenue' and '1/1 block-D street'

It does following processing of data:

*	Reads incoming Datasets.
*	Validates address data value against a valid address format using ``Validate Address`` node. Some of the valid address formats are '123 xyx avenue' and '1/1 block-D street'.
*	Prints address validation result in output.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/validateadd-workflow.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Incoming dataset**

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/validateadd-incoming-dataset.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Validate Address Node configuration**

*	``Validate Address`` node is configured as below.
*	Column containing Address value is to be selected in ``Input Column Name`` list.
*	Output prints address validation result.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/validateadd-config.png
   :alt: datavalidation_userguide
   :width: 90%
   
**Validate Address Node output**

Output of ``Validate Address`` node prints address validation result.

.. figure:: ../../_assets/user-guide/data-preparation/data-validation/validateadd-printnode-output.png
   :alt: datavalidation_userguide
   :width: 90%       	    

