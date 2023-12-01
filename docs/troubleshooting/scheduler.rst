Scheduler
============

This document explains some of the common issues and corresponding resolutions related to Scheduler.

1. Pipeline Trigger Delay Due to Concurrent Scheduling
------------------------

**Problem**
+++++

Scheduler takes a few minutes to trigger all the pipelines if there are too many of them trigerred at the same time.


  
**Solution**
+++++

There could be different reasons for this issue like:

* The RAM allocated to Sparkflows machine could be low.
* The **-Xmx** value set for **fire-ui** server might be low or left as default of 2.5 GB.
* The Sparkflows machine might be overloaded with some external processes running.

To address this issue: 

* For trigerring a large number of parallel scheduled jobs, ensure that the machine has enough resources i.e. RAM and Number of cores.
* Ensure that the **-Xmx** is set to a higher number for **fire-ui** server. Eg: For trigerring 200 odd jobs at the same time, the -Xmx should be higher than default. Exact allocation would depend on the overall machine specifications as well.
* Ensure that the number of threads is set to a higher number via the property **org.quartz.threadPool.threadCount=20**. This config can be found in the file **quartz.properties** in the **conf** directory.
* In addition to the above property, the following also needs to be set at optimal/higher values and not left to the default i.e. **org.quartz.scheduler.batchTriggerAcquisitionMaxCount = 20** and **org.quartz.jobStore.acquireTriggersWithinLock = true**
* More details on the configuration can be found in the official `documentation of Quartz scheduler. <http://www.quartz-scheduler.org/documentation/>`_

2. Inconsistent Execution of Airflow Pipeline
--------------------------------

**Problem**
+++++++++

Pipeline is not running consistently in Airflow.


**Solution**
+++++++++

There could be different reasons for this issue:

* The Background Event Trigger Thread is stalled.

* The Websocket doesn’t receive events in timely manner.

* Airflow DAG Execution requests are not trigerred in timely manner.

To address this issue:

- Check the Machine Configuration.

  Ensure minumum 8 cores and 16 GB RAM are used.

- Check if any additional processes (running in the same VM where Sparkflows is running) hogging the memory and processes.

  Examples of additional processes:
    
    * Agent handling the traffic between Load Balancer and installed service.
    * Any Applications (e.g. Envoy) which scans the deployed App and logs (CPU, Mem).

- Check that the DAGs in Airflow are not queued up.

  Ensure Airflow Instance is configured with enough Memory and Processing Cores.

3. Inaccurate Job Scheduling: Timing Mismatch
---------------------------------

**Problem**
++++++++

It seems that the job is running at a wrong schedule. Let's consider a typical example of misperception. The Pipeline Schedule indicates that the Job is running at say every 15th minute of the hour as opposed to 45th minute of the hour.

**Solution**
+++++

Let's assume that a Job was scheduled in IST time to run every 45th minute. But when viewed in CDT timezone it may give a wrong impression that the job is running at the 15th min of the hour. **Note that 8:45 AM IST is equivalent to 9:15 PM CDT.**

One needs to ensure that the correct Cron Expression is used for running the Job every 45th minute.

4. Failure to Trigger Pipeline: No Execution Detected
------------------

**Problem**
++++++

Pipeline is not getting trigerred at all. 

**Solution**
+++++++

* Let’s assume that the Cron Expression has been copied from an external website (e.g. http://www.cronmaker.com/) and the Job fails when one tries to run the Pipeline.

* Ensure that there is no extra space and unwanted characters in the Cron Expression.
