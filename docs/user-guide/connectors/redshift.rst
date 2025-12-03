Redshift
========================

Sparkflows has processors for reading from and writing to Redshift.

Read Redshift AWS
-----------

Processor Configuration Parameters:

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - URL
        - URL
        - The JDBC URL to connect to.
      * - REDSHIFT TABLE
        - Redshift Table
        - The Redshift table that should be read. Note that anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table you could also use a subquery in parentheses.
      * - AWS ACCESS KEY ID
        - AWS Access Key Id.
        - AWS Access Key Id.
      * - AWS SECRET ACCESS KEY
        - AWS Secret Access Key.
        - AWS Secret Access Key.
      * - TEMPORARY S3 DIRECTORY
        - Temporary S3 directory.
        - Temporary S3 directory.

.. figure:: ../../_assets/aws/read_redshift.PNG
   :alt: aws
   :width: 85% 

Write Redshift AWS
---------------

While using the above, the processor needs to have below parameter:

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - URL
        - URL
        - The JDBC URL to connect to.
      * - REDSHIFT TABLE
        - Redshift Table
        - The Redshift table that should be write. Note that anything that is valid in a FROM clause of a SQL query can be used. For example, instead of a full table you could also use a subquery in parentheses.
      * - AWS ACCESS KEY ID
        - AWS Access Key Id.
        - AWS Access Key Id.
      * - AWS SECRET ACCESS KEY
        - AWS Secret Access Key.
        - AWS Secret Access Key.
      * - TEMPORARY S3 DIRECTORY
        - Temporary S3 directory.
        - Temporary S3 directory.
      * - SAVE MODE
        - Save Mode.
        - Whether to Append, Overwrite or Error if the path exists.


.. figure:: ../../_assets/aws/saveredshift.PNG
   :alt: aws
   :width: 85%
