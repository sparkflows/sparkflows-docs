Split Dataset By Expression
===========================

In Fire Insights you can split the incoming DataFrame. Based on your need, use the processors descripbed below: 

- 'SplitByExpression': This processor splits the incoming dataset based on an expression. Rows satisfying the expression go into one dataframe and the rest go into another dataframe.
- 'SplitByMultipleExpressions': This processor splits the incoming dataset into multiple dataframes based on up to five conditional expressions.The output of each expression is routed to a separate output path.
- 'Split': This processor splits the incoming dataframe into two based on the percentage specified for the split. Split processor is especially useful in machine learning workflows.

Workflow
--------

.. figure:: ../../_assets/tutorials/dataset/32.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
   
In the example workflow above, 'Split By Multiple Expressions' processor splits the incoming dataframe into 3 output dataframes. As mentioned earlier, 'SplitByMultipleExpressions' can split incoming dataframe into up to five dataframes. 


.. figure:: ../../_assets/tutorials/dataset/33.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
Output
------

For the example workflow, the three output dataframes are shown below:

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
