Triggering Workflows by Event
==============================

Workflow Executions can be triggered by sending an event to a Kafka Topic.

Fire can be configured to poll for events from those topics.

Use Case
--------

The kind of use cases this can handle are:

* A Job loads data into HIVE
* Now the Job wants to trigger another workflow
* It pushes an event to a Kafka Topic to trigger the workflow

Event Format
-----------

Fields in the Event are | (pipe) separated.

Below is the format of the event.

* Type|Value|spark submit configs|jarfiles|programparameters|emailOnSuccess|emailOnFailure

* Type : Type determines the kind of data in the seconds column

  * 0 : workflow id
  * 1 : workflow name
  * 2 : workflow uuid

* Value : This defines value. Values are based on the Type used:

  * ID of the workflow
  * Name of the workflow
  * UUID of the workflow
  
* Spark Submit Configs : extra Spark Submit configurations to be applied when running the Spark Job.
* Program parameters : extra program parameters if any
  * Program Parameters are passed to the workflow. An example is ‘--var key1=value1’.
* Email on Success : email addresses to send Success email on Job Completion.
* Email on Failure : email addresses to send Failure email on Job Failure.


Example Events
--------------

* 0|5| | | |success@sparkflows.io|failure@sparkflows.io

In the above example:

  * 0 : Trigger by workflow id
  * 5 : Workflow id to trigger
  * success@sparkflows.io : Email address to send regarding success of the workflow
  * failure@sparkflows.io : Email address to send regarding failure of the workflow
  


