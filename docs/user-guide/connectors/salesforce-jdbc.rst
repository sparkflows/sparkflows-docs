Salesforce using JDBC
===========

Fire Insights enable to Read from and Write to Salesforce using cdata JDBC Driver.

Below are the steps for Downloading and Configuring cdata JDBC Driver and Reading and Writing to Salesforce in Fire Insights

Download and Configure cdata JDBC Driver
----------------

Login to cdata Salesforce JDBC Driver page and Click on Download Trial version, after adding some needed information you can download in zip format in your system.

::

    https://www.cdata.com/drivers/salesforce/download/jdbc/
    

.. figure:: ../../_assets/user-guide/salesforce/3.PNG
   :alt: salesforce
   :width: 90%
   
   
.. figure:: ../../_assets/user-guide/salesforce/4.PNG
   :alt: salesforce
   :width: 90%   

.. figure:: ../../_assets/user-guide/salesforce/5.PNG
   :alt: salesforce
   :width: 90%   
   
Once Dowloaded completed, unzip that and extract jar from file `setup.jar` with below command and accept END USER LICENSE AGREEMENT with some required informations.   

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
   
Configured cdata JDBC Driver in Fire Insights
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now cdata JDBC Driver jar can be configured in Fire Insights to Read and Write to Salesforce using JDBC Connection.

Below are steps to configure cdata JDBC Driver in Fire Insights and Read and Write to Salesforce.

- Copy the ``cdata.jdbc.salesforce.jar`` to ``fire-user-lib & fire-server-lib`` and restart the Fire server.

