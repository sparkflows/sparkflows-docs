Python Integration
===================

Sparkflows supports Python in Workflows in a few ways:

.. panels::
    :container: container-lg pb-3
    
    :doc:`/user-guide/python/pyspark`

    The PySpark Processor allows writing PySpark or Python code to processes the incoming DataFrame and create a new DataFrame. It can also be used to build scikit-learn models act.

    ---

    :doc:`/user-guide/python/jython`
    
    The Jython Processor allows writing Jython code to processes the incoming DataFrame and create a new DataFrame.

    ---

    :doc:`/user-guide/python/pipe-python2`
    
    The Pipe Python Processor pipes the incoming DataFrame through pipe to the Python Script. It also passes the Schema of the DataFrame to the Python script through the command line argument. (argv[1])


.. toctree::
   :hidden:

   pyspark.rst
   jython.rst
   pipe-python.rst
   pipe-python2.rst

