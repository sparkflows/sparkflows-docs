Write to S3
=========================

Fire Insights workflows can write data to S3 locations using Save CSV processor. To get detailed information, read `Databricks Documentation. <https://docs.databricks.com/_static/notebooks/data-import/s3.html>`_

Workflow
--------
Below is an example workflow that writes data to S3. When the workflow is executed, the DataFrame is saved to the S3 location.

  .. figure:: ../../_assets/aws/workflow_csvs3.PNG
     :alt: S3 Workflow
     :width: 60%

Processor Configuration
------------
In the configuration window of the **Save CSV** processor, the path is specified as: **s3a://fire-sample-data/write/**.

Browse S3 specified Path & other parameters for processor **SaveCSV** as given below:

* PATH : Click on **BROWSE S3** and specify the path where file is required to be saved.
* SAVE MODE : Select Append, Overwrite, ErrorIfExists, or Ignore.
* HEADER : Select true or false depending on the file type.

  .. figure:: ../../_assets/aws/configurations3_save.PNG
     :alt: S3 Workflow 
     :width: 60%

Execution Result
--------

  .. figure:: ../../_assets/aws/save_execution.PNG
     :alt: S3 Workflow
     :width: 60%

Access Data
---------
Once the above workflow  gets successfully completed, the data saved can be viewed using **DATA/AWS S3** location with the specified path.

  .. figure:: ../../_assets/aws/browse_s3.PNG
     :alt: S3 Workflow
     :width: 60%
