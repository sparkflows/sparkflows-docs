Processing Multiple Files
=========================

This workflow reads in multiple files available in a specific directory. It then filters and calculates the number of bedrooms with specific prices and then prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads multiple CSV files available in a specific directory.
* Filters it to calculate the number of bedrooms with specific prices.
* Prints the results.

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/1.PNG
   :alt: Housing Analysis
   :width: 80%
   
Reading CSV files
---------------------

It reads multiple CSV files available in a specific directory using the ReadCSV processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/8.PNG
   :alt: Housing Analysis
   :width: 80%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/3.PNG
   :alt: Housing Analysis
   :width: 80%

Filter its data
----------------

It then filters to calculate the number of bedrooms with specific prices using an SQL processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/4.PNG
   :alt: Housing Analysis
   :width: 80%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/5.PNG
   :alt: Housing Analysis
   :width: 80%   
   
Print the results
------------------

It will print the results with the output required after filter aggregation.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/6.PNG
   :alt: Housing Analysis
   :width: 80% 
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/7.PNG
   :alt: Housing Analysis
   :width: 80%
