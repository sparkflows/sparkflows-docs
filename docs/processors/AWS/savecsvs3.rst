SaveCSV-S3-AWS
=========== 

Saves the DataFrame into the specified S3 location in CSV Format

Type
--------- 

transform

Class
--------- 

fire.nodes.aws.NodeSaveCSVS3

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
        - Path where to save the CSV files Ex- (s3a://<bucketName>),If you don't give path it will browse your s3 bucket list
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the path Exists




