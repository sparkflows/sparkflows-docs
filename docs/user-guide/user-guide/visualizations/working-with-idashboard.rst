Dashboards
=======================

Fire Insights allows creating of the Dashboard. You can create new datasets using JDBC data type from MySQL database using connection & then use the datasets in creating charts & dashboards.

Creating Dashboard
--------------------

- For creating a Dashboard, you need to create MySQL Connection, add Google REST API key which is used in displaying the Google Maps and then create a JDBC dataset using it.

You can define a new dataset by clicking on the ``Create Dataset`` button using Connections option on the dataset page.

It will bring up the dialog box below. Select the MySQL Connection being used for creating dataset.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_connection.PNG
   :alt: Dataset
   :width: 80%

.. figure:: ../../../_assets/tutorials/dataset/jdbc_connection1.PNG
   :alt: Dataset
   :width: 80%

Entering Field Details
^^^^^^^^^^^^^^^^^^^^

Below are the details of the fields in the ``Create Dataset`` page:

- **NAME**: Name of the new dataset we are creating.
- **DESCRIPTION**: Description of the new dataset.
- **CATEGORY**: Category of the new dataset.
- **DB**: Database for MySQL database.
- **TABLE**: Table for MySQL.


.. figure:: ../../../_assets/tutorials/dataset/jdbc_dataset_detail.PNG
   :alt: Dataset
   :width: 80%

Updating the Schema of the Dataset
^^^^^^^^^^^^^^^^^^^^

You can update the Schema of the dataset by clicking on ``Update Sample Data/Schema``. It would display sample data for the dataset followed by the Schema inferred by Fire Insights.

You can update the column names in the schema based on your data.
 
 .. figure:: ../../../_assets/tutorials/dataset/jdbc_schema.PNG
   :alt: Dataset
   :width: 80%

Saving the New Dataset
^^^^^^^^^^^^^^^^^^^^

Click on the ``Save`` button to save the new dataset created.

Dashboard
^^^^^^^^^^^^^^^^^^^^^^

Click on the ``Dashboard`` tab in the same application where you have created JDBC dataset.


 .. figure:: ../../../_assets/tutorials/dataset/jdbc-dashboard.PNG
   :alt: Dataset
   :width: 80%

Click on the ``Chart`` tab & select Choose a JDBC dataset, there you will find all JDBC datasets created under your application.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_dataset.PNG
   :alt: Dataset
   :width: 80%

Select any JDBC dataset for which you want to create ``Chart`` & select ``CREATE NEW``

It will take you to the new page, as below :

.. figure:: ../../../_assets/tutorials/dataset/jdbc_chart_create.PNG
   :alt: Dataset
   :width: 80%

Select the ``Chart Type`` if you want to see the availble chart types.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_chart_type.PNG
   :alt: Dataset
   :width: 80%

In the above step, we selected ``Bar Chart`` & updated column for x & y axis and added some filters.

Add NAME, DESCRIPTION & save it.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_chart_update.PNG
   :alt: Dataset
   :width: 80%

Once you save it, the chart will appear on the chart list page.

Similarly, you can create a different chart using a specified chart type.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_chart_list.PNG
   :alt: Dataset
   :width: 80%

Now using an existing chart, you can create a new dashboard. 

Select the ``Dashboard`` tab & click on ``CREATE DASHBOARD``.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_dashboard.PNG
   :alt: Dataset
   :width: 80%

It will take you to the new dashboard page.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_dashboard_create.PNG
   :alt: Dataset
   :width: 80%

Using drag & drop you need to add a chart in canvas and then Add NAME and DESCRIPTION to it. After this SAVE it.

.. figure:: ../../../_assets/tutorials/dataset/save-dashboard.PNG
   :alt: Dataset
   :width: 80%

Once the Dashboard gets saved successfully, it will appear on the dashboard list (Grid or List view) page from where you can view, edit & delete it.

.. figure:: ../../../_assets/tutorials/dataset/jdbc_dashboard_page.PNG
   :alt: Dataset
   :width: 80%

.. note::  Make sure to add Google REST API key in Fire Insights configurations.
