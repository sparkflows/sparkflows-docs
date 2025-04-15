Databricks Connection
=======

Sparkflows enables you to create Databricks connection and use the connection to submit job on respective Databricks cluster. Connections can be at various levels:

  * Global : Everyone has access to these connections.
  * Group  : Users belonging to the group have access to these connections.
  * Project: The owner of the project and the groups with which the Project has been shared with have access to the Project level connections.

Below are the steps required to create Databricks connection:

1. Login to Sparkflows web server URL. 

It can be created by the Administrator under ``Administration -> Global/Group Connections``. These connections are available for everyone to use if defined at ``Global`` level or for a particular Group if defined at the ``Group`` level.

.. figure:: ../../../_assets/installation/connection/databricks_selgrp_global.png
   :alt: connection
   :width: 60%    

2. Add Connection details

Make selection in the ``Add Connection`` screen as below to create ``Databricks Compute`` connection.

.. figure:: ../../../_assets/installation/connection/databricks_sel_type.png
   :alt: connection
   :width: 60%    

3. On selection ``Databricks`` from the dropdown page would be displayed as below with ``General`` and ``Databricks`` tabs:

Content of the ``General Tab`` would be based on the ``Authentication Type`` selected.

For more details on the fields refer the following table:

GENERAL Tab (User Credential):

.. list-table:: 
   :widths: 10 20 20
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - CREDENTIAL STORE  
     - Select the Credential Store from drop-down
     - Choose specific Credential Store from drop-down or Select Do not use Credential Store
   * - Select Category
     - Select Category of Connection Type
     - Select Compute Connection
   * - CONNECTION TYPE 
     - Select the Connection type from drop-down
     - Choose Databricks as Connection Type
   * - CONNECTION NAME
     - Connection Name
     - Add an unique Connection Name
   * - Auth Type
     - Select the Authentication Type
     - Select the appropriate option from ``User Credential`` or ``OAUTH``
   * - TOKEN 
     - Token
     - Add token generated
   * - POSTBACK URL
     - Fire Insights Post Back URL
     - Add Fire Insights Post Back URL
   * - TITLE 
     - Title for selected Connection
     - Add an unique Title
   * - DESCRIPTION
     - Connection Description
     - Add some Connection Description
   * - URL
     - Jdbc url for databricks connection
     - Add Jdbc Url for Databricks Connection

.. figure:: ../../../_assets/installation/connection/databricks_add_conn1.png
   :alt: connection
   :width: 60%    

.. figure:: ../../../_assets/installation/connection/databricks_general_uc1.png
   :alt: connection
   :width: 60%    

GENERAL Tab (OAUTH):

.. list-table:: 
   :widths: 10 20 20
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - CREDENTIAL STORE  
     - Select the Credential Store from drop-down
     - Choose specific Credential Store from drop-down or Select Do not use Credential Store
   * - Select Category
     - Select Category of Connection Type
     - Select Compute Connection
   * - CONNECTION TYPE 
     - Select the Connection type from drop-down
     - Choose Databricks as Connection Type
   * - CONNECTION NAME
     - Connection Name
     - Add an unique Connection Name
   * - Auth Type
     - Select the Authentication Type
     - Select the appropriate option from ``User Credential`` or ``OAUTH``
   * - POSTBACK URL
     - Fire Insights Post Back URL
     - Add Fire Insights Post Back URL
   * - Client ID 
     - Client ID for the connection
     - Enter Client ID for the connection
   * - Client Secret 
     - Client Secret for the connection
     - Enter Client Secret for the connection
   * - TITLE 
     - Title for selected Connection
     - Add an unique Title
   * - DESCRIPTION
     - Connection Description
     - Add some Connection Description
   * - URL
     - Jdbc url for databricks connection
     - Add Jdbc Url for Databricks Connection

.. figure:: ../../../_assets/installation/connection/databricks_add_conn1.png
   :alt: connection
   :width: 60%    

.. figure:: ../../../_assets/installation/connection/databricks_general_oa1.png
   :alt: connection
   :width: 60%    

For more details on creating Databricks connection refer the following image:

DATABRICKS Tab :

.. list-table:: 
   :widths: 10 20 20
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Fire core jar
     - path of Fire core jar dependencies
     - Absolute path of Fire core jar  
   * - Python file
     - path of Pyspark main file
     - Absolute path of Pyspark main file
   * - Fire pyspark libraries
     - path of Fire pyspark libraries
     - Absolute path of Fire pyspark libraries
   * - DBFS Scratch directory
     - Scratch directory on DBFS where it have Read/Write/Delete Permissions.
     - Absolute path ex. dbfs:/FileStore


.. figure:: ../../../_assets/installation/connection/databricks_other.PNG
   :alt: connection
   :width: 60%    

2.  Test & Save the Connection

Once you save the connection, it can be used for submitting the job on specific Databricks cluster.

Documentation
+++++

Reference guide : `Databricks User Guide Documentation. <https://docs.sparkflows.io/en/latest/databricks-user-guide/index.html>`_

.. note:: Make sure to add "POSTBACK URL" through which jobs running on Databricks would post back results to Sparkflows using this URL or else it will take from ``app.postMessageURL``, added in configuration.
