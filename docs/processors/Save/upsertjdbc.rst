UpsertJDBC
=========== 

This node insert or update the data to databases using JDBC.

Type
--------- 

transform

Class
--------- 

fire.nodes.save.NodeUpsertJDBC

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - primaryKeyColumn
        - PrimaryKeyColumn
        - Key column name in table
      * - url
        - URL
        - The JDBC URL to connect to
      * - table
        - DB Table
        - The JDBC table to write to
      * - driver
        - Driver
        - The class name of the JDBC driver needed to connect to the URL
      * - user
        - User
        - Username with which to connect to the DB
      * - password
        - Password
        - Password with which to connect to the DB




