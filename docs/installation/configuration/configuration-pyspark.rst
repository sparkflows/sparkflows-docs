PySpark Configuration
========

Sparkflows can be configured to use the PySpark engine and create workflow using it.

Below are the Prerequisites before configuring PySpark engine in Sparkflows:

::

    Python 3.7+ 
    
    
Install the required python dependencies.

::

    cd fire-x.y.x/dist/fire
    pip install -r requirements.txt
    
''requirements.txt'' file is available in the installation directory of Sparkflows:

::

    fire-x.y.x/dist/fire/requirements.txt    
    
Once the above dependency gets installed successfully, Login to Sparkflows webserver URL and go inside ''ADMINISTRATIONS -->> Configurations'' and update following parameters:

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

