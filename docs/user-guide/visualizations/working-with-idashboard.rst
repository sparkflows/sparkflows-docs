Interactive Dashboard
=======================

Fire allows you to create interactive Dashboards.

Fire enable to create New Dataset using JDBC data type from MYSQL db & use that jdbc datasets in creating charts & dashboard.

Creating I-Dashboard
--------------------

- For creating I-Dashboard, Create JDBC datasets if not available.

You can define a New Dataset by clicking on the ``Create Dataset`` button in the Dataset page.

It will bring up the dialog box below. Select the format of the file for which the new Dataset is being created.

.. figure:: ../../_assets/tutorials/dataset/jdbc_dataset.PNG
   :alt: Dataset
   :align: center
   :width: 60%

Entering Field Details
^^^^^^^^^^^^^^^^^^^^

Below are the details of the fields in the ``Create Dataset`` page:

- **NAME** : Name of the New Dataset we are creating.
- **DESCRIPTION** : Description of the New Dataset.
- **CATEGORY** : category of the New Dataset.
- **JDBC DRIVER** : Enter JDBC DRIVER.
- **JDBC URL** : Enter JDBC URL for MYSQL DB.
- **USER** : username for MYSQL DB.
- **PASSWORD** : password for MYSQL DB.
- **DB** : Database for MYSQL DB.
- **TABLE** : Table for MYSQL.


.. figure:: ../../_assets/tutorials/dataset/create_data.PNG
   :alt: Dataset
   :align: center
   :width: 60%

Updating the Schema of the Dataset
^^^^^^^^^^^^^^^^^^^^

You can update the Schema of the Dataset by clicking on ``Update Sample Data/Schema``. It would display sample data for the dataset followed by the Schema inferred by Fire Insights.

You can update the column names in the schema based on your data.
 
 .. figure:: ../../_assets/tutorials/dataset/update_sampledata.PNG
   :alt: Dataset
   :align: center
   :width: 60%

Saving the New Dataset
^^^^^^^^^^^^^^^^^^^^

Click on the ``Save`` button to save the New Dataset created.

