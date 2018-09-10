SaveJDBC
=========== 

This node writes data to databases using JDBC.

Type
--------- 

transform

Class
--------- 

fire.nodes.save.NodeSaveJDBC

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      :stub-columns: 1

      * - Name
        - Title
        - Description
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
      * - truncate
        - Truncate
        - Whether to truncate the table in case Save Mode is Overwrite
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the table Exists




