Processing Multiple Files
=========================

This workflow reads in multiple files available in a specific directory. It then filters and calculates the number of bedrooms with specific prices and then prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads multiple CSV files available in a specific directory.
* Filters it to calculate the number of bedrooms with specific prices.
* Prints the results.

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/MultiCSV.png
   :alt: Housing Analysis
   :width: 50%
   
Reading CSV files
---------------------

It reads multiple CSV files available in a specific directory using the ReadCSV processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/10.PNG
   :alt: Housing Analysis
   :width: 60%

Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/11.PNG
   :alt: Housing Analysis
   :width: 60%

Filter its data
----------------

It then filters to calculate the number of bedrooms with specific prices using an SQL processor.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/12.PNG
   :alt: Housing Analysis
   :width: 60%
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/13.PNG
   :alt: Housing Analysis
   :width: 60%   
   
Print the results
------------------

It will print the results with the output required after filter aggregation.

Processor Configuration
^^^^^^^^^^^^^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/14.PNG
   :alt: Housing Analysis
   :width: 60% 
   
Processor Output
^^^^^^

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/15.PNG
   :alt: Housing Analysis
   :width: 60%
