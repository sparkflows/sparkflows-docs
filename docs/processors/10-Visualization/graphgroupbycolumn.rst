Graph Group By Column
=========== 

Groups the data by the given column and plots the number of records in each group

Type
--------- 

transform

Class
--------- 

fire.nodes.graph.NodeGraphGroupByColumn

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - title
        - Title
      * - xlabel
        - X Label
      * - ylabel
        - Y Label
      * - maxValuesToDisplay
        - Max Values To Display
        - Maximum number of values to display in result.
      * - chartColors
        - Chart Colors
      * - groupByColumn
        - Group By Column
      * - graphType
        - Chart Type


Details
-------


This node represents distribution / count of group of data in Graphical format.

A numeric column from the incoming dataset is selected to aggregate data into multiple groups. Count of data-points in each group is plotted in the Chart.

Chart Type used to represent data can be selected in the node.


