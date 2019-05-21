Python
======

Sparkflows supports Python in Workflows in a few ways:

* PySpark Processor

The PySpark Processor allows writing PySpark/Python code to processes the incoming DataFrame and create a new DataFrame.
It can also be used to build scikit-learn models etc.

* Jython Processor

The Jython Processor allows writing Jython code to processes the incoming DataFrame and create a new DataFrame.

* Pipe Python Processor

Pipe Python Processor allows writing Python script to process the incoming DataFrame.

The incoming DataFrame is piped to the python script.

The Python script takes in each record of the DataFrame as a comma separated string. It parses the string, processes the record and writes out the new record.


.. toctree::
   :maxdepth: 2

   pyspark.rst
   jython.rst
   pipe-python.rst
   pipe-python2.rst

