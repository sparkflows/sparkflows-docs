Livy
=========

1. Job Submission Issues in Livy
------
**Problem**
++++++

I do not see anything after submitting the job to Livy.

**Solution**
++++++++++

Do check in the logs for exceptions and the root cause. The log files can be analysed from Livy url.

Possible causes are:

* The Postback Url configured in Fire Insights is configured wrongly.
* The Postback Url configured in Fire Insights is not accessible from EMR Livy.

   .. figure:: ..//_assets/installation/troubleshoot/livy_1.PNG
      :alt: troubleshoot
      :width: 60%

* Test connectivity from the Apache Spark cluster to the postback URL from one of the machines of the cluster (EMR) using:

   ::

    curl https://<alb-host>/ -v
    
  .. note::  Make sure to replace 'alb-host' with your load balancer's domain name.

2. Class Not Found Exception while processing Delta File through Livy submission
------
**Problem**
++++++

ClassNotFound Exception as below:

   .. figure:: ..//_assets/installation/troubleshoot/livy-deltafile-error.png
      :alt: troubleshoot
      :width: 60%


**Solution**
++++++++++

Add Delta Jars to the Livy Connection.

Possible causes are:

* Delta Jars might be missing.
* Delta Jars might not have been added to the Livy Connection or added to a different section.

They needed to be added as below:

   .. figure:: ..//_assets/installation/troubleshoot/livy-connection-livytab-delta.png
      :alt: troubleshoot
      :width: 60%

.. note::  Make sure to add Delta Jars to the Jars section.
