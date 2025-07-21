File Check and Email Notification in Sparkflows Pipeline
====

This tutorial demonstrates how to build a Sparkflows pipeline that checks for a file in an S3 bucket, performs conditional branching based on the file’s presence, and triggers an EMR step to send dynamic email notifications using a reusable EmailNotification workflow.

Overview
----
  
In this use case, you will use S3Sensor, BranchPythonOperator, and EMR Steps to implement the following pipeline:

* **S3 File Check:** Check whether a specific file exists in an S3 bucket using the **S3Sensor** operator.
* **Conditional Branching:** Based on the file's existence, use **BranchPythonOperator** to execute different actions, such as sending a notification via **EMR steps**.
* **EMR Step:** Trigger an EMR step that sends an email notification, passing the subject and content of the message as parameters.


The overall flow will ensure that:

* If the file is not found in the S3 bucket, an EMR job will be triggered, which sends an email notification indicating the file’s availability.
* If the file is found in the S3 bucket, an EMR job will be triggered, which sends an email notification indicating the file’s availability, a different action can be taken (such as skipping the job or sending an alert about the missing file).

Workflow with EmailNotificationNode
----

* Create a generalised workflow with EmailNotificationNode that sends email notifications by passing the subject and content in parameters. This workflow can then be reused across various scenarios, such as when a file is available or when a file is not available. The email notification logic is encapsulated within the workflow, making it flexible for different use cases.


* In the pipeline, use EMRWorkflow with the below workflow to send the notification.

Workflow
++++

 .. figure:: ../../../_assets/tutorials/file_check/workflow.png
    :alt: File Check and Email Notification
    :width: 70%





Emailnotification node: configuration
++++

 .. figure:: ../../../_assets/tutorials/file_check/emailnotification-node-config.png
    :alt: File Check and Email Notification
    :width: 70%





Workflow parameters: subject and date_value
++++

 .. figure:: ../../../_assets/tutorials/file_check/workflow-parameters.png
    :alt: File Check and Email Notification
    :width: 70%








Pipeline with S3Sensor, Branch and AddStep
----

Pipeline
++++

 .. figure:: ../../../_assets/tutorials/file_check/pipeline.png
    :alt: File Check and Email Notification
    :width: 70%

S3 File Check
++++
Check whether a specific file exists in an S3 bucket using the **S3Sensor** operator.

 .. figure:: ../../../_assets/tutorials/file_check/s3-file-check.png
    :alt: File Check and Email Notification
    :width: 70%






Conditional Branching
++++
Based on the file's existence, use **BranchPythonOperator** to execute different actions, such as sending a file available or not available notification via EMR steps with EmailNotification workflow.

 .. figure:: ../../../_assets/tutorials/file_check/conditional-branching.png
    :alt: File Check and Email Notification
    :width: 70%





EMR Step
++++
Trigger an EMR step that sends an email notification, passing the subject and content of the message as parameters. Select the Generalized EmailNotification workflow with EmailNotificationNode. The same workflow is used for both "file found" and "file not found" scenarios by passing different parameters, as shown below.

File Found

 **subject: Data Quality File is Available**

 **date_value: {file_date_value}   //Pipeline parameter**

 .. figure:: ../../../_assets/tutorials/file_check/dataquality-file-is-available.png
    :alt: File Check and Email Notification
    :width: 70%


File Not Found

 **subject: DataQuality File Not Available** 

 **date_value: {file_date_value}   //Pipeline parameter**

 .. figure:: ../../../_assets/tutorials/file_check/dataquality-file-not-available.png
    :alt: File Check and Email Notification
    :width: 70%





PipelineParameters
++++

 .. figure:: ../../../_assets/tutorials/file_check/pipeline-parameters.png
    :alt: File Check and Email Notification
    :width: 70%





Pipeline Task Status
++++

 .. figure:: ../../../_assets/tutorials/file_check/pipeline-task-status.png
    :alt: File Check and Email Notification
    :width: 70%






EmailNotification
++++

 .. figure:: ../../../_assets/tutorials/file_check/email-notification.png
    :alt: File Check and Email Notification
    :width: 70%































