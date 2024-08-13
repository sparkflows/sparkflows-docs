AWS EKS Setup
=============

Below are steps on how to setup EKS in AWS.

Step 1 : Create an IAM Role
------------------------------

Create an IAM Role for your EKS Cluster:

#. Navigate to the **IAM Dashboard**.
#. Click on **Roles**, then select **Create Role**.
#. Choose **AWS Service** as the trusted entity.
#. Select **EKS** and then **EKS Cluster**.
#. Click **Next** to proceed.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

#. Give the Role a **name**, and click on **Create role**. This will allow your EKS Cluster to perform operations such as creating pods or load balancers.

Step 2 : Create the EKS Cluster
--------------------------------
#. Go to the **EKS Console** and click on **Clusters**, then select **Create Cluster**.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

#. Provide a **name** for your cluster, choose the **Kubernetes version**, and select the **EKS Role** you created in the previous step.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

#. Click **Next** and choose the recently created **VPC**. The subnets and security group will be automatically selected. For Cluster Endpoint Access, choose **Public and Private**. Set everything else as **default**, and click on **Create**. This step might take up to 15 minutes.


   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

   Once your cluster is ready, it should display an Active status on the EKS page.

Step 3: Create a Node Group EC2 IAM Role
-----------------------------------------------
Before setting up the Node Group for your cluster, you need to create an IAM Role that allows the kubelet daemon on each node to interact with AWS APIs and manage pods.

#. Navigate to the **IAM Dashboard**.
#. Click on **Roles** and then select **Create Role**.
#. Choose **AWS Service** as the trusted entity and select **EC2**.
#. Click **Next** and add the required policies.
#. Give the Role a **name** and click on **Create role**.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

Step 4: Create a Node Group
----------------------------
Now, let's create the Node Group for your cluster:

#. Return to the **EKS dashboard**, select your cluster, and click on **Add Node Group**.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%
#. Provide a **name** for the Node Group, select the Node Group IAM Role you created earlier, and click **Next**.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

#. Choose the AMI and instance type for your nodes. For this project, we'll use Amazon Linux 2 t2.xlarge EC2 instances.
#. Configure the auto-scaling group parameters based on your needs.
#. Leave the remaining settings as default and create the Node Group.


Step 5: Configure EKS
------------------------

Once your EKS cluster is up and running, you'll need to update the local kubeconfig to execute kubectl commands.

#. Export AWS Credentials and Region.
   
   Start by exporting your AWS credentials and region as shown below: ::

      export AWS_ACCESS_KEY_ID=A************4IOR
      export AWS_SECRET_ACCESS_KEY=PlxK***************iaFpp3EwVTuFJP/GHc8S
      export AWS_DEFAULT_REGION=us-east-1

   Ensure you have permission to access the EKS cluster. Navigate to the EKS Cluster in the AWS Console, click on **IAM Access**, and add your IAM role if it's not already present.

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%

#. Update Local Kubeconfig.

   Update your local kubeconfig to point to the EKS cluster: ::

      aws eks update-kubeconfig --region us-east-1 --name <clustername> --profile <aws-profile>

#. Verify Kubeconfig.

   Confirm that your kubeconfig is correctly pointing to the AWS EKS cluster: ::

      kubectl config get-contexts

   .. figure:: ../../../_assets/aws/aws-eks/
      :alt: aws
      :width: 60%


#. Create a User Account.

   Create a user account named sparkflows-admin and associate it with the IAM role used to create the EKS cluster. Create a ServiceAccount with the following configuration: ::

      apiVersion: v1
      kind: ServiceAccount
      metadata:
        name: sparkflows-admin
        annotations:
          eks.amazonaws.com/role-arn: arn:aws:iam::004331324847:role/eks-stem

   Apply this configuration: ::

      kubectl apply -f service-account.yaml

#. Create a Job Role.

   Define a ClusterRole with the necessary permissions for Sparkflows to run Jupyter notebooks: ::

      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRole
      metadata:
       name: job-creator
      rules:
      - apiGroups: ["batch",""]
        resources:
        - jobs
        - pods
        - pods/log
      verbs:
      - create
      - get
      - update
      - watch
      - list

#. Bind the Role.

   Bind the job-creator role to the sparkflows-admin user using a ClusterRoleBinding: ::

      apiVersion: rbac.authorization.k8s.io/v1
      kind: ClusterRoleBinding
      metadata:
       name: job-creator-binding
      subjects:
      - kind: ServiceAccount
        name: sparkflows-admin
        namespace: default
      roleRef:
       kind: ClusterRole
       name: job-creator
       apiGroup: rbac.authorization.k8s.io

   After this, you should be able to create and execute notebooks from Sparkflows.
