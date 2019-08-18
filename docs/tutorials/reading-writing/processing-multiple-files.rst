Processing multiple files
=========================

This workflow reads in multiple files available in specific directory. It then filters and calculates number of bedrooms with specific prices and then prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads multiple csv files available in specific directory.
* Filters it to calculate number of bedrooms with specific prices.
* Prints the results.

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/1.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60%
   
Reading CSV files
---------------------

It reads multiple CSV files available in specific directory using ReadCSV processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/8.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/3.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60%

Filter its data
----------------

It then filters to calculate number of bedrooms with specific prices using SQL processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/4.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/5.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60%   
   
Print the results
------------------

It will print the results with the output required after filter aggregation.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/6.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60% 
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/7.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60% 
