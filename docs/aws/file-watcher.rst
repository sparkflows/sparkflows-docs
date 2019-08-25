File Watcher with AWS & Sparkflows
=================

Overview
--------

There are many use cases where we have to process the incoming files on S3. This document describes one way to achieve it with SQS, Lambda and using the REST API of Fire Insights.

Design
------

The below diagram captures the high level design:

.. figure:: ../_assets/aws/file-watcher-1.png
   :alt: File Watcher
   :align: center

Below is the flow of execution:

* New files arrives on S3
* Finally a _SUCCESS file gets written in the S3 bucket
* It triggers an event which is send to a configures SQS queue.
* Once the event reaches SQL, it triggers an AWS Lambda.
* The AWS Lambda uses the Fire Insights REST API to execute a workflow to process the new incoming files in the AWS S3 bucket.


