Overivew and Architecture
=========================

Sparkflows deployment architecture on ECS Fargate would look like below:


.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/Sparklfows_ECS_Fargate.png
   :alt: aws
   :width: 60%
   




1. Sparkflows tasks running on ECS Fargate containers.
2. Metadata is stored in RDS MySQL instance.
3. Via the web interface, create workflows, pipelines with interactive execution.
4. User can browse the S3 and Hive tables.
5. Execute the workflows and pipelines on EMR Cluster through Livy/Airflow and also on EKS.
