StructuredStreamingKensis
=========== 

Reads in streaming text from Kensis stream

Input
--------------
It does not take any DataFrame as input

Output
--------------
It reads events from Kensis and creates DataFrame from the resulting rows. This DataFrame is passed to the output Nodes.

Type
--------- 

sparkstreaming

Class
--------- 

fire.nodes.structuredstreaming.NodeStructuredStreamingKinesis

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - streamName
        - Stream Name
        - Kensis Stream Name
      * - endpointUrl
        - Endpoint Url
        - Kensis Endpoint Url




