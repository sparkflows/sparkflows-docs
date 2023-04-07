Cast Data Type
==========

Fire Insights provides processors for Cast Data Type.


Cast Data Type Processors in Fire Insights
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Cast To Different Types-1
     - It casts specified columns to different datatypes as specified.
   * - Cast To Different Types-2
     - It casts specified columns to different datatypes in the specified format.
   * - Cast To Single Type
     - It casts the specified input columns to a new data type.
 
Cast To Different Types-1
----------------------------------------

Below is a sample workflow which contains Cast To Different Types-1 processor in Fire Insights. It demonstrates the usage of Cast To Different Types-1 node to cast columns to different datatypes.

It does the following processing of data:

*	Reads incoming dataset.
*	Casts columns from incoming dataset to different datatypes using Cast To Different Types-1 node.
*	Prints output dataset with columns casted to different datatypes using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastType1WF.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/InputData.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Cast To Different Types-1 Node configuration**

Cast To Different Types-1 node is configured as below.

*	Input of this node are the incoming dataset.
*	Column that needs to be casted to different datatype is to be selected in the ``Columns`` list.
*	Datatype to which Column needs to be casted is to be selected in the ``New Data Type`` list.
*	``Replace Existing Cols`` needs to be selected as ``True`` if casted column is needed to replace the existing column in the output.
*	A ``Variables List`` row needs to be added for each casting requirement.
*	Output of this node would display dataset with columns casted to different datatypes.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastType1Config.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Cast To Different Types-1 Node output**

Output of Cast To Different Types-1 node displaying dataset with columns casted to different datatypes.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastType1Output.png
   :alt: castdatatype_userguide
   :width: 70%       	    
   

Cast To Different Types-2
----------------------------------------

Below is a sample workflow which contains Cast To Different Types-2 processor in Fire Insights. It demonstrates the usage of Cast To Different Types-2 node to cast columns to different datatype in the specified format.

It does the following processing of data:

*	Reads incoming dataset.
*	Casts columns to different datatype in the specified format using Cast To Different Types-2 node.
*	Prints output dataset with columns casted to different datatype in the specified format using the Print node.


.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastType2WF.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/InputData.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Cast To Different Types-2 Node configuration**

Cast To Different Types-2 node is configured as below.

*	Input of this node are the incoming dataset.
*	Column that needs to be casted to different datatype is to be selected in the ``Columns`` list.
*	Datatype to which Column needs to be casted is to be selected in the ``New Data Type`` list.
*	``Replace Existing Cols`` needs to be selected as ``True`` if casted column is needed to replace the the existing column in the output.
*	Format of the output data is to be specified in ``Formats`` box.
*	A ``Variables List`` row needs to be added for each casting requirement.
*	Output of this node would display dataset with columns casted to different datatype in the specified format.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastType2Config.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Cast To Different Types-2 Node Output**

Output of Cast To Different Types-2 node displaying dataset with columns casted to different datatype in the specified format.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastType2Output.png
   :alt: castdatatype_userguide
   :width: 70%       	    
   

Cast To Single Type
----------------------------------------

Below is a sample workflow which contains Cast To Single Type processor in Fire Insights. It demonstrates the usage of Cast To Single Type node to cast selected columns to single datatypes.

It does the following processing of data:

*	Reads incoming dataset.
*	Casts selected columns to single datatypes using Cast To Single Type node.
*	Prints output dataset with columns casted to single datatype using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastSingleWF.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Incoming Dataset**

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/InputData.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Cast To Single Type Node Configuration**

Cast To Single Type node is configured as below.

*	Input of this node are the incoming dataset.
*	Columns that are needed to be casted to single datatype are to be selected in the ``Columns`` list.
*	Datatype to which Columns need to be casted is to be selected in the ``New Data Type`` list.
*	``Replace Existing Cols`` needs to be selected as ``True`` if casted columns are needed to replace the existing columns in the output.
*	Output of this node would display dataset with columns casted to single datatype.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/InputData.png
   :alt: castdatatype_userguide
   :width: 70%
   
.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastSingleConfig.png
   :alt: castdatatype_userguide
   :width: 70%
   
**Cast To Single Type Node Output**

Output of Cast To Single Type node displaying dataset with columns casted to single datatype.

.. figure:: ../../_assets/user-guide/data-preparation/castdatatype/CastSingleOutput.png
   :alt: castdatatype_userguide
   :width: 70%       	    
   

