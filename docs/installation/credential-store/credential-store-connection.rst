Credential Store Connection
============================

Fire Insights enables you to create Connection. The values in the Connections can be fetched from the Credential Stores.

Below are the steps for adding connection using values from the Credential Store.

Go to Administration/Global Connections
-------------

Login to Fire Insights. Go to Administration and select Global Connections.

.. figure:: ../../_assets/credential_store/7.PNG
   :alt: Credential Store
   :width: 90%

Add Connection
-----------

Click on ADD CONNECTION. Select either of the two, Add Connection For All or Add Connection For Group based on your requirements.


.. figure:: ../../_assets/credential_store/8.PNG
   :alt: Credential Store
   :width: 90%
   

Add Connection Parameter
--------------------------

.. list-table:: Connection Parameter
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - CREDENTIAL STORE
     - Select Credential Store Listed in dropdown.
   * - CONNECTION TYPE
     - Select Connection type configured in KeyVault it can be `Databricks, MySql, MOngo DB, Sql Server, HIve, Redshift and Snowflake`
   * - CONNECTION NAME
     - Add a Connection Name.
   * - USERNAME
     - Username for the selected Connection and if username is added in KeyVault, add $USER-NAME
   * - PASSWORD
     - Password for selected Connection, and if password is added in KeyVault, add $PASSWORD
   * - TITLE
     - Add a unique title.
   * - DESCRIPTION
     - Add description.
   * - URL
     - URL for selected Connection, and if URL is added in KeyVault, add $URL
     
.. figure:: ../../_assets/credential_store/9.PNG
   :alt: Credential Store
   :width: 70%     

After Adding the above parameter, you can Click on TEST CONNECTION, It will shows Successfully Connected and after saving it will show in Connection LIst.

.. figure:: ../../_assets/credential_store/18.png
   :alt: Credential Store
   :width: 90%   
   
.. figure:: ../../_assets/credential_store/17.png
   :alt: Credential Store
   :width: 90%      

.. figure:: ../../_assets/credential_store/12.PNG
   :alt: Credential Store
   :width: 90%

Now you can use the connection in Processor in Workflow and Submit the Job etc..

.. figure:: ../../_assets/credential_store/13.PNG
   :alt: Credential Store
   :width: 90%

.. figure:: ../../_assets/credential_store/14.PNG
   :alt: Credential Store
   :width: 90%
   
.. figure:: ../../_assets/credential_store/15.PNG
   :alt: Credential Store
   :width: 90% 

.. figure:: ../../_assets/credential_store/16.PNG
   :alt: Credential Store
   :width: 90% 

.. note::  Above Example is shown for Snowflake Connection and Using Readsnowflake node in workflow.
