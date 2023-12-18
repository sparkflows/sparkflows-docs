File Watcher with AWS and Sparkflows
=================

Overview
--------

Processing files pushed to S3 is a common requirement in various use cases. To efficiently handle this task, the combination of SQS (Simple Queue Service) and Lambda can be utilized. By configuring a Lambda function as a trigger for an SQS queue, you can automate the processing of messages within the queue. 

In this document, we will explore a method to achieve this using SQS, Lambda, and leveraging the REST API of Fire Insights. This approach provides a seamless and effective solution for processing files stored in S3.

Follow the steps given below:

Design
------

The diagram given below captures the high level design:

   .. figure:: ../../_assets/aws/file-watcher-1.png
      :alt: File Watcher
      :width: 55%


Below is the flow of execution:

#. New files arrives in the S3 directory location: **/sparklows-file-watcher/raw-data/iot/2019-08-2201**

   * In the above design, the raw data arrives in the directory: **/sparklows-file-watcher/raw-data**
   * There are various types of raw data which can be expected.
   * IOT is one type of raw data. Each day, we receive a number of IOT files in the folder: **/sparklows-file-watcher/raw-data/iot/yyyy-MM-dd**
   * Once all the files for the date are written to the appropriate folder, **a _SUCCESS** file is written into it.

#. The availability of _SUCCESS file triggers an event which is sent to a configured SQS queue.
#. Once the event reaches SQS, it triggers an AWS Lambda.
#. The AWS Lambda uses the Fire Insights REST API to execute a workflow to process the new incoming files in the AWS S3 bucket.
#. If AWS Lambda fails, it sends the event to DLQ (Dead Letter Queue) to be appropriately handled.


Step 1 : Create an SQS Queue
-------------------

Create an SQS Queue to receive the events from S3 and to trigger the AWS Lambda function.

Below, we see the SQS queue : **sf-workflow-file-watcher-ql-dev**

It has the premissions as shown below to receive the messages from S3 bucket and to invoke the AWS Lambda function.

   .. figure:: ../../_assets/aws/file-watcher-sqs-queue-1.png
      :alt: SQS Queue
      :width: 65%
      


   .. figure:: ../../_assets/aws/file-watcher-sqs-queue-2.png
      :alt: SQS Queue
      :width: 65% 
    

Step 2 : Configure AWS S3 bucket to generate events
------------------------------------------

Configure the AWS S3 bucket to send events for the new files received into AWS SQS queue.

Then, it looks for the new files with prefix of **events** with the suffix **_SUCCESS**. 

It sends these events to **sf-workflow-file-watcher-ql-dev** SQS Queue.

   .. figure:: ../../_assets/aws/file-watcher-s3-events.png
      :alt: S3 Events
      :width: 40%
     
   
   
Step 3 : Create the AWS Lambda function
------------------------------

Create the AWS Lambda function to take the SQL Event and begin the workflow in Fire Insights. This workflow would process the newly arrived files.

Firstly, create an IAM role. An example is shown below.

We add 3 Environment variables as shown below. These are used by the Lambda functions in this example.

  * SPARKFLOWS_TOKEN or KMS_ARN
  * SPARKFLOWS_URL
  * WORKFLOW_ID

Instead of the Sparkflows token, users can encrypt the token using KMS and use the KMS ARN as the Environment variable and decrypt the token using KMS inside the Lamdba.

   
   .. figure:: ../../_assets/aws/file-watcher-lambda-2.png
      :alt: AWS Lambda
      :width: 65%


Upload the JAR file for the RequestHandler. It can also be placed into S3 location and the Lambda configured for it.

WorkflowExecuteHandler
++++++++++++++++++++++

::

   package com.sf.handler

   import com.amazonaws.services.lambda.runtime.events.SQSEvent
   import com.amazonaws.services.lambda.runtime.events.SQSEvent.SQSMessage
   import com.amazonaws.services.lambda.runtime.{Context, LambdaLogger, RequestHandler}
   import com.amazonaws.services.s3.event.S3EventNotification
   import com.amazonaws.services.s3.event.S3EventNotification.S3EventNotificationRecord
   import com.sf.WorkflowExecute

   import scala.collection.JavaConverters._

   class WorkflowExecuteHandler extends  RequestHandler[SQSEvent, Unit] {

     private val token = System.getenv("SPARKFLOWS_TOKEN")
     private val sparkflowsURL = System.getenv("SPARKFLOWS_URL")
     private val workflowId = System.getenv("WORKFLOW_ID")

     def handleRequest(sqsEvent: SQSEvent, context: Context): Unit = {

       implicit val logger: LambdaLogger = context.getLogger

       logger.log(s"sparkflowsURL: $sparkflowsURL")
       logger.log(s"workflowId: $workflowId")

       sqsEvent
         .getRecords
         .asScala.map(sqsMessageToS3Event)
         .foreach(_.getRecords.asScala.foreach(processS3Record))
     }

     private[handler] def sqsMessageToS3Event(sqsMessage: SQSMessage): S3EventNotification = {
       S3EventNotification.parseJson(sqsMessage.getBody)
     }

     private[handler] def processS3Record(s3EventRecord: S3EventNotificationRecord)
                                         (implicit logger: LambdaLogger): Unit = {

       val s3Entity = s3EventRecord.getS3
       val inputBucketName: String = s3Entity.getBucket.getName
       val inputObjectKey: String = s3Entity.getObject.getUrlDecodedKey
       val eventName: String = s3EventRecord.getEventName
       val path = s"s3://$inputBucketName/$inputObjectKey".replace("/_SUCCESS", "")

       logger.log(s"Event record $eventName; path $path")

       val body = s"""
                     |{
                     |  "workflowId": "${workflowId}",
                     |  "parameters": "--var datapath=${path}"
                     |}
          """.stripMargin

        val workflowStatus = WorkflowExecute.executeWorkflow(body, token, sparkflowsURL)

        logger.log(s"Status of workflow $workflowStatus")
     }
   }


WorkflowExecute
+++++++++++++++

::

   package com.sf

   import com.mashape.unirest.http.Unirest

   object WorkflowExecute {

     def executeWorkflow(body: String, token: String, sparkflowsHostName: String) = {

       val workflow = Unirest.post(s"$sparkflowsHostName/api/v1/workflow/execute")
         .header("Content-Type", "application/json")
         .header("Cache-Control", "no-cache")
         .header("Authorization", s"Bearer $token")
         .body(body)
         .asString

       workflow match {
         case s if workflow.getStatus >= 200 && workflow.getStatus <= 300 => workflow.getBody
         case f => throw SubmissionFailedException(s"Job submissions failed, status code is ${f.getStatus}")
       }
     }
     case class SubmissionFailedException(message:String) extends Exception(message)
   }
