Fire Insights Deployment on ECS Fargate
=======================================

Fire Insights can be deployed on ECS Fargate. This document explains the steps required to configure the task, service, application load balancer and task groups to run Fire Insights on ECS Fargate.

Below are the steps:

Step 1 : Pre-requisite Check
--------

Ensure that you have an AWS account with the necessary access to resources before proceeding with the deployment.


Step 2 : Create ECS Cluster
----------

Create the ECS cluster wih VPC and security group. Note that any pre-existing ECS cluster can also be used for deployment.

  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-cluster.png
     :alt: aws
     :width: 60%


Step 3 : Define Task
--------------
To create the task, attach the **ecsTaskExecutionRole** with all the policies and image name.

Add the ENV variable to use external MySQL otherwise the task will create and use the H2 database, by default. 

Also, an external database is mandatory when multiple replicas of the same task are being run simultaneously.

Tasks deployed on container would run the following processes:

Web Server : Main Fire UI and Fire Process : Helper processes for Spark jobs


  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/task-definition.png
     :alt: aws
     :width: 60%
   

Step 4 : Configure Service
-------------------
Select the tasks, application load balancer and target groups to deploy the service.

  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-service.png
     :alt: aws
     :width: 60%
   

**Application Load Balancer:**

* Internet which faces ALB listens to port 80.
* Container which runs the Fire task listens to port 8080.
* In target group, map the target port to 8080.
   
  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-alb.png
     :alt: aws
     :width: 60%
   
**Target Group:**

* Target type is IP and and target port is 8080.
 
  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-tg-1.png
     :alt: aws
     :width: 60%
   

* Health checks with path '/healthcheck' and success codes as '200, 302'.
  
  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/healtcheck.PNG
     :alt: aws
     :width: 60%

Step 5 : Deploy Service
--------------
Service is deployed with containers which run the tasks, ALB and target group.

  .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-alb-1.png
     :alt: aws
     :width: 60%
   
**Note:** Use the DNS name from the application load balancer.
  
  
  


