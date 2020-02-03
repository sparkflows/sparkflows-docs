Creating New Datasets
-----------------
 
You can define a New Dataset by clicking on the ``Create Dataset`` button in the Dataset page.

It will bring up the dialog box below. Select the format of the file for which the new Dataset is being created.

.. figure:: ../../_assets/tutorials/dataset/10.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
Entering Field Details
^^^^^^^^^^^^^^^^^^^^

Below are the details of the fields in the ``Create Dataset`` page:

- **NAME** : Name of the New Dataset we are creating.
- **DESCRIPTION** : Description of the New Dataset.
- **HAS HEADER ROW** : This is used for CSV/TSV files. It indicates whether the dataset has a header row specifying the name of the columns or not.
- **DELIMITER** : Delimiter field is also used for CSV/TSV files. It indicates the delimiter to be used between the fields in the data.
- **PATH** : It defines the location of the file or directory containing the data files for the Dataset. It can either point to a single file, or to a directory containing a set of files. All the files have to have the same schema.


    
 .. figure:: ../../_assets/tutorials/dataset/16.PNG
   :alt: Dataset
   :align: center
   :width: 60%  


Updating the Schema of the Dataset
^^^^^^^^^^^^^^^^^^^^

You can update the Schema of the Dataset by clicking on ``Update Sample Data/Schema``. It would display sample data for the dataset followed by the Schema inferred by Fire Insights.

In this example, the data file did not have a header row. So Fire gave it standard column names of ``C0, C1`` etc.

You can update the column names in the schema based on your data.
 
 .. figure:: ../../_assets/tutorials/dataset/17.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   

Saving the New Dataset
^^^^^^^^^^^^^^^^^^^^

Click on the ``Save`` button to save the New Dataset created.
 
 
 
 
 
 
 
 
 
 
 
 




