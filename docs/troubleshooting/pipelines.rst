Pipelines
============

This document explains some of the common issues and corresponding resolutions:

1. Pipelines not getting trigerred in Airflow in deterministic manner
------------------------------------------------------------

**Issue Description**

There could be different types of issues observed.

* The Background Event Trigger Thread is stalled
* The Websocket doesn't receive events in timely manner
* Airflow DAG Execution requests are not trigerred in timely manner
  
**Resolution**

Check the Machine Configuration.

* Ensure minumum 8 cores and 16 GB RAM are used.
* Check if any additional processes (running in the same VM where Sparkflows is running) hogging the memory and processes.

  Examples of additional processes: 
    * Agent handling the traffic between Load Balancer and installed service, 
    * any Applications (e.g. Envoy) which scans the deployed App and logs (CPU, Mem)  

* Check DAGs in Airflow are not queued up
* Ensure Airflow Instance is configured with enough Memory and Processing Cores. 
