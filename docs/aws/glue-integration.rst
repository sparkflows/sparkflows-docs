Glue Integration
================

Fire Insights can be configured to submit jobs to the AWS Glue cluster.


Architecture diagram
----------

.. figure:: ..//_assets/aws/glue/architecture.png
   :alt: aws
   :width: 60%

Below are the steps for AWS Glue Network Connection to call Fire Insights APIs in Aws Glue Jobs.

Configuration
-------------

In Administration/Configuration/AWS Glue configure the following parameters:

* Glue URL


Network Configuration
------------------

The following Network Configuration are needed.


Execution
---------

Now when workflows are executed in Fire Insights, they submit the jobs onto AWS Glue. The results are displayed back in Fire Insights.

