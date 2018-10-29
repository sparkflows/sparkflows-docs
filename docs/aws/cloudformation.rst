CloudFormation Templates
========================

Using CloudFormation Templates, Fire can be easily installed on AWS.

Overview
--------

* This CFT works with EMR 5.8 onwards.

Relevant Files
--------------

* https://s3.amazonaws.com/sparkflows-release/fire/CFT/emr-fire.json
* https://s3.amazonaws.com/sparkflows-release/fire/CFT/fire.sh
* https://s3.amazonaws.com/sparkflows-release/fire/CFT/script-runner.jar

Details
----------

The CFT does the following:

* Creates EMR cluster with 1 master node and 2 worker nodes by default.
* Once the cluster is ready it runs the job/script to deploy Fire (takes around 1-1:30 min for deploying app!).

Download relevant files
-----------------------

* Download CFT emr-fire.json from the above link or use the below CloudFormation Template.
* Download fire.sh and script-runner.jar from the above link and upload it to your s3 bucket

Update Cloudformation templates based on your environment
---------------------------------------------------------

* Modify Cloudformation template (emr-fire.json) according to your requirement and deploying environment

 * Update the CFT for ElasticMapReduce-Master-SecurityGroup under mastersg - From AWS console -> EC2 -> Security Groups -> 'search for "ElasticMapReduce-master"'
 * Update the CFT for ElasticMapReduce-Slave-SecurityGroup under slavesg - From AWS console -> EC2 -> Security Groups -> 'search for "ElasticMapReduce-slave"'
 * Update the CFT for Applications - By default CFT deploy with Hadoop, Hive & Spark, add the other required Applications.
 * Update the CFT for EbsRootVolumeSize - If required change the root(/) ebs volume size, by default cft has 50GB disk volume
 * Update the CFT for SizeInGB for Master and Core Instances - If required change the SizeInGB under EbsConfiguration, by default cft has 50GB disk volume (used for hdfs)
 * Update the CFT for VolumesPerInstance for Master and Core Instances - If required change the VolumesPerInstance under EbsConfiguration, by default cft has 1. It means one additional disk of 50GB added to each instance(for hdfs). e.g. If you change it 2, two 50GB (SizeInGB size) disks will be added to each instances.
 * Update the CFT for fire.sh and script-runner.jar - Change the s3 bucket path for these two files, this s3 bucket  must be same bucket as S3Bucket. You'll pass the S3Bucket value while creating the cloudformation stack.

Steps to Create EMR Cluster and Deploy the Fire
--------------------------------------------------
* AWS web Console -> Management tools -> CloudFormation -> Create Stack -> Upload a template to Amazon S3 (Select the updated emr-fire.json from your system) -> Provide all the required details
 * Stack name - CloudFormation stack name
 * Parameters
  * AdditionalSecurityGroups - From the list choose the additional secuirty group(sg), it's required because default emr sg's ports are not opened for ssh, fire & etc...
  * AmiId - EMR cluster can be launched using Custom AMI, pass the value if you have a Custom AMI
  * ClusterName - Name for EMR Cluster
  * CoreInstanceType - Provide the required instance type for core nodes, default instance type is m4.xlarge
  * CoreNodes - Choose the required number of core nodes, by default it's 2
  * EmrVersion - Choose the required EMR version, it's should be above EMR v.5.8.x 
  * Environment - By default dev
  * FireVersion - Enter the required version of Fire
  * KeyName - Enter the valid pem key name to connect to emr nodes
  * MasterInstanceType - Provide the required instance type for master nodes, default instance type is m4.xlarge
  * MasterNodes - By default 1
  * Owner - provide the name of a team or person creating the cluster
  * ReleaseVersion - Enter the required ReleaseVersion, it has to match with fire version
  * S3Bucket - Provide the s3 bucket name, this s3 bucket should be same s3 bucket where fire.sh and script-runner.jar are uploaded
  * Subnet - Provide the proper subnet name, which as sufficient resources to create emr cluster
  * TaskInstanceType - Optional, required only if you're choosing TaskNodes. Provide the required instance type for task nodes, default instance type is m4.xlarge
  * TaskNodes - Optional, required only if you want to create the cluster with tasknodes.By default zero, enter the required number of nodes
