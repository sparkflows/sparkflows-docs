ReadHBase
=========== 

Read the rows in the incoming DataFrame onto Apache HBase using the specific field mapping

Input
--------------
It does not take any DataFrame as input

Output
--------------
It queries HBase and creates a DataFrame from the resulting rows. This DataFrame is passed to the output Nodes.

Type
--------- 

dataset

Class
--------- 

fire.nodes.hbase.NodeReadHBase

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - hbaseSite
        - HBase Site XML (if reading from hbase-site.xml)
        - HBase Site XML eg: /etc/hbase/conf/hbase-site.xml
      * - hbaseMaster
        - HBase Master
        - HBase Master eg: localhost:60000
      * - timeout
        - Timeout
        - Timeout eg: 120000
      * - hbaseZookeeperQuorum
        - HBase Zookeeper Quorum
        - HBase Zookeeper Quorum eg: localhost
      * - zookeeperZnodeParent
        - Zookeeper Znode Parent
        - Zookeeper Znode Parent eg: /hbase
      * - hbaseTableName
        - HBase Table Name
        - HBase Table from which to read data from
      * - dateFormat
        - Date Format for date columns
        - eg: yyyy-MM-dd
      * - timeFormat
        - Time Format for timestamp columns
        - eg: yyyy-MM-dd HH:mm:ss
      * - inputColNames
        - HBase Column Name
        - HBase Table Schema
      * - inputColTypes
        - HBase Column Type
        - Data Type of the Column
      * - inputColFamilyNames
        - HBase Column Family
        - HBase Column Family




