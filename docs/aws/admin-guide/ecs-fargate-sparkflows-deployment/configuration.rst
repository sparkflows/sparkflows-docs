Fire Insights Deployment on ECS Fargate
=======================================

Follow the below steps to configure the task, service, application load balancer and task groups to run Fire Insights on ECS Fargate.


Pre-requisite
--------

You need to have an AWS account with required access to the resources.


ECS Cluster
----------

Create the ECS cluster wih VPC and security group. (Any pre-existing ECS cluster can also be used for deployment.)

.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-cluster.png
   :alt: aws
   :width: 60%


Task Definition
--------------
In order to create the task, attach the **ecsTaskExecutionRole** with all the policies and image name.

Add the ENV variable to use external MySQL otherwise the task will create and use the H2 database, by default. Also, an external database is mandatory when multiple replicas of the same task are being run simultaneously.


**Tasks deployed on container would run the following processes:**
 ``Web Server : Main Fire UI and Fire Process : Helper processes for Spark jobs``


.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/task-definition.png
   :alt: aws
   :width: 60%
   

Service
-------
Select the tasks, application load balancer and target groups to deploy the service.

.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-service.png
   :alt: aws
   :width: 60%
   

**Application Load Balancer:**


1. Internet which faces ALB listens to port 80.
2. Container which runs the Fire task listens to port 8080.
3. In target group, map the target port to 8080.
   

.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-alb.png
      :alt: aws
      :width: 60%
   
**Target Group:**

 
Target type is IP and and target port is 8080.
 
 
.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-tg-1.png
   :alt: aws
   :width: 60%
   

Health checks with path / and success code 200, 302.
  
.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-tg-2.png
   :alt: aws
   :width: 60%





Service is deployed with containers which run the tasks, ALB and target group.

.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-alb-1.png
   :alt: aws
   :width: 60%
      

Use the DNS name from the application load balancer.
  
  
  


