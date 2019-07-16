StreamingTextFileStream
=========== 

It monitors a specified directory for new files. It keeps reading in any new files created in the directory.

Input
--------------
It does not take any DataFrame as input

Output
--------------
It reads the new files and creates DataFrame from the content of the text files. This DataFrame is passed to the output Nodes.

Type
--------- 

sparkstreaming

Class
--------- 

fire.nodes.streaming.NodeStreamingTextFileStream

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
        - Directory from where to pick up files from
      * - batchDuration
        - Batch Duration in Seconds
        - Batch Duration in Seconds
      * - outputCol
        - Output Column
        - Output Column




