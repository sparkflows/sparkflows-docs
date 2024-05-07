Databricks Integration Steps
======================

Fire Insights integrates with Databricks. It submits jobs to the Databricks clusters using the REST API of Databricks and have the results displayed back in Fire Insights.

Fire also fetches the list of Databases and Tables from Databricks, making it easier for the user to build their workflows and execute them. 

In addition fire displays the list of Databricks clusters running for the user.

Databricks can be running on Azure or on AWS.

* Running Databricks on Azure : `Azure-Databricks Documentation <https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal>`_
* Running Databricks on AWS : `AWS-Databricks Documentation <https://databricks.com/aws>`_

Below are the steps for Integrating Fire Insights with your Databricks clusters.

Step 1 : Install Fire Insights
^^^^^^^^^^^^^^^^

To begin, install Fire Insights on any machine. Ensure that this machine is accessible from your Databricks cluster.

Step 2 : Upload Fire Core JAR to Databricks
^^^^^^^^^^^^^^

Fire Insights relies on a specific JAR file to execute tasks within Databricks. 

This JAR file, named **fire-spark_3.2.1-core-3.1.0-jar-with-dependencies.jar**, must be uploaded to Library on to Databricks. 

You can do this by following these steps:

#. **Login** to your **Databricks Account** using your credentials.
#. Click on **Compute** located on the left side pane.
   
   .. figure:: ../../_assets/configuration/databricks_intsall_lib.PNG
      :alt: Databricks
      :width: 60%
   
#. Click on **Install new** from **Libraries** tab.

   .. figure:: ../../_assets/configuration/databricks_intsall_lib.PNG
      :alt: Databricks
      :width: 60%

#. Upload JAR File **fire-spark_3.2.1-core-3.1.0-jar-with-dependencies.jar** either from your machine or
   
   use the download link from the previous step by selecting the **Drop JAR here** option or you can upload it **dbfs** location and copy the full path.

   .. figure:: ../../_assets/configuration/databricks_lib_core.PNG
       :alt: Databricks
       :width: 60%
   
#. Once **fire-spark_3.2.1-core-3.1.0-jar-with-dependencies.jar** path is updated, click on **install**.

   .. figure:: ../../_assets/configuration/databricks_lib_update.PNG
      :alt: Databricks
      :width: 60%
   
   .. note:: This will install library on Databricks cluster.
   

Step 3 : Create REST API Token in Databricks
^^^^^^^^^^^^^^

To facilitate communication between Fire Insights and Databricks via REST API calls, a token must be generated in your Databricks account. 

Follow these steps to create your token:

#. **Login** to your **Databricks Account** using your credentials.
#. Click on **Settings**.

   .. figure:: ../../_assets/configuration/user-setting.png
      :alt: Databricks
      :width: 60%

#. Click on **Developer**.

   .. figure:: ../../_assets/configuration/databricks_access_token.png
      :alt: Databricks
      :width: 60%

#. Click on **Manage & Generate new token**.

   .. figure:: ../../_assets/configuration/databricks_generate_token.png
      :alt: Databricks
      :width: 60%

#. Add **Comment & Lifetime(days)** for token expiry & click on **Generate**.

   .. figure:: ../../_assets/configuration/databricks_token.png
      :alt: Databricks
      :width: 60%

#. Copy the token generated and click on **DONE**.

   .. figure:: ../../_assets/configuration/databricks_token_copy.png
      :alt: Databricks
      :width: 60%


Step 4 : Create Databricks Connection in Fire Insights
^^^^^^^^^^^^^^

The connection can be created by the **Administrator** under **Administration/Global Connections**. These connections are available for everyone to use. It can also be created by any user with their Application. In this case, it is only available to the Application and its users.

Refer the below table for more details on parameter settings:

GENERAL Tab :

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
     
.. figure:: ../../_assets/installation/connection/databricks_general.PNG
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


.. figure:: ../../_assets/installation/connection/databricks_other.PNG
   :alt: connection
   :width: 60%    

Step 5 : Test and Save the Connection
^^^^^^^^^^^^^^^^^^^^^^

After setting the parameters, test the connection and save it. Once the connection is saved, it can be used for submitting the job on specific Databricks cluster.

More details on creating these connections can be found here : `Create Databricks Connection <https://docs.sparkflows.io/en/latest/installation/connection/compute-connection/databricks.html>`_

.. note:: Please make sure to specify a POSTBACK URL. This is the address where results from Databricks jobs will be sent to Fire Insights. If you don't provide one, the system will automatically use the **app.postMessageURL** updated by default in configurations.

With these steps completed, you're now ready to harness the power of the Databricks Connection within Fire Insights. This integration allows you to seamlessly:

* Browse Databricks File System (DBFS).
* Access information about your Databricks Clusters.
* Explore your Databricks Databases and Tables.
* Create workflows that read from and write to Databricks, enhancing your data processing capabilities.


