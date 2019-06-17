Operational Guidance
=================

This document describes details for operating Sparkflows when running on AWS.

Onboarding New Users
--------

New users can be created in Sparklows by logging into it. Then go to Administration/Users.

Health Check
-----

The main server process which handles the web requests is fire-ui. This is a long running process and very stable. This process can be checked for responsiveness for any health checks.

Backup and Recovery
------

EMR cluster normally start with a mimumum of 1 master node and 2 worker nodes. 

We recommend using at least 16GB machines for the master and worker nodes.

As your data volume and the number of concurrent users increases, we recommend increasing the size of the EMR cluster. Memory can be increased to 32GB to 64GB to 512GB. Since Apache Spark has the ability to use as much memory you provide, its a good idea to give it more memory.

Same for the number of disks and vcores.
