Writing to S3 files
=========================

https://docs.databricks.com/_static/notebooks/data-import/s3.html

Fire Insighs workflows can write data to S3 locations.

Below is an example workflow which writes data to S3. When the workflow is executed, the Dataframe is saved to the S3 location.

In the dailog box of the save CSV processor the path is specified as ``s3a://sparkflow-sample-data/write/``

.. figure:: ../../_assets/aws/csvsave-workflow.PNG
   :alt: S3 Workflow
   :align: center

Browse S3 specified Path & other parameter for processor SaveCSV 

.. figure:: ../../_assets/aws/configuration-csvs3.PNG
   :alt: S3 Workflow
   :align: center

Execution Result

.. figure:: ../../_assets/aws/saveexecution.PNG
   :alt: S3 Workflow
   :align: center

Once the above workflow successfully completed, the save data can be viewed using ``DATABROWSERS/AWS S3`` Location with specified path

.. figure:: ../../_assets/aws/browses3.PNG
   :alt: S3 Workflow
   :align: center  
