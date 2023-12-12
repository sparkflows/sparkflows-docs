Start EMR Cluster
=========

Fire Insights can submit jobs to AWS EMR cluster. This page describes the details of launching an EMR cluster on AWS.

Below are steps on how to create an EMR Cluster using AWS Console :

Step 1 : Sign-in to AWS Management Console
----------

#. Go to `Amazon Web Services Sign-in Page <https://console.aws.amazon.com/emr>`_ and enter your credentials to sign-in to your account.
#. Once you login, navigate to **Amazon EMR console**.

Step 2 : Create Cluster
----------

#. In the left navigation pane of EMR Console Page, click on **EMR on EC2** option and select **Clusters** and then proceed by choosing **Create cluster** option.

   .. figure:: ../../../_assets/aws/emr/aws_emr_create.PNG
      :alt: emr
      :width: 60%

#. On the **Create Cluster** page, note the default values for **Release, Instance type, Number of instances, and Permissions**. These fields automatically populate with values that work for general-purpose clusters.

#. In the **Cluster name** field, enter a unique cluster name to help you identify your cluster, such as *My first cluster*.

#. Under **Applications**, choose the **Spark** option to install Spark on your cluster.

   .. figure:: ../../../_assets/aws/emr/aws_cluster_details.PNG
      :alt: emr
      :width: 60%


#. Use bootstrap actions to install software or customize your instance configuration.

   .. figure:: ../../../_assets/aws/emr/aws_emr_bootstrap.PNG
      :alt: emr
      :width: 60%

         
   .. Note:: In order to use PySpark engine, you need to add **bootscript** to EMR cluster before proceeding further. `Click here <https://sparkflows-release.s3.amazonaws.com/fire/docker/docker-ubuntu/emr-bootstrap_nump_fix.sh>`_ to get the bootscript. 

   .. figure:: ../../../_assets/aws/emr/python_dependency.PNG
      :alt: emr
      :width: 60%
     

#. Under **Cluster logs**, select the **Publish cluster-specific logs to Amazon S3** check box. 

   Replace the *Amazon S3 location value* with the **Amazon S3 bucket** you created, followed by /logs. For example, **s3://DOC-EXAMPLE-BUCKET/logs**. 

   **Note :** Adding /logs creates a new folder called 'logs' in your bucket, where Amazon EMR can copy the log files of your cluster.


   .. figure:: ../../../_assets/aws/emr/aws_emr_logs.PNG
      :alt: emr
      :width: 60%

#. Under **Security configuration and permissions**, choose your **EC2 key pair**. 

   In the same section, select the **Service role for Amazon EMR** dropdown menu and choose **EMR_DefaultRole**. 

   Next, select the **IAM role for instance profile** dropdown menu and choose **EMR_EC2_DefaultRole**.

   .. figure:: ../../../_assets/aws/emr/aws_emr_role.PNG
      :alt: emr
      :width: 60%

#. Click on **Create cluster** to launch the cluster and open the **Cluster Details Page**.

#. Find the cluster **Status** next to the cluster name. The status changes from **Starting** to **Running** to **Waiting** as Amazon EMR provisions the cluster. 

Reference Documentation is available at the `Amazon EMR Tutorial Guide <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html>`_ for further details.
