Aggregate
==========

Fire Insights provides processors that show aggregates for combinations of values in the selected columns.


Aggregate Processors in Fire Insights
----------------------------------------


.. list-table:: Aggregate Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Cube
     - Cube Node computes aggregations of a group of rows against all possible combinations of values in the selected grouping columns.
   * - Group By
     - This node computes aggregations of a group of rows against selected grouping column by applying selected aggregate functions on specified aggregate columns.
   * - Pivot By
     - This node creates a DataFrame based on the Pivot table created out of the incoming DataFrame. Pivot table is created by Aggregation of rows by applying the Aggregate functions on the Aggregate Columns against the Grouping and Pivot Columns selected.
   * - Rollup
     - Rollup Node generates a result set that shows aggregates for a hierarchy of values in the selected columns.
 

Cube
----------------------------------------

Below is a sample workflow which contains ``Cube`` processor in Fire Insights. It demonstrates usage of ``Cube`` node to compute aggregated value against all possible combinations of values in selected Cube columns.

It does the following processing of data:

*	Reads incoming Dataset.
*	Filters incoming Dataset based on requirement. Here, dataset is filtered for selected Departments.
*	Aggregated value (Sum of Salary) is computed using ``Cube`` node against all possible combinations of values in selected Cube Columns (Location and Dept).
* 	Aggregated data is printed using Print node.

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/Cube_WF.png
   :alt: cube_node_userguide
   :width: 55%
   

**Cube Node configuration**

*	It computes aggregation against all combinations of selected Cube columns values. Aggregated value (Sum of Salary) is computed using ``Cube`` node against all combinations of selected Cube Columns (Location and Dept) values.
*	Columns from incoming datasets against whom Aggregated values need to be calculated are to be selected as ``Cube Columns``. Multiple columns can be selected as ``Cube Columns``.
*	Columns on which aggregated values need to be computed are to be selected as ``Aggregated Columns``. If aggregated values need to be calculated on multiple columns then additional rows need to be added.
*	Function that needs to be used for Aggregated Value calculation is to be selected in ``Aggregate Operation To Use``. It can be different for each row.


.. figure:: ../../_assets/user-guide/data-preparation/aggregate/CubeNode1.png
   :alt: cube_node_userguide
   :width: 75%

Aggregate column and Aggregate function selection to compute aggregated value is done as below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/CubeNode2.png
   :alt: cube_node_userguide
   :width: 75%

**Cube Node output**

Aggregated value computed with the use of Cube node is displayed using Print node as shown below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/CubeNodeOutput.png
   :alt: cube_node_userguide
   :width: 75%

Group By
----------------------------------------

Below is a sample workflow which contains ``Group By`` processor in Fire Insights. It demonstrates the usage of ``Group By`` node to compute aggregation of data by grouping rows together based on ``Group By`` columns.

It does the following processing of data:

*	Reads incoming dataset.
*	Aggregated value (Sum of Salary) is computed with the use of ``Group By`` node by grouping rows together based on Group By column (Location).
* 	Aggregated data is printed using the Print node as shown below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/GroupBy_WF.png
   :alt: groupby_node_userguide
   :width: 55%
   

**Group By Node configuration**

*	It computes aggregation of data by grouping rows together based on Group By columns. Aggregated value (Sum of Salary) is computed using ``Group By`` node by grouping rows together based on ``Group By`` column (Location).
*	Columns from incoming Datasets against whom Aggregated values need to be calculated are to be selected as ``Grouping Columns``. Multiple columns can be selected as ``Grouping Columns``.
*	Columns on whom aggregated values need to be computed are to be selected as ``Aggregated Columns``. If aggregated values need to be calculated on multiple columns then additional rows need to be added.
*	Function that needs to be used for Aggregated Value calculation is to be selected in ``Aggregate Operation To Use``. It can be different for each row.
*	``Where Clause`` and ``Having Clause`` in the ``Filter Setting`` tab can be used to filter outgoing dataset.

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/GroupBy1.png
   :alt: groupby_node_userguide
   :width: 75%

Aggregate column and Aggregate function selection to compute aggregated value is done as below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/GroupBy2.png
   :alt: groupby_node_userguide
   :width: 75%

Filter Setting is entered as below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/GroupBy3.png
   :alt: groupby_node_userguide
   :width: 75%

**Group By Node output**

Aggregated value computed with the use of ``Group By`` node is displayed using the Print node as shown below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/GroupByOutput.png
   :alt: groupby_node_userguide
   :width: 75%

