Read HIVE Table
=========== 

This node reads data from HIVE table and creates a DataFrame from it

Input
--------------
It reads in CSV text files

Output
--------------
It creates a DataFrame from the data read and sends it to its output

Type
--------- 

dataset

Class
--------- 

fire.nodes.hive.NodeHIVE

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - db
        - HIVE Database
        - HIVE Database
      * - table
        - HIVE Table
        - HIVE Table from which to read the data
      * - query
        - HIVE Query (Optional)
        - If a separate HIVE query needs to be used for reading from HIVE. This field is optional.
      * - outputColNames
        - Column Names of the database table
        - Column Names of the database table
      * - outputColTypes
        - Column Types of the database table
        - Column Types of the database table




