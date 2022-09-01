Testing Fire Insights on AWS
============================

This document describes how to test if Fire Insights is running on AWS.

Below are the overall steps:

1. Ensure you can log into the system
2. View the Sample Applications
3. Execute a workflow on EMR

Log into the System
-------------------

* Log into the system as the ``hadoop`` user which you had created during the Deployment process.
  * http://docs.sparkflows.io/en/latest/aws/running-on-emr.html

View the Sample Applications
----------------------------

* Go to the ``Applications/List' page.
* If you loaded the Sample Applications during the deployment process you would see some Sample Applications listed.
* Click on any of them to view their Datasets/Workflows etc.

Execute a workflow on EMR
------------------

* From the Applications/Workflows page.
* Click on the Execute icon next to any workflow
* This will open up the Execute page.
* Click on ``Execute`` to execute the workflow on the EMR cluster
* The results of execution would get displayed on the page.
