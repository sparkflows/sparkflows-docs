Data Quality
=============


Data quality is an important aspect whenever we ingest data.
Incomplete or wrong data can lead more false predictions by a machine learning algorithm, we may lose opportunities to monetize our data because of the data issues and business can lose their confidence on the data.

In sparkflows, user can create the workflow with Summary, Correlation etc nodes to get the more details about the dataset.

Sample Dataset: http://eforexcel.com/wp/downloads-16-sample-csv-files-data-sets-for-testing/

Example:

Workflow
--------

Below is the workflow to do Data Profile

* Reads data from a sample dataset.
* Correlation of the fields in dataset
* Summary of the numeric fields.


.. figure:: ../../_assets/tutorials/data-qualaity/employee-data-profiling-workflow.png
   :alt: End
   :align: center
   :width: 60%
   
   
   SampleData
   ----------
   
.. figure:: ../../_assets/tutorials/data-qualaity/employee-data-profiling-sample-data.png
   :alt: End
   :align: center
   :width: 60%