Pivot By
----------------------------------------

Below is a sample workflow which contains ``Pivot By`` processor in Fire Insights. It demonstrates the usage of ``Pivot By`` node to compute aggregation of data using Grouping columns and displayed against each Pivot Column value.

It does the following processing of data:

*	Reads incoming dataset.
*	Aggregated value (Employee Count) is computed with the use of ``Pivot By`` node by grouping rows together based on ``Group By`` column (Department) and displayed against each ``Pivot Column`` value (Location).
* 	Aggregated data is printed using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/PivotBy_WF.png
   :alt: pivotby_node_userguide
   :width: 55%
   

**Pivot By Node configuration**

*	It computes aggregation of data using Grouping columns and display it against each Pivot Column value. Aggregated value (Employee Count) is computed using ``Pivot By`` node by grouping rows together based on ``Group By`` column (Department) and displayed against each ``Pivot Column`` value (Location).
*	Columns from incoming Datasets against which Aggregated values need to be calculated are to be selected as ``Grouping Columns``. Multiple columns can be selected as ``Grouping Columns``.
*	Columns from incoming datasets against whom Aggregated values for each Group need to be displayed are to be selected as ``Pivot Columns``. Values from ``Pivot Columns`` would be displayed as Columns in the output. Multiple columns can be selected as ``Pivot Columns``.
*	Columns on which aggregated values need to be computed are to be selected as ``Aggregated Columns``. If aggregated values need to be calculated on multiple columns then additional rows need to be added.
*	Function that needs to be used for Aggregated Value calculation is to be selected in ``Aggregate Operation To Use``. It can be different for each row.


.. figure:: ../../_assets/user-guide/data-preparation/aggregate/PivotBy1.png
   :alt: pivotby_node_userguide
   :width: 75%

``Pivot Columns`` are selected as below. Data from ``Pivot Columns`` would be displayed as Columns in the output. Aggregated values would be diaplayed against each Pivot Column value. Multiple Pivot columns can be selected.

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/PivotBy2.png
   :alt: pivotby_node_userguide
   :width: 75%

Aggregate column and Aggregate function selection to compute aggregated value is done as below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/PivotBy3.png
   :alt: pivotby_node_userguide
   :width: 75%

**Pivot By Node output**

Aggregated value computed using ``Pivot By`` node is displayed using Print node as shown below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/PivotByOutput.png
   :alt: pivotby_node_userguide
   :width: 75%
   
Rollup
----------------------------------------

Below is a sample workflow which contains ``Rollup`` processor in Fire Insights. It demonstrates usage of ``Rollup`` node to compute aggregation of data using ``Rollup Columns``. Output is displayed in hierarchical order depicting the manner in which aggregation rolls-up upward.

It does the following processing of data:

*	Reads incoming dataset.
*	Filters incoming dataset based on requirement. Here, dataset is filtered for selected Departments.
*	Aggregated value (Sum of Salary) is computed using ``Rollup`` node for combinations of selected ``Rollup Columns`` (Location and Dept).
* 	Aggregated data is printed using the Print node.

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/Rollup_WF.png
   :alt: rollup_node_userguide
   :width: 55%
   

**Rollup Node configuration**

*	It computes aggregation of data using ``Rollup Columns``. Output is displayed in hierarchical order depicting the manner in which aggregation rolls-up upward. Aggregated value (Sum of Salary) is computed using ``Rollup`` node for combinations of selected ``Rollup Columns`` (Location and Dept).
*	Columns from incoming datasets against which Aggregated values need to be calculated are to be selected as ``Rollup Columns``. Multiple columns can be selected as ``Rollup Columns``.
*	Columns on which aggregated values are to be computed need to be selected as ``Aggregated Columns``. If aggregated values are to be calculated on multiple columns then additional rows need to be added.
*	Function that needs to be used for Aggregated Value calculation is to be selected in ``Aggregate Operation To Use``. It can be different for each row.

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/Rollup1.png
   :alt: rollup_node_userguide
   :width: 75%

Aggregate column and Aggregate function selection to compute aggregated value is done as below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/Rollup2.png
   :alt: rollup_node_userguide
   :width: 75%

**Rollup Node output**

Aggregated value computed with the use of Rollup node is displayed using the Print node as shown below:

.. figure:: ../../_assets/user-guide/data-preparation/aggregate/RollupOutput.png
   :alt: rollup_node_userguide
   :width: 75%
