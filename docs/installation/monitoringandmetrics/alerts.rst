Email Alerts
=============

Configuring Alerts:
-------------------
By following below steps user can configure the email alerts for the executions in sparkflows

Login to ``Sparkflows`` application -> ``Administration`` -> ``Monitoring`` -> ``Alerts``

Once the user navigates to the alerts page, please fill in the following details to trigger the alert email

 .. figure:: ../../_assets/alerts/alert-home.png
      :alt: Alert-config
      :width: 60%

 
- Alert Enabled
- MailToUser
- FrequencyToSendAlert
- JobFailureThreshold


``Alert Enabled``  : property used to enable or disable the email alert.

``MailToUser`` : Add the receiver's email addresses in this property, separated by commas.

``FrequencyToSendAlert`` : Sparkflows will use this property to monitor execution times.
If there are no executions or an increased number of failed executions, it will send an email alert.


 .. figure:: ../../_assets/alerts/alert-no-executions.png
      :alt: alert-no-executions
      :width: 60%


``JobFailureThreshold`` : This property is used to monitor the execution failure rate within a specified time limit(FrequencyToSendAlert).
If the failure rate exceeds the configured threshold (e.g., 50%), an email alert will be triggered and sent to the user.


 .. figure:: ../../_assets/alerts/alert-execution-exceeds-failure.png
      :alt: alert-execution-exceeds-failure
      :width: 60%

.. note:: 

 ``FrequencyToSendAlert``
 For example, if the Alert Frequency is set to 5 minutes, the Sparkflows scheduler will check if any workflow/pipeline has executed within the last 5 minutes. If no executions have occurred during this period, it will trigger an alert email notification.
 
 ``JobFailureThreshold``
 For example, if the user schedules the workflow/pipeline to run every minute and sets the Alert Frequency to 5 minutes, the workflow/pipeline will execute 5 times within that period. The Sparkflows scheduler then calculates the Job Failure Threshold, say 50%. If all 5 executions fail, resulting in a 100% failure rate—exceeding the 50% threshold—the system will trigger an alert email notification.
