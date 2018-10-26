CloudFormation Templates
========================

Using CloudFormation Templates, Fire can be easily installed on AWS.

Overview
--------

* This CFT works with EMR 5.8 onwards.

Details
----------

The CFT does the following:

* Creates EMR cluster with 1 master node and 2 worker nodes
  * Master : m4.xlarge
  * Worker : m4.xlarge
  * AMI
* Once the cluster is ready it runs the job/script to deploy Fire (takes around 1-1:30 min for deploying app!).

CloudFormation Template
------------------------

Below is the CFT for deploying Fire::

 {
   "AWSTemplateFormatVersion": "2010-09-09",
   "Description": "Cloudformation Template to spin up EMR clusters V1 (Version 5 of EMR only)",
   "Mappings": {
     "parms": {
       "mastersg": {
         "dev": "sg-80f189f6"
       },
       "slavesg": {
         "dev": "sg-c8f088be"
       }
     }
   },
   "Parameters": {
     "AdditionalSecurityGroups": {
       "Description": "Additional Security groups",
       "Type": "List<AWS::EC2::SecurityGroup::Id>",
       "Default": "sg-d4e50aa0"
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
       "Description": "Subnet IDs",
       "Type":  "String",
       "Default": "subnet-35a03809"
     },
     "KeyName": {
       "Description": "Provide the EC2 Key name",
       "Type": "String",
       "Default": "sparkflows"
     },
     "Owner": {
       "Type": "String",
       "Default": "jayant"
     },
     "MasterNodes": {
       "Description": "No of Master nodes",
       "Type": "Number",
       "Default": 1
     },
     "CoreNodes": {
       "Description": "No of Core nodes",
       "Type": "Number",
       "Default": 1
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
         "EbsRootVolumeSize" : "10",
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
                                      "SizeInGB" : "10",
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
                                      "SizeInGB" : "10",
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




