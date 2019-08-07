Housing-Analysis
=================

This workflow reads in multiple files available in specific directory, It then filter it to aggregate number of bedrooms with specific prices and then prints the results.

Workflow
-------

Below is the workflow. It does the following:

* Reads multiple csv files available in specific directory.
* Filter it to aggregate number of bedrooms with specific prices.
* Prints the results.

.. figure:: ../../_assets/tutorials/analytics/housing-analysis/1.PNG
   :alt: Housing Analysis
   :align: center
   :width: 60%
   
Reading from Dataset
---------------------

It reads multiple csv files available in specific directory.

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
^^^^^^^^^^^^^^^^
It then filter to aggregate number of bedrooms with specific prices using SQL processor.

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
   
Prints the results
------------------

It will print the result with the output required after filter aggregations.

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




