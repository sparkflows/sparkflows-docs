Split Dataset By Expression
===========================

Fire Insights allows you to split incoming dataframes. Based on your needs, use the processors described below: 

- 'SplitByExpression': This processor splits the incoming dataset based on an expression. Rows satisfying the expression go into one dataframe and the rest go into another dataframe.
- 'SplitByMultipleExpressions': This processor splits the incoming dataset into multiple dataframes based on up to five conditional expressions.The output of each expression is routed to a separate output path.
- 'Split': This processor splits the incoming dataframe into two based on the percentage specified for the split. Split processor is especially useful in machine learning workflows.

Workflow
--------

.. figure:: ../../_assets/tutorials/dataset/32.PNG
   :alt: Dataset
   :align: center
   :width: 60%
   
   
In the example workflow above, 'Split By Multiple Expressions' processor splits the incoming dataframe into three output dataframes. The three conditions are on column c1 - "c1<3" , "c1>=3 and c1<5", and "c1>=5". As mentioned earlier, 'SplitByMultipleExpressions' can split incoming dataframe into up to five dataframes. 


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
