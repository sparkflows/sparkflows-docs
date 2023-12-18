CloudFormation Template with Embedded H2 Database
========================


Overview
--------

Using CloudFormation Templates, Fire can be easily installed on AWS. This CFT works with EMR 5.8 onwards.

Following the below steps would allow you to start up an EMR Cluster and have Fire setup on it.

The CFT does the following:

* Creates EMR cluster with 1 master node and 2 worker nodes by default.
* Once the cluster is ready it runs the job/script to deploy Fire (takes around 1-1:30 min for deploying app!).


Relevant Files
--------------

.. list-table:: 
   :widths: 15 20 40
   :header-rows: 1

   * - Title
     - Description
     - File
   * - emr-file-h2.json
     - CloudFormation Template
     - https://s3.amazonaws.com/sparkflows-cft/h2-db/emr-fire-h2.json
   * - deploy-fire-h2.sh
     - Script for deploying Fire
     - https://s3.amazonaws.com/sparkflows-cft/h2-db/deploy-fire-h2.sh
   * - script-runner.jar
     - Script Runner
     - https://s3.amazonaws.com/sparkflows-cft/h2-db/script-runner.jar
     

Ports
-----

* With this CFT and **deploy-fire-h2.sh**, when Fire comes up, it would be listening on ports 8085 and 8086.

Step 1 : Download Files and Upload to your S3 Bucket
----------------------------------------------

* Download CFT **emr-fire-h2.json** from the above link.
* Download **deploy-fire-h2.sh** and **script-runner.jar** from the above links and upload them to your s3 bucket.


Step 2 : Update CloudFormation Template based on your Environment
---------------------------------------------------------

Update the CFT **emr-fire-h2.json** according to your requirement and environment in which you are deploying.

* ElasticMapReduce-Master-SecurityGroup under mastersg::

    From AWS console -> EC2 -> Security Groups -> search for "ElasticMapReduce-master".
  
  
* ElasticMapReduce-Slave-SecurityGroup under slavesg::

    From AWS console -> EC2 -> Security Groups -> search for "ElasticMapReduce-slave".
  
  
* Applications::

    By default the CFT deploys Hadoop, Hive & Spark. Add any other Applications which you need.
  
  
* EbsRootVolumeSize::

    If required, change the root(/) ebs volume size. By default CFT has 50GB disk volume.
  
  
* SizeInGB for Master and Core Instances::

    If required, change the SizeInGB under EbsConfiguration. By default CFT has 50GB disk volume (used for hdfs).
  
  
* VolumesPerInstance for Master and Core Instances::

    If required, change the VolumesPerInstance under EbsConfiguration By default cft has 1. It means one additional disk of 50GB added to each instance(for hdfs). e.g. If you change it to 2, two 50GB (SizeInGB size) disks will be added to each instance.
  
  
* deploy-fire-h2.sh and script-runner.jar::

    Change the s3 bucket path for these two files, this s3 bucket  must be same bucket as S3Bucket. You'll pass the S3Bucket value while creating the cloudformation stack.


Step 3 : Create EMR Cluster and Deploy Fire
--------------------------------------------------

#. Navigate to **AWS web Console -> Management tools -> CloudFormation** and click on **Create Stack**.
#. On **Select Template Page**:
  
   * Select the radio-button **Upload a template to Amazon S3**.
   * Select the updated **emr-fire-h2.json** from your system.
   * Click **Next** to navigate to the **Specify Details Page**.
  
#. On **Specify Details Page**:

   * Enter the **CloudFormation stack name** and 
   * Update parameters as below where needed:

     .. list-table:: 
        :widths: 10 40
        :header-rows: 1

        * - Name of Parameter
          - Description
        * - AdditionalSecurityGroups
          - From the list, choose the additional secuirty group, it's required as default EMR security group's ports are not opened for SSH, Fire etc.
        * - AmiId
          - EMR cluster can be launched using Custom AMI, pass the value if you have a Custom AMI.
        * - ClusterName
          - Name for EMR Cluster.
        * - CoreInstanceType
          - Provide the required instance type for core nodes, default instance type is m4.xlarge.
        * - CoreNodes
          - Choose the required number of core nodes, by default it’s 2.
        * - EmrVersion
          - Choose the required EMR version, it should be above EMR v.5.8.x.
        * - Environment
          - By default dev.
        * - FireVersion
          - Enter the required version of Fire.
        * - KeyName
          - Enter the valid PEM key name to connect to EMR nodes.
        * - MasterInstanceType
          - Provide the required instance type for master nodes, default instance type is m4.xlarge.
        * - MasterNodes
          - By default, it is 1. 
        * - Owner
          - Provide the name of a team or person creating the cluster.
        * - ReleaseVersion
          - Enter the required ReleaseVersion, it has to match with fire version.
        * - S3Bucket
          - Provide the s3 bucket name, this s3 bucket should be same s3 bucket where deploy-fire-h2.sh and script-runner.jar are uploaded.
        * - Subnet
          - Provide the proper subnet name, which has sufficient resources to create EMR cluster. 
        * - TaskInstanceType
          - Optional, required only if you’re choosing TaskNodes. Provide the required instance type for task nodes, default instance type is m4.xlarge.
        * - TaskNodes
          -  Optional, required only if you want to create the cluster with tasknodes. By default zero, enter the required number of nodes.


#. Click **Next** to navigate to the **Options Page**. On this page:

   * Enter the **tag details**, if required (not mandatory).
  
#. Click **Next** to navigate to the **Review Page**. On this page:
  
   * Review all the details provided to create an EMR stack.
   * Click on **Create** to start creating the stack.

#. Next page is back to **CloudFormation Page**. On this page:

   * Choose your **Stack name**.
   * Click on **Events** to check the process.
   * Click on **Resources** to get the EMR Cluster Id.
  
   Once the stack runs successfully, your EMR cluster and Fire is ready to use. Cluster creation time depends on your EMR cluster configuration.

#. To **cross check** the Fire installation:

   * Go to **EMR** from AWS Web Console.
   * Choose your **EMR cluster**.
   * Identify the **Master Node Public DNS**. 
   * Go to **http://masternodeip:8085/index.html**
  
  
Step 4 : Connect Fire to the New Cluster
-------------------------------
#. Go to **User/Administration**.
#. Click on **Infer Hadoop Configuration**.
#. Click on the **Save** button.

Step 5 : Load Examples
--------------
#. In Fire, click on **Load Examples**.
#. **SSH** to the master node.
#. **cd /opt/fire/fire-3.1.0**
#. Upload the example data files to HDFS:

   **hadoop fs -put data**

Step 6 : Create Hadoop User
----------------------
#. Go to **Administration/User**.
#. Click on **Add User**.
#. Create a new user with username **hadoop**.
#. Log out and log back in as user **hadoop**.

Step 7 : Start Running the Examples
--------------------------

#. Go to **Applications**.
#. Start creating/using the Applications.

     
Summary
-------

Using the above CFT, you have your EMR cluster with Fire running seamlessly.
