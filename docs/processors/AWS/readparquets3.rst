ReadParquet-S3-AWS
=========== 

Read the Parquet file from specified S3 location

Type
--------- 

dataset

Class
--------- 

fire.nodes.aws.NodeReadParquetS3

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
        - Path from where Parquet files to read (s3a://<bucketName>),If you don't give path it will browse your s3 bucket list
      * - awsAccessKeyId
        - AWS Access Key Id
        - AWS Access Key Id
      * - awsSecretAccessKey
        - AWS Secret Access Key
        - AWS Secret Access Key
      * - outputColNames
        - Column Names for the Parquet
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the Parquet
        - Data Type of the Output Columns
      * - outputColFormats
        - Column Formats for the Parquet
        - Format of the Output Columns




