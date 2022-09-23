Salesforce using JDBC
===========

Fire Insights enable to Read from and Write to Salesforce using cdata JDBC Driver.

Below are the steps for Downloading and Configuring cdata JDBC Driver and Reading and Writing to Salesforce in Fire Insights

Download and Configure cdata JDBC Driver
----------------

Login to cdata Salesforce JDBC Driver page and Click on Download Trial version, after adding some needed information you can download in zip format in your system.

  * cdata JDBC Driver URL :  https://www.cdata.com/drivers/salesforce/download/jdbc/
    

.. figure:: ../../_assets/user-guide/salesforce/3.PNG
   :alt: salesforce
   :width: 90%
   
   
.. figure:: ../../_assets/user-guide/salesforce/4.PNG
   :alt: salesforce
   :width: 90%   

.. figure:: ../../_assets/user-guide/salesforce/5.PNG
   :alt: salesforce
   :width: 90%   
   
Once Dowload completed, unzip that and extract jar from file `setup.jar` with below command and accept END USER LICENSE AGREEMENT with some required informations.   

::

    java -jar setup.jar
    
.. figure:: ../../_assets/user-guide/salesforce/6.PNG
   :alt: salesforce
   :width: 90%   

.. figure:: ../../_assets/user-guide/salesforce/7.PNG
   :alt: salesforce
   :width: 90%   
   
.. figure:: ../../_assets/user-guide/salesforce/8.PNG
   :alt: salesforce
   :width: 90%    
 
On Successful completion of above steps, Go to path where you installed salesforce drive and point to below path:

::

    $salesforce_home/lib/
    
    
.. figure:: ../../_assets/user-guide/salesforce/9.PNG
   :alt: salesforce
   :width: 90%     
   
Configure cdata JDBC Driver in Fire Insights
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now cdata JDBC Driver jar can be configured in Fire Insights to Read and Write to Salesforce using JDBC Processors.

Below are steps to configure cdata JDBC Driver in Fire Insights and Read and Write to Salesforce.

- Copy the ``cdata.jdbc.salesforce.jar`` to ``fire-user-lib & fire-server-lib`` and restart the Fire server.
- Login to Fire Insights application and Go inside project and workflow tab to create an example workflow with Read and Write to Salesforce using Read JDBC & Save JDBC Processors.

Read Salesforce
---------------

Now you can Read Salesforce using cdata JDBC Driver in Fire Insights application using Read JDBC Processor


Processor Configuration Parameters for Salesforce cdata JDBC Connection:

.. list-table::
      :widths: 5 20
      :header-rows: 1

      * - Name
        - Value
      * - URL
        - JDBC URL to connect to salesforce using cdata JDBC Driver
      * - USER
        - USER NAME in Salesforce
      * - PASSWORD
        - PASSWORD in Salesforce
      * - DB TABLE 
        - Table Name
      * - DRIVER
        - Salesforce JDBC Driver Name ie. ``cdata.jdbc.salesforce.SalesforceDriver``

.. figure:: ../../_assets/user-guide/salesforce/10.PNG
   :alt: salesforce
   :width: 90% 

Once above parameter is added, Click on refresh schema to see Field Name

.. figure:: ../../_assets/user-guide/salesforce/11.PNG
   :alt: salesforce
   :width: 90% 

Processor output
--------------

.. figure:: ../../_assets/user-guide/salesforce/12.PNG
   :alt: salesforce
   :width: 90% 

Write to Salesforce
-----------------

Now you can Write to Salesforce using cdata JDBC Driver in Fire Insights application using Save JDBC Processor

Processor Configuration Parameters for Salesforce cdata JDBC Connection:

.. list-table::
      :widths: 5 20
      :header-rows: 1

      * - Name
        - Value
      * - URL 
        - Salesforce cdata JDBC Driver URL 
      * - DB TABLE
        - Table Name
      * - DRIVER
        - Salesforce JDBC Driver Name ie. ``cdata.jdbc.salesforce.SalesforceDriver``
      * - USER
        - USER NAME of Salesforce
      * - PASSWORD
        - PASSWORD of Salesforce
      * - TRUNCATE
        - false
      * - SAVE MODE
        - It can be Append, Overwrite, ErrorIfexist & Ignore
        
.. figure:: ../../_assets/user-guide/salesforce/13.PNG
   :alt: salesforce
   :width: 90%         

On Successful execution of Workflow the data will be Written to Salesforce.
