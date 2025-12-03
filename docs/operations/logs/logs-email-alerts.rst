Log Format for Email Alerts
=====
This document outlines the standard log formats used for email alerts across different sections in Sparkflows.

Standard Format for Email
----
Below is the standard log format used when an email is triggered during various executions in Sparkflows.

::

    [EMAIL_SEND] status= emailType= recipient= message="some useful message"

**Log Examples**
+++++++++++++++++++++++

**1. Log Entry for Email triggered on executing workflow: Success / Failed (Scala and PySpark)**

  .. figure:: ../../_assets/configuration/logs/logs-email-wf-execution.PNG
      :alt: Logs
      :width: 70%

**2. Log Entry for Email triggered when scheduled workflow runs**

  .. figure:: ../../_assets/configuration/logs/logs-email-wf-scheduler.PNG
     :alt: Logs
     :width: 70%

**3. Log Entry for Email triggered from Email Node within a workflow**

  .. figure:: ../../_assets/configuration/logs/logs-email-node-email.PNG
     :alt: Logs
     :width: 70%

**4. Log Entry for Email triggered on executing pipeline: Success / Failed**

  .. figure:: ../../_assets/configuration/logs/logs-email-pipeline-execution.PNG
     :alt: Logs
     :width: 70%

**5. Log Entry for Email triggered on scheduled pipeline runs**

  .. figure:: ../../_assets/configuration/logs/logs-email-pipeline-scheduler.PNG
     :alt: Logs
     :width: 70%

**6. Log Entry for Email triggered when Data Quality rules are evaluated**

  .. figure:: ../../_assets/configuration/logs/logs-email-data-quality.PNG
     :alt: Logs
     :width: 70%















