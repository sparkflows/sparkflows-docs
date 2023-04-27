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
