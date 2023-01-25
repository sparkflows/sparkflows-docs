Postback Url 
=========

I do not see anything after submitting the job to Emr Livy
------------------------------------------------------------

Do check in the logs for exceptions and the root cause. The log files can be analysed from Livy url.

Possible causes are:

* The Postback Url configured in Fire Insights is configured wrongly.
* The Postback Url configured in Fire Insights is not accessible from EMR Livy.

.. figure:: ..//_assets/installation/troubleshoot/livy_1.PNG
   :alt: troubleshoot
   :width: 60%

* Test connectivity of EMR to ALB host via curl command from EMR Machine::

    curl https://<alb-host>/ -v
    
.. note::  Make sure to change the alb-host to your domain name of load balancer.    

