PySpark Configuration
========

Sparkflows can be configured to use the PySpark engine and create workflow using it.

Login to Sparkflows webserver URL and goto ``ADMINISTRATIONS`` -> ``Configurations`` and update following parameters:

::

    module.workflowTypes = both
    

.. figure:: ../../_assets/installation/pyspark_configurations.PNG
   :alt: pyspark
   :width: 60%
    
Once the above configuration is updated and changes are saved, you need to refresh the Sparkflows webserver URL to verify the latest configuration changes.

Now open any project and select workflows tab, clicking on ''Create'' button will show you option to create workflow using PySpark engine.

.. figure:: ../../_assets/installation/pyspark_wf.PNG
   :alt: pyspark
   :width: 60%


.. Note:: Make sure to install all Sparkflows python dependencies.
