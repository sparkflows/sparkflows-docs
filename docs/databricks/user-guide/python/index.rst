Python Integration
===================

Sparkflows supports Python in Workflows in a few ways:

.. panels::
    :container: container-lg pb-3
    
    :doc:`/user-guide/python/pyspark`

    The PySpark Processor allows writing PySpark/Python code to processes the incoming DataFrame and create a new DataFrame. It can also be used to build scikit-learn models act.

    ---

    :doc:`/user-guide/python/jython`
    
    The Jython Processor allows writing Jython code to processes the incoming DataFrame and create a new DataFrame.

    ---

    :doc:`/user-guide/python/pipe-python`

    Pipe Python Processor allows writing Python script to process the incoming DataFrame. The incoming DataFrame is piped to the python script. The Python script takes in each     record of the DataFrame as a comma separated string. It parses the string, processes the record and writes out the new record.
    
    ---
    
    :doc:`/user-guide/python/pipe-python2`
    
    It pipes the incoming DataFrame through pipe to the Python Script. It also passes the Schema of the DataFrame to the Python script through the command line argument. (argv[1])


.. toctree::
   :hidden:

   pyspark.rst
   jython.rst
   pipe-python.rst
   pipe-python2.rst

