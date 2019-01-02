StructuredStreamingSocket
=========== 

Reads in streaming text from a socket

Input
--------------
It does not take any DataFrame as input

Output
--------------
It reads events a socket and creates DataFrame from the resulting rows. This DataFrame is passed to the output Nodes.

Type
--------- 

sparkstreaming

Class
--------- 

fire.nodes.structuredstreaming.NodeStructuredStreamingSocket

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - host
        - Hostname
        - Host to connect to for listening
      * - port
        - Port
        - Port to connect to 




