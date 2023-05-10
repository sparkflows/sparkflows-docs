Step 3 : Create Dataset
---------

To use a data file in multiple projects, it is ideal to wrap it into a dataset. Dataset allows the schema and other meta information of the data to be defined in one place.

The steps involved in creating a dataset are:

#. **Open** the **project** where you want to create a dataset and click **Datasets tab**.
#. Click on **Create** and choose one of the methods from the **drop-down** list to create a Dataset.
#. Select the **dataset type** and enter the **fields** in the dialog box.
#. Click **Update Sample Data/Schema** to update schema and click **Eye Icon** to view the file contents.
#. Click **Save** to save the new dataset.

This document explains in detail the steps involved in creating a dataset.

Step 1 : Open the Project
======

#. Click the **Projects** tab in the **top-menu bar** of the Fire Insights.
#. Click the **Project Name** where you want to create your dataset.
#. Click the **Datasets** tab in upper-middle bar on the Project page.

Step 2 : Select the Method to Create Dataset
=============

#. Click **Create** on the **Dataset Page**.
#. Select the method to create the dataset from the **drop-down** list. Choose any one of the below:
   
   * From Existing File
   * By Uploading New File
   * Using Connections
  
  Here, we choose **From Existing File** method. 

  .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-1.png
   :alt: Dataset
   :width: 60%

Step 3: Select Dataset Type and Enter the Fields
===============
 
#. On the pop-up **Create Dataset Page**, select dataset type from the available file formats.

   *Note: Fire offers AVRO, CSV, JSON, PARQUET, SEQUENCE, XML file formats.*  
   
   Here, we choose **CSV**.

   .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-2.png
    :alt: Dataset
    :width: 60% 

#. On the **Dataset Details Page**, enter the required fields as below:

   * ``Name``: Name of the new dataset. 
   * ``Category``: An apt category that you want to tag the dataset to.
   * ``Description``: Description of the new dataset.
   * ``Mode``: Choose the mode to mark the strictness of parsing of the data file.
   * ``Has Header Row``: Indicates whether the dataset has a header row specifying the names of the columns or not.
   * ``Delimiter``: Indicates the delimiter to be used between the fields in the data.
   * ``Path``: Path for the location of the file or directory containing the data files for the dataset.
   * ``Drop Sepcial Character in Column Name``: Indicate whether the dataset should drop special character in column name.  
 
Step 4: Update the Schema and View File Contents
===========

#. Click **Update Sample Data/Schema** to update the schema of the dataset. 

   *Note: Sample data for the dataset will be displayed followed by the schema.*

   .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-3.png
    :alt: Dataset
    :width: 60% 

#. Click **Eye Icon** located adjacent to **Browse File System** button to view the file contents.

   .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-4.png
    :alt: Dataset
    :width: 60%
  
.. note:: * We have created the dataset using a comma separated file named ``housing.csv`` which contains a header row specifying column names. 
          * If the file does not contain the header row, Fire will give dummy column names e.g. ``C0``, ``C1``, etc.  
          * In case of missing header row, Fire allows you to customize the column names in the schema based on your data.

Step 5 : Save the New Dataset
=======

#. Click **Save** to save the new dataset and you are ready to use it in your workflows.

View the New Dataset
======== 
 
#. Click the **Datasets Tab** to view the datasets list belonging to the project.

  .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-5.png
   :alt: Dataset
   :width: 60%







 
 
 
 
 
 
 
 










 
 
 
 
 
 
 
 



