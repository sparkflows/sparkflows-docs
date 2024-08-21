Connections
-----------

Fire Insights enables you to create different connections. Sparkflows offers the following three types of Connections:

**1. Compute Connections   2. Storage Connections   3. GenerativeAI Connections**

Connections can be created at various levels:

* Global  : Everyone has access to these connections.
* Group   : Users belonging to a group will only have access to these connections.
* Project : The owner of the project and the groups with which the project has been shared with have access to these connections.

Below are the steps for creating a Connection:

Login to Sparkflows
+++++

Login to Sparkflows as an ``Admin``. Click on ``Administration`` tab from the main menu and then select ``Global Connections`` to reach the next page as shown below.


.. figure:: ../../../_assets/postgresql/administration.png
      :alt: postgresql
      :width: 60%

Add Connection
++++

Enter the configuration details with the help of table given below and click on ``Add Connection``.


.. figure:: ../../../_assets/installation/connection/mysql_storage.PNG
   :alt: connection
   :width: 60%


.. toctree::
   :maxdepth: 2

   compute-connection/index.rst
   storage-connection/index.rst
   gen-ai-connection/index.rst
