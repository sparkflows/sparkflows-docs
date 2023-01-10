Time Series Visualizations
--------------------------

Visualizing time series data can be a powerful way to uncover patterns and trends in the data. There are several different types of visualizations that are commonly used for time series data.

Fire Insights provides a number of Processors for the visualization of the time series data.

.. list-table:: Update New features where needed
   :widths: 10 40
   :header-rows: 1

   * - Charts
     - Description
   * - Line
     - A line chart, also known as a line plot, is a type of chart that is commonly used to display the trend of a variable over time. Line charts are often used for visualizing time series data, such as stock prices, weather data, or other types of data that change over time.
   * - Bar
     - A bar chart, also known as a bar plot, is a type of chart that is commonly used to display the distribution of a dataset.When working with time series data, a bar chart can be useful for showing the distribution of the data across different time periods, or to compare the values of a variable over different time periods.
   * - Scatter
     - Scatter plots are used to observe relationships between variables.  A scatter plot can be created for both univariate and multivariate data.
   * - Box plots
     - A box plot, also known as a box-and-whisker plot, is a type of chart commonly used to display the distribution of a dataset. A box plot can be created for both univariate and multivariate data. When working with time series data, a box plot can be useful for showing the distribution of the data across different time periods.
   * - Histogram
     - A histogram is a type of chart that is commonly used to display the distribution of a dataset. Like a box plot, a histogram can be created for both univariate and multivariate data.When working with time series data, a histogram can be useful for showing the distribution of the data across different time periods.

Charts : LineChart
==================

Line Charts are perfect for series of data points to form a continuous line.
For example it can be used to represent Daily sales data

Below is the sample workflow which contains ``Time Series data`` and outputs a line chart in Fire Insights.

   .. figure:: ../../_assets/ml_userguide/visual.PNG
      :alt: ml_userguide
      :width: 75%

Configurations for visualization processors in Fire Insight:

* Set number of columns want to represent on y axis with respect to x axis
* Set chart type based on data type

   .. figure:: ../../_assets/ml_userguide/visualization_configurations.PNG
      :alt: ml_userguide
      :width: 75%

Output result of ``Visualization`` processor:

Charts : LineGraph
==================

   .. figure:: ../../_assets/ml_userguide/visual_result.PNG
      :alt: ml_userguide
      :width: 75%


Charts : BarChart
==================


   .. figure:: ../../_assets/ml_userguide/barchart.png
      :alt: ml_userguide
      :width: 75%
   
Charts : ColumnChart
==================

   .. figure:: ../../_assets/ml_userguide/column.png
      :alt: ml_userguide
      :width: 75%
