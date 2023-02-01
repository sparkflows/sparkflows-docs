Python
===========

Fire Insights supports both Java/Scala and Python engines.

When using the python engine, python 3.6+ has to be present. Also the dependent packages need to be installed.

Below are some helpful python commands.

Check python version
----------------

::


    python --version
    python3 --version


List all the python packages
--------------------

::

    pip list
    

Install python packages
---------------

::

    pip install -r requirements.txt
    
    
Remove all the wheel files in the cache
---------------------------

::


    pip cache purge

Customized python library installation
----

::

  
    pip install (python_library)==1.2.0
