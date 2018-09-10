SaveAVRO-S3-AWS
=========== 

Saves the DataFrame into the specified S3 location in AVRO Format

Type
--------- 

transform

Class
--------- 

fire.nodes.aws.NodeSaveAvroS3

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - path
        - Path To S3
        - Path where to save the AVRO files Ex- (s3a://<bucketName>),If you don't give path it will browse your s3 bucket list
      * - awsAccessKeyId
        - AWS Access Key Id
        - AWS Access Key Id
      * - awsSecretAccessKey
        - AWS Secret Access Key
        - AWS Secret Access Key




