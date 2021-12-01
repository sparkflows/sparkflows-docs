Split Dataset By Expression
===========================

Fire Insights allows you to split incoming dataframes. Based on your needs, use the processors described below: 

- 'SplitByExpression': This processor splits the incoming dataset based on an expression. Rows satisfying the expression go into one dataframe and the rest go into another dataframe.
- 'SplitByMultipleExpressions': This processor splits the incoming dataset into multiple dataframes based on up to five conditional expressions.The output of each expression is routed to a separate output path.
- 'Split': This processor splits the incoming dataframe into two based on the percentage specified for the split. Split processor is especially useful in machine learning workflows.

Workflow
--------

.. figure:: ../../_assets/tutorials/data-preparation/Split-Dataset-By-Expression/4.PNG
   :alt: Dataset
   :width: 100%
   
   
In the example workflow above, 'Split By Multiple Expressions' processor splits the incoming dataframe into three output dataframes. The three conditions are on column c1 - "c1<3" , "c1>=3 and c1<5", and "c1>=5". As mentioned earlier, 'SplitByMultipleExpressions' can split incoming dataframe in up to five dataframes. 


.. figure:: ../../_assets/tutorials/data-preparation/Split-Dataset-By-Expression/5.PNG
   :alt: Dataset
   :width: 100%

.. figure:: ../../_assets/tutorials/data-preparation/Split-Dataset-By-Expression/6.PNG
   :alt: Dataset
   :width: 100%

Output
------

For the example workflow, the three output dataframes are shown below:

.. figure:: ../../_assets/tutorials/data-preparation/Split-Dataset-By-Expression/7.PNG
   :alt: Dataset
   :width: 100%

.. figure:: ../../_assets/tutorials/data-preparation/Split-Dataset-By-Expression/8.PNG
   :alt: Dataset
   :width: 100%
   
.. figure:: ../../_assets/tutorials/data-preparation/Split-Dataset-By-Expression/9.PNG
   :alt: Dataset
   :width: 100%   
