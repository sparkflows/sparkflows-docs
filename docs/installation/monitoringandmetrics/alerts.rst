Email Alerts
=============

Configuring Alerts:
-------------------
By following below steps user can configure the email alerts for the executions in sparkflows

Login to ``Sparkflows`` application -> ``Administration`` -> ``Monitoring`` -> ``Alerts``

Once the user navigates to the alerts page, please fill in the following details to trigger the alert email

 - Alert Enabled
 - MailToUser
 - FrequencyToSendAlert
 - JobFailureThreshold


``Alert Enabled``  : property used to enable or disable the email alert.

``MailToUser`` : Add the receiver's email addresses in this property, separated by commas.

``FrequencyToSendAlert`` : Sparkflows will use this property to monitor execution times.

  If there are no executions or an increased number of failed executions, it will send an email alert.

``JobFailureThreshold`` : This property is used to monitor the execution failure rate within a specified time limit(FrequencyToSendAlert).

  If the failure rate exceeds the configured threshold (e.g., 50%), an email alert will be triggered and sent to the user.
