Start EMR Cluster
=========

Fire Insights can submit jobs to AWS EMR cluster. This page describes the details of launching and EMR cluster on AWS.

Below are steps on how to create an EMR Cluster using AWS Console:

1. Sign in to the AWS Management Console, and open the Amazon EMR console at https://console.aws.amazon.com/emr

2. Under ``EMR on EC2`` in the left navigation pane, choose ``Clusters``, and then choose ``Create cluster``.

.. figure:: ../../_assets/aws/emr/aws_emr_create.PNG
         :alt: emr
         :width: 60%



3. On the ``Create Cluster`` page, note the default values for ``Release, Instance type, Number of instances, and Permissions``. These fields automatically populate with values that work for general-purpose clusters.

4. In the ``Cluster name`` field, enter a unique cluster name to help you identify your cluster, such as ``My first cluster``.

5. Under ``Applications``, choose the ``Spark`` option to install Spark on your cluster.

.. figure:: ../../_assets/aws/emr/aws_cluster_details.PNG
         :alt: emr
         :width: 60%


6. Use bootstrap actions to install software or customize your instance configuration.

.. figure:: ../../_assets/aws/emr/aws_emr_bootstrap.PNG
         :alt: emr
         :width: 60%

.. Note:: Inorder to use PySpark engine, you need to add ``bootscript`` to emr cluster before starting from below location:

https://sparkflows-release.s3.amazonaws.com/fire/docker/docker-ubuntu/emr-bootstrap_nump_fix.sh

.. figure:: ../../_assets/aws/emr/python_dependency.PNG
         :alt: emr
         :width: 60%

7. Under ``Cluster logs``, select the Publish cluster-specific logs to Amazon S3 check box. Replace the ``Amazon S3 location`` value with the Amazon S3 bucket you created, followed by /logs. For example, s3://DOC-EXAMPLE-BUCKET/logs. Adding /logs creates a new folder called 'logs' in your bucket, where Amazon EMR can copy the log files of your cluster.


.. figure:: ../../_assets/aws/emr/aws_emr_logs.PNG
         :alt: emr
         :width: 60%

8. Under ``Security configuration and permissions``, choose your ``EC2 key pair``. In the same section, select the ``Service role for Amazon EMR`` dropdown menu and choose ``EMR_DefaultRole``. Then, select the ``IAM role for instance profile`` dropdown menu and choose ``EMR_EC2_DefaultRole``

.. figure:: ../../_assets/aws/emr/aws_emr_role.PNG
         :alt: emr
         :width: 60%

9. Choose ``Create cluster`` to launch the cluster and open the cluster details page.

10. Find the cluster ``Status`` next to the cluster name. The status changes from ``Starting`` to ``Running`` to ``Waiting`` as Amazon EMR provisions the cluster. 


Reference Documentations : https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html