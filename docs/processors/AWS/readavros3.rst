ReadAVRO-S3-AWS
=========== 

Read the AVRO file from specified S3 location

Type
--------- 

dataset

Class
--------- 

fire.nodes.aws.NodeReadAvroS3

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
        - Path from where AVRO files to read (s3a://<bucketName>),If you don't give path it will browse your s3 bucket list
      * - outputColNames
        - Column Names for the AVRO
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the AVRO
        - Data Type of the Output Columns
      * - outputColFormats
        - Column Formats for the AVRO
        - Format of the Output Columns




