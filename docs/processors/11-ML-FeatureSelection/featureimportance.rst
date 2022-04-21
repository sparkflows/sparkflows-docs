Feature Selection With Importance
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.featureselection.NodeFeatureSelectionWithImportance

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - targetCol
        - TargetCol
        - Target column to be used when selecting the features
      * - featureCols
        - Feature Columns
        - The list of columns for which to calculate the feature importance
      * - mlType
        - MLType
        - target column type, Regression or Classification
      * - numfeatures
        - NumFeatures
        - Number features to be selected from Feature Importance calculated


Details
-------


This node enables to select the top features using Feature Importance.

In the workflow editor, it outputs the incoming schema without any changes. The reason for it is that unless the workflow is fully executed on the full data, it does not know the list of the top features.


