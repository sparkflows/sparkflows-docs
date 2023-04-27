Scheduler
============

This document explains some of the common issues and corresponding resolutions:

1. Scheduler takes a few minutes to trigger all the pipelines if there are too many of them trigerred at the same time
----------------------------------------------------------------------------------------------------------------------

**Issue Description**

There could be different reasons for this issue.

* The RAM allocated to Sparkflows machine could be low
* The ``-Xmx`` value set for ``fire-ui`` server might be low or left as default of 2.5 GB
* The Sparkflows machine might be overloaded with some external processes running
  
**Resolution**


* For trigerring a large number of parallel scheduled jobs, ensure that machine has enough resources - RAM and Number of cores.
* Ensure that the ``-Xmx`` is set to a higher number for ``fire-ui`` server. Eg: For trigerring 200 odd jobs at the same time, the -Xmx should be higher than default. Exact allocation would depend on the overall machine specifications as well.
* Ensure that the number of threads is set to a higher number via the property ``org.quartz.threadPool.threadCount=20``. This config can be found in the file ``quartz.properties`` in the ``conf`` directory.
* In addition to the above property, the following also needs to be set at optimal/higher values and not left to default ``org.quartz.scheduler.batchTriggerAcquisitionMaxCount = 20`` and ``org.quartz.jobStore.acquireTriggersWithinLock = true``
* More on the configurations can be found in the official documentatin of Quartz scheduler - http://www.quartz-scheduler.org/documentation/

2. Pipeline is not running consistently in Airflow
----------------------------------------------------------------------------------------------------------------------

**Issue Description**

There could be different reasons for this issue.

The Background Event Trigger Thread is stalled.

The Websocket doesn’t receive events in timely manner.

Airflow DAG Execution requests are not trigerred in timely manner.

**Resolution**

- Check the Machine Configuration.

Ensure minumum 8 cores and 16 GB RAM are used.

- Check if any additional processes (running in the same VM where Sparkflows is running) hogging the memory and processes.

Examples of additional processes:
Agent handling the traffic between Load Balancer and installed service.

any Applications (e.g. Envoy) which scans the deployed App and logs (CPU, Mem).

- Check DAGs in Airflow are not queued up.

Ensure Airflow Instance is configured with enough Memory and Processing Cores.

3. It seems job is running at a wrong schedule
----------------------------------------------------------------------------------------------------------------------

**Issue Description**

Lets conside a typical example of misperception. The Piopeline Schedule is showing that Job is running at say every 15th minute of the hour as opposed to 45th min of the hour

**Resolution**

Let’s assume a Job was scheduled in IST time to run every 45th minute. But when viewed in CDT timezone it may give a wrong impression that the job is running at the 15th min of the hour. Note: 8:45 am IST is 9:15 pm CDT

One need to ensure correct cron expression is used for running the job every 45th min.

4. Pipeline is not getting trigerred at all
----------------------------------------------------------------------------------------------------------------------

**Issue Description**

Let’s assume the Cron Expression has been copied from external website like http://www.cronmaker.com/. Then one tries to run the Pipeline and the job fails.

**Resolution**

Ensure that there is no extra space and unwanted characters in the Cron Expression.
