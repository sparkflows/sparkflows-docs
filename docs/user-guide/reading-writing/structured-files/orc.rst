ORC
========


Save ORC
----------------------------------------

Below is a sample workflow which contains the Save ORC processor in Fire Insights. It demonstrates the usage of Save ORC node to save incoming dataset in ORC format.

It does the following processing of data:

*	Reads the incoming dataset.
*	Coalesce node is used to define the number of partitions to be created while saving.
*	Saves incoming dataset in ORC format using the Save ORC node.

.. figure:: ../../../_assets/user-guide/read-write/save-files/save-orc-wf.png
   :alt: savefiles_userguide
   :width: 50%
   
**Incoming Dataset**

.. figure:: ../../../_assets/user-guide/read-write/save-files/InputData.png
   :alt: savefiles_userguide
   :width: 75%
   
**Save ORC node configuration**

Save ORC node is configured as below.

*	HDFS location where created file needs to be saved is to be selected in the ``Path`` box.
*	Save mode to be selected in the ``Save Mode`` list. It states whether to *Append*, *Overwrite*, *Error out if file exists* or *Ignore* while saving the file.
*	Saves the incoming dataset in ORC format.

.. figure:: ../../../_assets/user-guide/read-write/save-files/OrcGenConfig.png
   :alt: savefiles_userguide
   :width: 75
