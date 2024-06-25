Machine Sizing
----

Fire Insights is generally installed on a Linux vm. By default the job run on the same machine. Fire Insights can also be configured to submit the jobs to an Apache Spark Cluster. 

Below are some considerations for the sizing of the machine.
  
Scenario I
++++

Below is the default basic configuration for installing Fire Insights.

It will support 3-5 users running lightweight jobs on the same machine. If Fire Insights is configured to submit the jobs to an Apache Spark Cluster, then heavy jobs can also be run.  
  
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 16GB+
     - More memory would be preferable
   * - vCPU
     - 8+
     - More vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 500GB+
     - Depending on Job Compute, if running locally

Scenario II
++++

6-15 users 

It will support 6-15 users running lightweight jobs on the same machine. If Fire Insights is configured to submit the jobs to an Apache Spark Cluster, then heavy jobs can also be run.  
  
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 30GB+
     - More memory would be preferable
   * - vCPU
     - 16+
     - More vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 1000GB+
     - Depending on Job Compute, if running locally


Scenario III
++++

16-30 users 

It will support 16-30 users running lightweight to medium jobs on the same machine. If Fire Insights is configured to submit the jobs to an Apache Spark Cluster, then heavy jobs can also be run.  
  
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 60GB+
     - More memory would be preferable
   * - vCPU
     - 24+
     - More vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 2000GB+
     - Depending on Job Compute, if running locally

