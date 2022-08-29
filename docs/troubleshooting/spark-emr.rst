
Tune the Big Data Infrastructure (Elastic Map Reduce Computes)
====

- Getting the Right Partition Size and Instance Type.

- The general principles to be followed when tuning partition for Spark application are as follows:

  - Too few partitions – Cannot utilize all cores available in the cluster.
  - Too many partitions – Excessive overhead in managing many small tasks.
  - Reasonable partitions – Helps us to utilize the cores availab
  - Avoid Key Names in Lexicographic Order
  - Use hashing / random prefixes or reverse date-times.
  
- Compression
  - If you have less than 32 GB of RAM, set the JVM flag -XX:+UseCompressedOops to make pointers be four bytes instead of eight.
  - You can add these options in spark-env.sh.
  - Compress data set to minimize bandwidth from S3 to EC2.
  - Ensure splittable compression is used or have each file be the optimal size for parallelization on the cluster
  
- Saving Files in proper formats
  - Prefer columnar file formats like Parquet for increased performance on reads.While saving
  - DataFrame into file system, set the number of records per file, df.write.option(“maxRecordsPerFile",10000).save(....)
  - Ref: http://www.gatorsmile.io/anticipated-feature-in-spark-2-2-max-records-written-per-file/
  
- Right Cluster Types
  - Persistent clusters remain alive all the time, even when a job has completed. These clusters are preferred when continuous jobs have to run on the data.
  - Since clusters take a few minutes to boot up and spin, using persistent clusters saves a significant amount of time which would otherwise be lost during the initialization process.
  - Generally, persistent clusters are preferred in testing environments. Errors in such an environment running transient clusters would close the job and might shut down the cluster, but with persistent
  - clusters jobs can continue to be submitted and modified.
  
- Right number of Executors
The ideal number of executors depends on various factors:
  — Incoming events per second, especially during peaks
  — Buffering capabilities of the streaming source
  — Maximum allowed lag, i.e. is it tolerable if the Streaming application lags behind by 3 minutes during a very high peak
  — It can be tweaked by running the streaming application in a preproduction environment and monitoring the streaming statistics in the Spark UI.
The reserved capacity depends on the aforementioned factors. The tradeoff lies between idling cluster resources versus maximum allowed lag during peaks.
  - As a general guideline:
Processing Time + Reserved Capacity <= Batch Duration

- Shuffle Memory Usage, Executor Memory-to-CPU ratio

"Stragglers" are tasks within a stage that take much longer to execute than other tasks.
In order to avoid Stragglers we need to remember:

  - Shuffle Less Often –To minimize the number of shuffles in a computation requiring several transformations, preserve partitioning across narrow transformations to avoid reshuffling data.
  - Shuffle Better - Computation cannot be completed without a shuffle sometimes. All wide transformations and all shuffles are not equally expensive or prone to failure.
  - Each core in an executor runs a single task at any one time. Hence, with 26GB per executor and 4 cores each executor, the HEAP_SIZE allocated for each task is 26G/4 or 4G.
  - However, not all the memory allocated to the executor is used for shuffle operations.

- Yarn resource allocation
  - Spark asks Yarn for the memory and cores for executing a job, so we need to ensure that Yarn itself has sufficient resources to provide to Spark.
  - In Yarn, memory in a single executor container is divided into Spark executor memory plus overhead memory (spark.yarn.executor.memoryOverhead).
  - This memory is the off-heap memory which is used for VM overheads and other native overheads.
  - If we need data locality then don’t use task nodes. Because the task nodes do not have local HDFS storage, they are effectively useless.
  - Any gains from leveraging the spot prices are likely wasted by the time lost due to poor data locality. 
  - Only use instance-backed Core nodes
  
- Auto scaling for EMR
  — Understand Amazon EMR Scale-Down Behavior
  — Configuring YARN Capacity Scheduler Queues in AWS EMR
  — Submitting a Spark Job to Different Queues help scale the Job independent of other jobs
  
  - Ref: 
    - https://mitylytics.com/2017/11/configuring-multiple-queues-aws-emr-yarn/
    - https://aws.amazon.com/blogs/big-data/best-practices-for-resizing-and-automatic-scaling-in-amazonemr/
    
- Key useful metrics YARNMemoryAvailablePercentage and ContainerPendingRatio.
  - Auto scaling policy should also specify the MaxCapacity and MinCapacity of instances.
  - EMR Auto-scaling and Spark Dynamic Allocation may not be mixed together for certain usecases for Transient Instances with pre-defined loads
  - Scale out rules:
    - Core – we auto scale on HDFS utilization. If HDFSUtilization >= 80 for 5 minutes add nodes.
    - Task – We have 3 rules related to yarn, apps pending and containers pending.
    - If YARNMemoryAvailablePercentage <= 15 add nodes
    - If AppsPending-Out >= 2 add nodes.
    - If ContainerPending-Out >= 75 add nodes.

- Auto-Scaling and Capacity Scheduler Gotchas
  - By default, EMR sets user-limit-factor in the capacity-scheduler.xml to 1. Because of this JOBS cannot be run concurrently.
  - If you change this, even with a single queue, you can run concurrent jobs. Check this value in your EMR configuration.
  - Turns out, Spark task stores its shuffle output in the local disks of the node and they are available through the external shuffle service that runs on the node manager service on every node.
  - The idea being that when an executor is completed, you can still get its output files from the node manager external shuffle service. But, with auto-scaling, these nodes get decommissioned and that output is no longer available.
  - So one then need to switch to a model of manually scaling up and scaling down as needed. Not as convenient, but it still gets the job done. Just will also need to setup some cron jobs on the master node to scale the cluster down (during a quiet period) to avoid cost run-ups.
  
- Special considerations for long-running jobs
  - Queue plays a very crucial role for long-running streaming jobs.
  - Because Spark driver and Application Master share a single JVM, any error in Spark driver stops long-running job. Fortunately it is possible to configure maximum number of attempts that will be made to re-run the application. It is reasonable to set higher value than default 2 (derived fromYARN
cluster property yarn.resourcemanager.am.max-attempts).
  - Generally 4 works quite well, higher value may cause unnecessary restarts even if the reason of the failure is permanent.
  - spark-submit --master yarn --deploy-mode cluster --conf spark.yarn.maxAppAttempts=4
    - Check if 4 attempts get exhausted in few hours for a long-running job. Then in order to avoid this situation, the attempt counter should be reset one every hour of so.
    — --conf spark.yarn.am.attemptFailuresValidityInterval=1h
      - Set maximum number of executor failures before the application fails. By default it is max(2 * num executors, 3), well suited for batch jobs but not for long-running jobs. So specify the following configuration parameters
   -  --conf spark.yarn.executor.failuresValidityInterval=1h
      --conf spark.task.maxFailures=8
  - Note without a separate YARN queue your long-running job will be preempted by a massive Hive query sooner or later.
 
- Important points regarding scaling spark-streaming jobs in EMR
  - Enabling the spark.dynamicAllocation property allows Spark to add and remove executors dynamically based on the workload.
  - When using Spark streaming ensure that the executor idle timeout is greater than the batch timeout to ensure the unused executors are removed from the cluster.
  - If the time to execute the entire job is taking longer than expected, then increase parallelism by increasing the number of cores per executor.However, more than 5 cores can lead to poor performance due to increased HDFS I/O.
  - Spark-Configuration Reference: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-sparkconfigure.
html
  - For example,
  '''
  for a 6 node r3.4xlarge cluster (5 executors per node):
  spark.executor.instances: “30"
  spark.yarn.executor.memoryOverhead: “3072"
  spark.executor.memory: “21G"
  spark.yarn.driver.memoryOverhead: “1034"
  spark.driver.memory: “6G"
  spark.executor.cores: “3"
  spark.driver.cores: “1"
  spark.default.parallelism: “180"
  spark.dynamicAllocation.enabled: “false"
  '''

  - For the YARN configurations users can cut the workload time by 50% simply by switching off this configuration:
    - spark.dynamicAllocation.enabled.
  - It basically allows the reuse of Spark executors in a multi-steps workloads.
