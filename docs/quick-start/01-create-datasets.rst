Step 3 : Create a Dataset
----------------

In this step, create a dataset over customers transactions data. Creating a Dataset allows us to define it once and use it various workflows.

The steps involved in creating a dataset are:

- *Go to the Dataset Listing Page*
- *Click on Create New Dataset*
- *Enter the fields in the dialog for the file for which we are creating the Dataset*
- *Update the schema of the Dataset*
- *Save the Dataset with a new name*

Customer Transaction Data
=========================

The data is is CSV format.

Below are a few records from the data::


    GEO1,100,001,00R,000002,00003.45
    GEO1,100,002,00R,000010,00041.23
    GEO1,100,003,00G,003432,00451.12
    GEO3,200,001,00G,100001,00003.13
    GEO1,200,002,00B,567890,00001.00
    GEO3,200,003,00B,101010,00002.22
    GEO1,300,001,00R,234234,00033;10
    GEO1,300,002,00G,001000,00044.88


Go to the Dataset Listing Page
==============================

 .. figure:: ../../_assets/tutorials/01/dataset-listings.png
   :alt: Dataset Listings
   :align: center

Click on Create Dataset
=======================

Click on the ``Create Dataset`` link to get started with creating the new dataset.


Enter the Field Details
=======================

Enter the fields below into the form. Below are the details of the fields:

- **NAME** : Name of the New Dataset we are creating.
- **DESCRIPTION** : Description of the New Dataset.
- **HAS HEADER ROW** : This is used for CSV/TSV files. It indicates whether the dataset has a header row specifying the name of the columns or not.
- **DELIMITER** : Delimiter field is also used for CSV/TSV files. It indicates the delimiter to be used between the fields in the data.
- **PATH** : Path for the location of the file or directory containing the data files for the Dataset.


 
 .. figure:: ../../_assets/tutorials/01/create-new-dataset.png
   :alt: Sparkflows Create New Datasets
   :align: center
 
 
Update the Schema of the Dataset
================================

Now click on ``Update`` to update the Schema of the Dataset. It would display sample data for the dataset followed by the Schema.

In this case, the data file did not have a header row. So Fire gave it standard column names of ``C0, C1`` etc.

You can update the column names in the schema based on your data.
 
 .. figure:: ../../_assets/tutorials/01/dataset-schema.png
   :alt: Dataset Schema
   :align: center
   

Save the New Dataset
====================

Now click on ``Save`` to save the new Dataset created.
 
 
 
 
 
 
 
 



