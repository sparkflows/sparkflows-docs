SaveRedshift-AWS
=========== 

This node save data to Redshift using JDBC.

Type
--------- 

transform

Class
--------- 

fire.nodes.aws.NodeSaveRedshift

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - url
        - URL
        - The JDBC URL to connect to
      * - dbtable
        - Redshift Table
        - The Redshift table that should be write. Note that anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table you could also use a subquery in parentheses.
      * - awsAccessKeyId
        - AWS Access Key Id
        - AWS Access Key Id
      * - awsSecretAccessKey
        - AWS Secret Access Key
        - AWS Secret Access Key
      * - tempS3Dir
        - Temporary S3 directory
        - Temporary S3 directory
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the path Exists