*  Validate all the provided vaules, click next -> if required (not mandatory) enter tag details for cloudformation tag, click next -> one more time cross check for all the details provided to create a emr stack, then click on create
* Come back to cloudformation, choose your stack name and click on events to check the process and click on Resources to get the EMR Cluster id
* Once the stack runs successfully, you're EMR Cluster and Fire is ready to use. Cluster creation time depends on your EMR cluster configuration
 * To cross check the fire installation, go to EMR from AWS web console -> choose the your emr cluster -> Steps -> choose the job, click on the view logs or http://masternodeip:8085/index.html
  
CloudFormation Template
------------------------

Below is the CFT for deploying Fire::

 {
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "Cloudformation Template to spin up EMR clusters V1 (Version 5 of EMR only)",
   "Mappings": {
     "parms": {
       "mastersg": {
         "dev": "ElasticMapReduce-Master-Private-SecurityGroup"
       },
       "slavesg": {
         "dev": "ElasticMapReduce-Slave-Private-SecurityGroup"
       }
     }
   },
   "Parameters": {
     "AdditionalSecurityGroups": {
       "Description": "Additional Security groups",
       "Type": "List<AWS::EC2::SecurityGroup::Id>"
     },
     "S3Bucket": {
       "Description": "Application s3_Bucket",
       "Type": "String",
       "Default": "sparkflows-release"
     },
     "ClusterName": {
       "Description": "Name of the cluster",
       "Type": "String"
     },
     "EmrVersion": {
       "Type": "String",
       "Description": "Must be EMR Version 5 (i.e: emr-5.8.0)",
       "Default": "emr-5.10.0"
     },
     "MasterInstanceType": {
       "Description": "Instance type of Master Node",
       "Type": "String",
       "Default": "m4.xlarge"
     },
     "CoreInstanceType": {
       "Description": "Instance type of Core Node",
       "Type": "String",
       "Default": "m4.xlarge"
     },
     "TaskInstanceType": {
       "Description": "Instance type of Core Node",
       "Type": "String",
       "Default": "m4.xlarge"
     },
     "ReleaseVersion": {
       "Type": "String",
       "Description": "Must be ReleaseVersion Version (i.e: rel-3.1.0)",
       "Default": "rel-3.1.0"
     },
     "FireVersion": {
       "Type": "String",
       "Description": "Must be FireVersion Version (i.e: fire-3.1.0)",
       "Default": "fire-3.1.0"
     },
     "TerminationProtected": {
       "Description": "Is the cluster to have termination protection enabled",
       "Type": "String",
       "AllowedValues": [
         "true",
         "false"
       ],
       "ConstraintDescription": "Boolean",
       "Default": "false"
     },
     "Environment": {
       "Description": "Environment type",
       "Type": "String",
       "AllowedValues": [
         "dev"
       ],
       "Default": "dev"
     },
     "AmiId": {
       "Description": "Provide the latest EMR ami",
       "Type": "String"
     },
     "Subnet": {
       "Description": "Subnet ID",
       "Type":  "String",
       "Default": "subnet-"
     },
     "KeyName": {
       "Description": "Provide the EC2 Key name",
       "Type": "String",
       "Default": "key name"
     },
     "Owner": {
       "Type": "String",
       "Default": "Owner name"
     },
     "MasterNodes": {
       "Description": "No of Master nodes",
       "Type": "Number",
       "Default": 1
     },
     "CoreNodes": {
       "Description": "No of Core nodes",
       "Type": "Number",
       "Default": 2
     },
     "TaskNodes": {
       "Description": "No of TaskNodes if required",
       "Type": "Number",
       "Default": 0
     }
   },
   "Resources": {
     "EMRClusterV5Metastore": {
       "Type": "AWS::EMR::Cluster",
       "Properties": {
         "Applications": [
           { "Name": "Hadoop" },
           { "Name": "Hive" },
           { "Name": "Spark" }
         ],
         "CustomAmiId" : { "Ref": "AmiId" },
         "EbsRootVolumeSize" : "50",
         "AutoScalingRole": "EMR_AutoScaling_DefaultRole",
         "Instances": {
           "AdditionalMasterSecurityGroups": {
             "Ref": "AdditionalSecurityGroups"
           },
           "AdditionalSlaveSecurityGroups": {
             "Ref": "AdditionalSecurityGroups"
           },
           "CoreInstanceGroup": {
             "EbsConfiguration"  : {
                    "EbsBlockDeviceConfigs" : [{
                              "VolumeSpecification" : {
                                      "SizeInGB" : "50",
                                      "VolumeType" : "gp2"
                              },
                               "VolumesPerInstance" : "1"
                     }],
                     "EbsOptimized" : "true"
             },
             "InstanceCount": {
               "Ref": "CoreNodes"
             },
             "InstanceType": {
               "Ref": "CoreInstanceType"
             },
             "Market": "ON_DEMAND",
             "Name": "Core instance group - 2"
           },
           "Ec2KeyName": {
             "Ref": "KeyName" },
           "Ec2SubnetId": {
             "Ref": "Subnet" },
           "EmrManagedMasterSecurityGroup": {
             "Fn::FindInMap": [ "parms", "mastersg", { "Ref": "Environment" } ]
           },
           "EmrManagedSlaveSecurityGroup": {
             "Fn::FindInMap": [ "parms", "slavesg", { "Ref": "Environment" } ]
           },
           "MasterInstanceGroup": {
             "EbsConfiguration"  : {
                     "EbsBlockDeviceConfigs" : [{
                              "VolumeSpecification" : {
                                      "SizeInGB" : "50",
                                     "VolumeType" : "gp2"
                              },
                              "VolumesPerInstance" : "1"
                                    }],
                     "EbsOptimized" : "true"
             },
             "InstanceCount": {
               "Ref": "MasterNodes"
             },
             "InstanceType": {
               "Ref": "MasterInstanceType"
             },
             "Market": "ON_DEMAND",
             "Name": "Master instance group - 1"
           },
           "TerminationProtected": {
             "Ref": "TerminationProtected"
           }
         },
         "JobFlowRole": "EMR_EC2_DefaultRole",
         "LogUri": {
           "Fn::Join": [ "", [ "s3n://", { "Ref": "S3Bucket" }, "/emr/logs/" ] ]
         },
         "Name": { "Fn::Join": [ "", [ { "Ref": "ClusterName" }, "-", { "Ref": "Environment"} ] ] },
         "ReleaseLabel": {
           "Ref": "EmrVersion"
         },
         "ServiceRole": "EMR_DefaultRole",
         "Tags": [
           { "Key": "Name", "Value": { "Fn::Join": [ "", [ "emr-instance-", { "Ref": "AWS::StackName" }, "" ] ] } },
           { "Key": "OwnerContact", "Value": { "Ref": "Owner" } }
         ],
         "VisibleToAllUsers": true
       }
     },
     "EMRTaskNodes": {
       "Type": "AWS::EMR::InstanceGroupConfig",
       "Properties": {
         "InstanceCount": {
           "Ref": "TaskNodes"
         },
         "InstanceRole": "TASK",
         "InstanceType": {
           "Ref": "TaskInstanceType"
         },
         "JobFlowId": {
           "Ref": "EMRClusterV5Metastore"
         }
       }
     },
     "setupsparkflows": {
       "Type": "AWS::EMR::Step",
       "Properties": {
         "ActionOnFailure": "CONTINUE",
         "HadoopJarStep": {
           "Jar": {
             "Fn::Join": [ "", [ "s3://", { "Ref": "S3Bucket" }, "/fire/CFT/script-runner.jar" ] ]
           },
           "Args": [
             { "Fn::Join": [ "", [ "s3://", { "Ref": "S3Bucket" }, "/fire/CFT/fire.sh" ] ] },
             { "Ref": "ReleaseVersion" },
             { "Ref": "FireVersion" }
           ]
         },
         "Name": "setupsparkflows",
         "JobFlowId": {
           "Ref": "EMRClusterV5Metastore"
         }
       }
     }
   }
 }


Summary
-------

Using the above CFT you have have your EMR cluster with Fire running immediately.
