Split Dataset By Expression
===========================

In Fire Insights you can split the incoming DataFrame. Based on your need, use the processors descripbed below: 

- 'SplitByExpression': This processor splits the incoming dataset based on an expression. Rows satisfying the expression go into one dataframe and the rest go into another dataframe.
- 'SplitByMultipleExpressions': This processor splits the incoming dataset into multiple dataframes based on up to 5 conditional expressions.The output of each expression is routed to a separate output path.
- 'Split': This processor splits the incoming dataframe into two based on the percentage specified for the split. Split processor is espeically useful in machine learning workflows.
 


The other is to split the incoming DataFrame based on an expression. 

We recently ran into a requirement for splitting the incoming DataFrame by multiple conditions. So we added a new Node called 'SplitByMultipleExpressions'. It allows users to specify up to 5 conditional expressions. The output of each expression is routed to one output path.

Workflow
--------

.. figure:: ../../_assets/tutorials/dataset/32.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
   
In the above workflow, the Node 'Split By Multiple Expressions' is able to split the incoming DataFrame into 3 output DataFrames. With the current implementation it can split up in to  5 ways.


.. figure:: ../../_assets/tutorials/dataset/33.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
Output
------

Each of the 3 output DataFrames look like below:

.. figure:: ../../_assets/tutorials/dataset/34.PNG
   :alt: Dataset
   :align: center
   :width: 60%

.. figure:: ../../_assets/tutorials/dataset/35.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
.. figure:: ../../_assets/tutorials/dataset/36.PNG
   :alt: Dataset
   :align: center
   :width: 60%   
