Planning Guidance
=================

This document describes details for helping you plan on deploying and using Fire Insights on AWS.

Security
--------

Fire Insights is installed onto the edge node or master node of the EMR cluster. The jobs fired by the users would be able to access and process data on S3, HDFS, Redshift, Kinesis.

Costs
-----

The main costs involved when using Fire Insights are around the EMR cluster. EMR cluster has master nodes and workflow nodes.

Pricing for EMR can be found here : https://aws.amazon.com/emr/pricing/

The more processing capacity needed, the larger should be the size of the EMR cluster.

Fire Insights can also run Machine Learning Modeling jobs onto SageMaker. If this is used, there would be cost associated with using AWS SageMaker. Amazon SageMaker Pricing details are here : https://aws.amazon.com/sagemaker/pricing/


Sizing
------

EMR cluster normally start with a mimumum of 1 master node and 2 worker nodes. 

We recommend using at least 16GB machines for the master and workder nodes.

As your data volume and the number of concurrent users increases, we recommend increasing the size of the EMR cluster.
