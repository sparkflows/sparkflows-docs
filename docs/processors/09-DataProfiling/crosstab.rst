Cross Tab
=========== 

Categorical V.S. Categorical

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeCrosstab

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - firstColumn
        - FirstColumn
      * - secondColumn
        - SecondColumn


Details
-------


This node displays distribution of data between all possible combination of all distinct values of two series.


Examples
-------


If CrossTab node is configured below i.e. selecting two columns from the dataset:

FirstColumn		:		Dept
SecondColumn	:		Location

then outgoing Dataframe would be created in tabular format displaying distribution / count of all possible combination between distinct value of [DEPT] and [LOCATION]
