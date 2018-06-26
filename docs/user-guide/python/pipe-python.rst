Pipe Python Processor
=====================

Sparkflows has a Pipe Python Processor.

It pipes the incoming DataFrame through pipe to the Python Script.

The Python script is written in the Workflow Editor.

DataFrame Schema
----------------

The schema of the dataframe is also passed into the Python script as an argument. It can be used in the Python script as needed.

The format of the dataframe schema is below::

    colname1:datatype1|colname2:datatype2|colname3:datatype3
    
    
