Flag Outlier
=========== 

Flag the outlier based on the selected column using Box-and-Whisker technique.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeFlagOutlier

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column to flag the outlier
        - The Input Column to flag the outlier
      * - lowerQuantile
        - LowerQuantile
        - 
      * - upperQuantile
        - UpperQuantile
        - 


Details
-------


This node identifies whether a data point is outlier in a series or not based on the lower and upper quantile set. 

It can be checked against numeric columns only.


Examples
-------


FlagOutlier node can be configured as below:

INPUT COLUMN TO FLAG THE OUTLIER	:	SALARY
LOWERQUANTILE						          :	0.25
UPPERQUANTILE						          :	0.75

New column [is_SALARY_outlier] would be added to the output specifing whether a data point is outlier or not.
