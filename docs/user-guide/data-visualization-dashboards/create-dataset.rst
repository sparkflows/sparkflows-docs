Create Dataset
======
This document explains in detail the prerequisites and steps required to create a Dataset in Sparkflows.

Prerequisites
------
Before you create a dashboard in Fire Insights, ensure the following prerequisites are completed:

**Create MySQL Connection**

Creating a MySQL connection is a prerequisite for creating dashboard.

Follow the steps given here to create a new MySQL connection: :ref:`Create MySQL Connection<SQL Server>`

**Add Google REST API Key**
  
Another prerequisite for creating a dashboard is to add the Google REST API Key in Fire Insights configuration. To add:

1.	**Login** to Fire Insights.
2.	From the Dashboard page, navigate to **Administration -> Configurations**.
  
 .. figure:: ../../_assets/tutorials/dataset/Dashboards/admin-page.png
       :alt: Dataset
       :width: 65%
  
3.	On Configurations page, click on ``PLUGINS`` tab in the middle bar.
4.	Add the **Google Rest API key** in the **Value** column, as shown below and click on **Save Configurations** button to save the key.

  .. figure:: ../../_assets/tutorials/dataset/Dashboards/api-config-page.png
      :alt: Dataset
      :width: 65%

Create JDBC Dataset
------
Follow the steps below to create a JDBC dataset in Fire Insights:
  
**Step 1 : Navigate to Datasets Page**
+++++++++++++++++++++++++++++++++++++++++
  
* Go to **Projects** and click on a **specific project**.
*	On the project page, click on ``Datasets`` tab to access Datasets List page.
  
**Step 2 : Select a MySQL Connection**
++++++++++++++++++++++++++++++++++++++++++
* Click on **Create** button and choose the option **Using Connection** from the dropdown, as shown below.
  
  .. figure:: ../../_assets/tutorials/dataset/Dashboards/2.png
      :alt: Dataset
      :width: 65%
  
* On Create Dataset dialog box, select the **MySQL Connection** from the dropdown that you want to use to create dataset.
  
  .. figure:: ../../_assets/tutorials/dataset/Dashboards/3.png
      :alt: Dataset
      :width: 65%
  
**Step 3 : Enter Dataset Details**
++++++++++++++++++++++++++++++++++++
  
* On Dataset Details page, enter the desired details as follows:
  
 •	``NAME`` : Name of the new dataset being created.
 •	``DESCRIPTION`` : Description of the new dataset.
 •	``CATEGORY`` : Category of the new dataset.
 •	``DB`` : Database for MySQL database.
 •	``TABLE`` : Table for MySQL.

   .. figure:: ../../_assets/tutorials/dataset/Dashboards/4.png
      :alt: Dataset
      :width: 65%


**Step 4 : Update Sample Data / Schema**
+++++++++++++++++++++++++++++++++++++++++
  
* Click on **Update Sample Data/Schema** button to update the schema of the dataset, as shown below. This step would display sample data for the dataset followed by the Schema inferred by Fire Insights.
 
  .. figure:: ../../_assets/tutorials/dataset/Dashboards/5.png
      :alt: Dataset
      :width: 65%
  
.. Note:: You can also customize the column names in the schema as per your choice.
  
**Step 5 : Save the Dataset**
++++++++++++++++++++++++++++++++

* Click on **Save** button to save the new dataset. Now, you are ready to use this dataset in **dashboards** or **charts**.





























