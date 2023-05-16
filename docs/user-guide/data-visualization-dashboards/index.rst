Dashboards
=======================

Dashboards in Fire Insights are powerful tools for data visualization and analysis, offering a consolidated view of key metrics and information. They enable real-time monitoring of performance indicators, facilitate data exploration through drill-down and filtering options, allow for performance tracking and goal evaluation, simplify report generation with customizable layouts and visualizations, and promote collaboration and communication through interactive features. 

The steps involved in creating dashboards in Fire Insights are:

#. Create MySQL connection
#. Add Google REST API key
#. Create JDBC dataset
#. Create chart(s)
#. Create dashboard(s)

This document explains in detail the steps required to create a dashboard in Fire Insights.

Step 1 : Create MySQL Connection
--------------------

Creating a MySQL connection is a prerequisite for creating dashboard. 

`Follow the steps given here to create a new MySQL connection. <SQL Server>`_

Step 2 : Add Google REST API Key
-----------

Another prerequisite for creating a dashboard is to add the Google REST API Key that is used in displaying the Google Maps.


Step 3 : Create JDBC Dataset
---------

#. On the Datasets List page, click **Create** and choose **Using Connections**.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/2.png
      :alt: Dataset
      :width: 65%

#. On Create Dataset dialog window, select the **MySQL Connection** that you want to use to create dataset.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/3.png
      :alt: Dataset
      :width: 65%

#. On Dataset Details page, enter the **field details** as below:

   - **NAME**: Name of the new dataset being created.
   - **DESCRIPTION**: Description of the new dataset.
   - **CATEGORY**: Category of the new dataset.
   - **DB**: Database for MySQL database.
   - **TABLE**: Table for MySQL.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/4.png
      :alt: Dataset
      :width: 65%

#. After you enter field details, click **Update Sample Data/Schema** to update the schema of the dataset.

   This step would display sample data for the dataset followed by the Schema inferred by Fire Insights.

   *Note: You can also customize the column names in the schema as per your choice.*
 
   .. figure:: ../../_assets/tutorials/dataset/Dashboards/5.png
      :alt: Dataset
      :width: 65%

#. Click **Save** to save the new dataset. Now, you are ready to use this dataset.

Step 4: Create Charts
-----------

#. Click **Dashboards** tab in the same project where you have created the JDBC dataset.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/6.png
      :alt: Dataset
      :width: 65%

#. Click **Charts** tab and then click **Choose a JDBC dataset**.
   
   From the **drop-down** list, choose the dataset for which you want to create a chart.

   .. figure:: ../../_assets/tutorials/dataset/jdbc_dataset.PNG
      :alt: Dataset
      :width: 65%

#. On the same page, click **Create New** to reach **Chart Editor** page.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/8.png
      :alt: Dataset
      :width: 65%

#. To see and select from available chart types, click **Bar Chart** drop-down button.
   
   .. figure:: ../../_assets/tutorials/dataset/Dashboards/9.png
      :alt: Dataset
      :width: 65%

#. To create chart, **drag-and-drop columns** from the dataset pane on the LHS to **x and y axis** and add **filters** as per your need.
   
   Note: In our example, we selected *Bar Chart* and updated column for x and y axis and added some filters.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/10.png
      :alt: Dataset
      :width: 65%

#. Give **name, description and category** to your chart and click **save** to save it.
   
   Once you save it, the chart will appear on the chart list page.

   Similarly, you can create a different chart using a specified chart type.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/11.png
      :alt: Dataset
      :width: 65%

   Now, you are ready to create a new dashboard using existing chart(s).
   
   
Step 5 : Create Dashboard
------
   
#. On the Dashboards List page, select the **Dashboards** tab (LHS) and click on **Create Dashboard** (RHS).

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/12.png
      :alt: Dataset
      :width: 65%
  
   You will reach the **Dashboard Editor** page as below.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/13.png
      :alt: Dataset
      :width: 65%

#. On the **Dashboard Editor** page, **add charts** from LHS pane displaying all the charts using **drag-and-drop** method.
   
   .. figure:: ../../_assets/tutorials/dataset/Dashboards/14.png
      :alt: Dataset
      :width: 65%
  
#. Give a **name** and **description** to your dashboard and click **Save** to save it.

   Once the Dashboard gets successfully saved, it will appear on the dashboard list (Grid or List view) page from where you can view, edit and delete it.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/15.png
      :alt: Dataset
      :width: 65%

.. note::  Make sure to add Google REST API key in Fire Insights configurations.
