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
