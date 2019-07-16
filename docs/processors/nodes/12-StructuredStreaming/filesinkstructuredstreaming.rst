StructuredStreamingFileSink
=========== 

It writes the DataFrame to files with Structured Streaming

Input
--------------
It takes in DataFrame as input

Output
--------------
It writes the incoming DataFrame to files.

Type
--------- 

transform

Class
--------- 

fire.nodes.structuredstreaming.NodeStructuredStreamingFileSink

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - path
        - Path
        - Path where to write the files
      * - outputMode
        - Output Mode
        - Output Mode for saving to Files
      * - checkpointLocation
        - Checkpoint Location
        - Checkpoint Location on HDFS compatible file system for Streaming
      * - format
        - Format
        - File Format
      * - partitionBy
        - Partition By Columns
        - Partition By Columns separated by space (can be empty in which case partitionBy would not be applied)




