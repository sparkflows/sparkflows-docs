Save JSON
^^^^^^^^^

This node saves the input DataFrame into the specified location in JSON Format. When running on a Cluster, it is saved on HDFS.
 
**Input**

It takes in a DataFrame as Input.

**Output**

  * Dataframe : The input DataFrame is passed to the output without any changes.


**Parameters**

+-----------+------------------+----------------------------------------+
| **Name**  | **Title**        | **Description**                        |
+-----------+------------------+----------------------------------------+
| path      | Path             | Path of File/Directory                 |
+-----------+------------------+----------------------------------------+
| overwrite | Overwrite Output | Whether to overwrite the output or not |
+-----------+------------------+----------------------------------------+


