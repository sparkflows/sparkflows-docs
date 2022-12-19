Integration with Redshift
========================

Fire is fully integrated with Redshift. Fire has a number of Processors specifically for Redshift.

Redshift Processors
-------------

Fire has processors for reading from and writing to Redshift. They include:

* Read Redshift AWS

while using the above processor need to have below parameter

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
        - The Redshift table that should be read. Note that anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table you could also use a subquery in parentheses.
      * - awsAccessKeyId
        - AWS Access Key Id
        - AWS Access Key Id
      * - awsSecretAccessKey
        - AWS Secret Access Key
        - AWS Secret Access Key
      * - tempS3Dir
        - Temporary S3 directory
        - Temporary S3 directory

.. figure:: ../_assets/aws/read_redshift.PNG
   :alt: aws
   :width: 60% 

* Write Redshift AWS

while using the above processor need to have below parameter

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


.. figure:: ../_assets/aws/saveredshift.PNG
   :alt: aws
   :width: 60%
