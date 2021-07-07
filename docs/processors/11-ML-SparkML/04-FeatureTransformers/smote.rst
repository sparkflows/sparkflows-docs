SMOTE
=========== 

Implementation of SMOTE - Synthetic Minority Over-sampling Technique.

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
Output DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeSMOTE

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - labelCol
        - Label Column
        - Label Column.
      * - featureCol
        - Feature Column
        - Feature Column with vector type.
      * - bucketLength
        - BucketLength
        - Bucket Length for LSH - The length of each hash bucket, a larger bucket lowers the false negative rate.




