EMR LIVY CONNECTION
=============

Fire Insights enable you to create Livy Connection and use the Connection to submit the Job.

Below are steps on how to create Livy Connection in Fire Insights.

1. Login to Fire Insights application and go inside Global Connections

Once you login to Fire Insights application Click on ''ADMINISTRATION'' tab on top, it will take you to Global Connections page, on clicking, it will take to configuration page.

.. figure:: ../../_assets/aws/livy/administration.PNG
   :alt: livy
   :width: 60%
   
2. Add Connection For Group

Once on Global Connections page Click on ''Add Connection For Group'' which pop up a new windows with Different ``Compute & Storage`` Connection, Select Compute Connection.

.. figure:: ../../_assets/aws/livy/add_connection.PNG
   :alt: livy
   :width: 60%
   
.. figure:: ../../_assets/aws/livy/add_livy_connection.PNG
   :alt: livy
   :width: 60%   
   
3. Update below parameter as per your Configurations

Once you Selected ''Connection Type & Groups'', Add the Connection parameters needed.

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Connection name
     - Connection Name
     - Name of Connection
   * - Postback Url
     - Postback Url
     - Postback Url through which Livy sent result back to Fire Insights
   * - Title 
     - Title of Selected Connection
     - Title of Selected Connection  
   * - Description 
     - Connection Description 
     - Connection Description
   * - Url
     - Url for selected COnnection type
     - Add URL for Livy Connection
   * - Driver Class
     - Driver Class for selected Connection type 
     - it COmes with default value  
     
