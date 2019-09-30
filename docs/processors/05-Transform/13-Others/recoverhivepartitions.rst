RecoverHivePartitions
=========== 

Node to recover the partitions of external hve table.

Type
--------- 

doc

Class
--------- 

fire.nodes.etl.NodeRecoverHivePartitions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - databaseName
        - HIVE Database
        - Name of the HIVE Database
      * - tableName
        - HIVE Table
        - Name of the HIVE table


Details
-------


This node is used recover the partitions of external hve table.

It will run the command: "MSCK REPAIR TABLE ${HIVE Database}.${HIVE Table}"


Parameters
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - HIVE Database
     - test
     
   * - HIVE Table
     - transactions
     
     
