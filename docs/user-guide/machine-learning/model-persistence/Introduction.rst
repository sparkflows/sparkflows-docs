Model Persistence - Introduction
===============

Sparkflows allows you to save the ML Model created. The ML Models can be loaded in the same or other workflows to be used for scoring. The ML Models can also be downloaded from HDFS Browse Page.

The ML models can be saved into the following locations:

* HDFS : When Sparkflows is connected to a Hadoop Cluster.

* S3 : When Sparkflows is configured and connected to AWS.

* Local Machine FileSystem : When Sparkflows is running in local mode.

In order to save onto S3, the model path can be provided as ``s3://models/priceprediction``.
