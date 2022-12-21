Time Series Visualizations
--------------------------

Fire Insights provides a number of Processors for the visualization of the time series data.

.. list-table:: Update New features where needed
   :widths: 10 40
   :header-rows: 1

   * - Charts
     - Description
   * - Line
     - Perfect for series of data points to form a continuous line.
   * - Bar
     - Bar charts are a fundamental visualization for comparing values between groups of data. Best way to represent Categorical data.
   * - Scatter
     - Scatter plots are used to observe relationships between variables.
   * - Histogram
     - Histograms are a type of graph that shows the distribution of a dataset. They graph the percentage or the number of instances of different categories.
   * - Pie
     - Illustrate the percentage breakdown of a small number of data points, then they can be very effective.

Charts : LineChart
==================

Line Charts are perfect for series of data points to form a continuous line.
For example it can be used to represent Daily sales data

Below is the sample workflow which contains ``Time Series data`` and outputs a line chart in Fire Insights.

.. figure:: ../../_assets/ml_userguide/visual.PNG
   :alt: ml_userguide
   :width: 90%

Configurations for visualization processors in Fire Insight:

* Set number of columns want to represent on y axis with respect to x axis
* Set chart type based on data type

.. figure:: ../../_assets/ml_userguide/visualization_configurations.PNG
   :alt: ml_userguide
   :width: 90%

Output result of ``Visualization`` processor:

Charts : LineGraph
==================

.. figure:: ../../_assets/ml_userguide/visual_result.PNG
   :alt: ml_userguide
   :width: 90%


Charts : BarChart
==================


.. figure:: ../../_assets/ml_userguide/barchart.png
   :alt: ml_userguide
   :width: 90%
   
Charts : ColumnChart
==================

.. figure:: ../../_assets/ml_userguide/column.png
   :alt: ml_userguide
   :width: 90%
