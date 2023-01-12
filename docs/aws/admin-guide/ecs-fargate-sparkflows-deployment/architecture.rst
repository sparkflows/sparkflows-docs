Overivew and Architecture
=========================

Fire Insights deployment on ECS Fargate can be understood with the help of following image:


.. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/Sparklfows_ECS_Fargate.png
   :alt: aws
   :width: 60%
   




1. Fire Insights tasks running on ECS Fargate containers.
2. Metadata is stored in RDS MySql instance.
3. In web interface, create workflows, pipelines etc. with interactive execution.
4. User can browse the S3 and Hive tables.
5. Execute the worfklows and pipelines on EMR Cluster through Livy/Airflow and also on EKS.
