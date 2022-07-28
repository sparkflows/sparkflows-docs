Fire Insights Deployment on ECS Fargate
=======================================

Below are the steps to configure the task, service, application load balancer and tasks group to run fire insights on ECS Fargate.


Pre-requisite
--------

Need to have an AWS account with required access to resources.


ECS CLuster
----------

Create the ecs cluster wih VPC and security group.(Also existing ecs cluster can be used).

.. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-cluster.png
   :alt: aws
   :width: 60%


Task Definition
--------------
Create the task by attaching the ecsTaskExecutionRole with all policy and image name.

Add the ENV variable to use external MySQL othwise by default task will create and use the h2db. And external database is mandataory when mutiple replica of same task is running.


**Tasks deployed on container would run the following processes:**
 Web Server : Main fire UI and Fire Process : Helper processes for spark jobs


.. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/task-definition.png
   :alt: aws
   :width: 60%
   

Service
-------
Deploy the service by selecting the tasks, application load balacer and target groups.

.. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-service.png
   :alt: aws
   :width: 60%
   

**Application Load Balancer:**


   Internet facing ALB listen to port 80.
   Container running the fire task listen to port 8080.
   In target group map the target port to 8080.
   
   .. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-alb.png
      :alt: aws
      :width: 60%
   
**Target Group:**

 
   Target type is IP and and target port 8080.
   
.. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-tg-1.png
   :alt: aws
   :width: 60%
   

   Health checks with path / and success code 200, 302
  
.. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-tg-2.png
   :alt: aws
   :width: 60%





Service is deployed with containers running the tasks, alb and target group.

.. figure:: ../../_assets/aws/ecs-fargate-sparkflows-deployment/ecs-alb-1.png
   :alt: aws
   :width: 60%
      

Use the DNS Name from running application load balancer.
  
  
  


