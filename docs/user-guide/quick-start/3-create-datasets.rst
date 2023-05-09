Step 3 : Create Dataset
---------

To use a data file in multiple projects, it is ideal to wrap it into a dataset. Dataset allows the schema and other meta information of the data to be defined in one place.

The steps involved in creating a dataset are:

#. **Open** the **project** where you want to create a dataset and click **Datasets tab**.
#. Click on **Create** and choose one of the methods from the **drop-down** list to create a Dataset.
#. Select the **dataset type** and enter the **fields** in the dialog box.
#. Click **Update Sample Data/Schema** to update schema and click **Eye Icon** to view the file contents.
#. Click **Save** to save the new dataset.

This page shows the detailed steps for creating a Dataset.

Step 1 : Open the Project
======

#. Click the **Projects** tab in the **top-menu bar** of the Fire Insights.
#. Click the **Project Name** where you want to create your dataset.
#. Click the **Datasets** tab in upper-middle bar on the Project page.

Step 2 : Select the Method to Create Dataset
=============

#. Click **Create** on the **Dataset Page**.
#. Select the method to create the dataset from the **drop-down** list. You can choose from the following methods offered:
   
   * From Existing File
   * By Uploading New File
   * Using Connections
  
  Here, we choose **From Existing Files** method. 

  .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-1.png
   :alt: Dataset
   :width: 60%

Step 3: Select Dataset Type and Enter the Fields
===============
 
#. On the pop-up **Create Dataset Page**, select dataset type from the available file formats e.g. CSV, XML, AVRO etc. Here, we choose **CSV**.

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

#. Click **Update Sample Data/Schema** to update the schema of the dataset. Sample data for the dataset will be displayed followed by the schema.

   .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-3.png
    :alt: Dataset
    :width: 60% 

#. Click **Eye Icon** located adjacent to **Browse File System** button to view the file contents.

   .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-4.png
    :alt: Dataset
    :width: 60%
  
.. note:: In our example, the dataset is created from a file named ``housing.csv`` . It is a comma separated file with a header row specifying the names of the various columns. If the data file does not have a header row, Fire Insights will give dummy column names like ``C0``, ``C1``, etc. You can update the column names in the schema based on your data.

Step 5 : Save the New Dataset
=======

Click **Save** to save the new dataset and you are ready to use it in your workflows.

View the New Dataset
======== 
 
Click the **Datasets Tab** to see the list of all the datasets that belong to the project.

  .. figure:: ../../_assets/tutorials/dataset/Create-Dataset/NewDataset-5.png
   :alt: Dataset
   :width: 60%







 
 
 
 
 
 
 
 










 
 
 
 
 
 
 
 



