Testing Fire Insights on AWS
----------------------------

After you have deployed Fire Insights on AWS, it is a good idea to test the things.

Below are a few good steps for achieving it:

* Ensure you can log into the sytem
* View the Sample Applications
* Execute a workflow on EMR

Log into the System
-------------------

* Log into the system as the ``hadoop`` user which you had created during the Deployment process.
  * http://docs.sparkflows.io/en/latest/aws/running-on-emr.html

View the Sample Applications
----------------------------

* Go to the ``Applications/List' page.
* If you loaded the Sample Applications during the deployment process you would see a number of Sample Applications listed.
* Click on any of them to view their Datasets/Workflows etc.

Execute a workflow on EMR
------------------

* From the Applications/Workflows page.
* Click on the Execute icon next to any workflow
* This will open up the Execute page.
* Click on ``Execute`` to execute the workflow on the EMR cluster
* The results of execution would get displayed on the page.
