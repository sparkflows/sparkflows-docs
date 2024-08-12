Fire Insights Deployment on AWS EKS
=======================================

Fire Insights can be deployed using AWS Elastic Kubernetes Service. This document explains the steps required to configure the task, service, application load balancer and task groups to run Fire Insights on ECS Fargate.

Below are the steps:

Step 1 : Pre-requisite Check
--------

Ensure that you have an AWS account with the necessary access to resources before proceeding with the deployment.

Install **eksctl** CLI tool to create and manage EKS clusters. Follow the steps mentioned here: https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html
or https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html.

Ensure that your aws cli is configured with your credentials. Follow the steps mentioned here: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

Step 2 : Create EKS Cluster
----------

Create an EKS cluster using eksctl. Use the following command in your terminal to create the cluster, change any parameters as needed:

    .. code-block:: bash

        eksctl create cluster \
        --name sparkflows-test-cluster \
        --region us-east-1 \
        --nodegroup-name standard-workers \
        --node-type t3.large \
        --nodes 1 \
        --nodes-min 1 \
        --nodes-max 2

The above command will create following resources.

1. Custom VPC and public and private subnets
2. EC2 and autoscaling group
3. CloudFormation stack
4. EKS cluster and node group
5. The cluster will have 1 worker nodes of t3.large EC2 instance and will be placed in public subnet by default.

The creation and deployment of the stack can take up a few minutes. Check for security group inbound and outbound rules to allow traffic from the desired source to the EKS cluster.


Step 3 : Deployment / Service Configuration
--------------
.. insert task definition image

Create deployment/service using kubectl. Update image url of deploy.yaml file accordingly.
.. insert infrastructure reqmnts image

  .. code-block:: YAML

    apiVersion: v1
    kind: Service
    metadata:
      name: fire
    spec:
      type: LoadBalancer
      ports:
        - port: 8080
          targetPort: 8080
      selector:
        app: fire
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: fire
    spec:
      selector:
        matchLabels:
          app: fire
      strategy:
        type: Recreate
      template:
        metadata:
          labels:
            app: fire
        spec:
          containers:
            - image: sparkflows/fire:py_3.3.1_3.2.53-rc81
              env:
                - name: KEYSTORE_PASSWORD
                  value: "12345678"
              name: fire
              resources:
                limits:
                  memory: "3Gi"
                requests:
                  memory: "1Gi"
              ports:
                - containerPort: 8080
                  name: fire

The above yaml file creates a service and deployment for Sparkflows.

    .. code-block:: bash

        kubectl apply -f deploy.yaml


Step 4 : Check Deployment
-------------------
On successful deployment, check the status of the pods and services using the following commands:

    .. code-block:: bash

        kubectl get pods
        kubectl get svc


Step 5 : Access Sparkflows
-------------------
Use the external IP of the service to access Sparkflows. The external IP can be found using the following command:

    .. code-block:: bash

        kubectl get svc fire

You can now use the **<external-IP>:targetPort** to access Sparkflows in the browser.

  .. note::  Two user accounts come preconfigured with Sparkflows.
           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Fire under the menu Administration/Users 
