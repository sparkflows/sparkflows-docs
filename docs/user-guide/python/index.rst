Python support in Sparkflows
============================

Sparkflows supports Python in Workflows in a couple of ways:

* Jython Processor

The Jython Processor allows writing Jython code to processes the incoming DataFrame and create a new DataFrame.

* Pipe Python Processor

Pipe Python Processor allows writing Python script to process the incoming DataFrame.

The incoming DataFrame is piped to the python script.

The Python script takes in each record of the DataFrame as a comma separated string. It parses the string, processes the record and writes out the new record.


.. toctree::
   :maxdepth: 2

   jython.rst
   pipe-python.rst

