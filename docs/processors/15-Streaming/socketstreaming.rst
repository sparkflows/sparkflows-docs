StreamingSocketTextStream
=========== 

Reads in streaming text from a socket

Input
--------------
It does not take any DataFrame as input

Output
--------------
It creates DataFrame from reading data from a socket. This DataFrame is passed to the output Nodes.

Type
--------- 

sparkstreaming

Class
--------- 

fire.nodes.streaming.NodeStreamingSocketTextStream

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - batchDuration
        - Batch Duration in Seconds
        - Batch Duration in Seconds
      * - hostname
        - Hostname
        - Host to connect to for listening
      * - port
        - Port
        - Port to connect to 


Details
-------



This Processor reads in messages from a Socket

Key Fields
--------------

Below are the key fields of this Processor.


* hostname: this is the name of the host from where to read in the messages
* port: this is the port number from where to read in the messages


Examples
-------


Below is an example of the fields:


* hostname: localhost
* port: 8099
