Writing to S3 files
=========================

https://docs.databricks.com/_static/notebooks/data-import/s3.html

Fire Insights workflows can write data to S3 locations.

Here is an example workflow that writes data to S3. When the workflow is executed, the Dataframe is saved to the S3 location.

In the dialog box of the save CSV processor, the path is specified as ``s3a://fire-sample-data/write/``

.. figure:: ../_assets/aws/workflow_csvs3.PNG
   :alt: S3 Workflow
   :width: 100%

Browse S3 specified Path & other parameters for processor SaveCSV like below:

* PATH : Click on BROWSE S3 and specify the path where file need to be saved.
* SAVE MODE : Select Append, Overwrite, ErrorIfExists or Ignore.
* HEADER : Select true or false depemding on file type.

.. figure:: ../_assets/aws/configurations3_save.PNG
   :alt: S3 Workflow
   :width: 100%

Execution Result

.. figure:: ../_assets/aws/save_execution.PNG
   :alt: S3 Workflow
   :width: 100%

Once the above workflow successfully completed, the saved data can be viewed using ``DATA/AWS S3`` Location with the specified path

.. figure:: ../_assets/aws/browse_s3.PNG
   :alt: S3 Workflow
   :width: 100%
