Integrate with Kubeflow
=====

This document explains in detail the steps involved in Integrating Kubeflow on HPE UA.

Follow the below steps to Integrate Kubeflow in Sparkflows:

#. Disable the Livy Connection

#. In Sparkflows, Navigate to File System: /usr/local/mlops

#. Put Docker file and extracted Docker zip components, inside docker context path (/usr/local/mlops)

#. Now again Enable the Livy Connection.

#. Navigate Administration >> Configuration >> MLOps and configure MLOps with Kubeflow

#. Add below details

   .. figure:: ../../_assets/hpe/kubeflow-integration-1.png
      :width: 60%
      :alt: Sparkflows On UA
	  
   .. figure:: ../../_assets/hpe/kubeflow-integration-2.png
      :width: 60%
      :alt: Sparkflows On UA

#. Parameters

	::
	
		mlops.mlflow.trackingURL              https://mlflow.sparkflows.net:5000  
		mlops.mlflow.deploy.mode              fire_mlops_server 
		mlops.port                            5000   
		mlops.aws.s3.secret.key               ***************************
		mlops.aws.s3.access.key               ***************************
		mlops.models.state.values             Dev,QA,Production  
		mlops.target.deployment               kubeflow
		mlops.kubeflow.username               your_username
		mlops.kubeflow.password               your_password
		mlops.docker.registry.sparkflows      10.102.54.230:5000  
		mlops.docker.context.path             /usr/local/mlops  
		mlops.kubeflow.namespace              sparkflows
		mlops.kubernetes.images.namespace     sparkflows 
		mlops.fire.server.jar.name            fire-spark_3.2.1-server-3.1.0-jar-with-dependencies.jar  
		mlops.deployment.container.port       5000 
		mlops.service.port                    80
		mlops.service.target.port             5000  
		mlops.aws.s3.endpoint.url             10.2.0.10:9000  
		mlops.aws.s3.ignore.tls               true  

#. Click on **Save** to save the configuration details.
