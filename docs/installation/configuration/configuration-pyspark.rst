PySpark Configuration
========

Sparkflows can be configured to use the PySpark engine and create workflow using it. 

Follow the steps below for the same.

Step 1 : Log in to Sparkflows
-----
* Open your web browser.
* Navigate to Sparkflows webserver URL.
* Login with your credentials.

Step 2 : Update Configuration Settings
-----
* Go to **Administration -> Configurations**.
* Click on **Module** Tab.
* Search for the following configuration and set its value to **both**, as shown below and save the configuration.

  ::

     module.workflowTypes = both
    

  .. figure:: ../../_assets/installation/pyspark_configurations.PNG
     :alt: pyspark
     :width: 60%

Step 3 : Refresh the Webserver
-----
* Once the above configuration changes are saved, refresh the Sparkflows webserver URL to verify the latest configuration changes.

Step 4 : Create a PySpark Workflow
-----
* Open any **project** and select **Workflows** tab.
* Click on **Create** button. You should now see an option in the dropdown to create a workflow using the PySpark engine, as shown below.

  .. figure:: ../../_assets/installation/pyspark_wf.PNG
     :alt: pyspark
     :width: 60%

.. Note:: Make sure to install all Sparkflows python dependencies.
