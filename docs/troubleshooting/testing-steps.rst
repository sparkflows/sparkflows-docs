Testing Steps
--------------

It is a good idea to run the following steps to ensure that the environment is set up and working right.

This document captures the various steps which can be easily run to confirm the environment and settings are working good.

Check if fire-ui process is running
+++++++++

ps -ef | grep fire-ui


Check if python 3.7+ has been set up
+++++++++

python --version


Run SparkPi on the cluster
+++++++++

Run SparkPi to ensure that the Apache Spark cluster has been set up correctly.

spark-submit ...

Check if Airflow has been correctly set up
+++++++++++
