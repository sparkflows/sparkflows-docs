Pipe Python Processor
=====================

Sparkflows has a Pipe Python Processor.

It pipes the incoming DataFrame through pipe to the Python Script.

The Python script is written in the Workflow Editor.

DataFrame Schema
----------------

The schema of the dataframe is also passed into the Python script as an ``argument``. It can be used in the Python script as needed.

The format of the dataframe schema is below::

    colname1:datatype1|colname2:datatype2|colname3:datatype3
    
Below is an example of printing the arguments and an example result::

    print "The arguments are: " , str(sys.argv)

    ['/tmp/fire/scripts/pipepython-1899418263068404925.py', 'id:DoubleType|label:DoubleType|f1:DoubleType|f2:DoubleType']
    
Simple Example
--------------

The below example reads in the incoming records, parses them, adds a new column whose value is the sum of the first and second fields. Finally it write out the updated record back for Spark to read::

    #!/usr/bin/python

    import sys

    for line in sys.stdin:
      line = line.strip()
      if not line:
        continue

      fields = line.split(",")

      total = str(float(fields[0]) + float(fields[1]))

      result = ",".join(fields) + "," + total

      print result
      print "The arguments are: " , str(sys.argv)
  
    
Pandas Example
--------------

Below is an example script which reads in the input lines and converts it to a Pandas Dataframe. It parses the schema passed in argv[1] to extract the column names::

    #!/usr/bin/python

    import sys
    import pandas as pd

    dataframe_list_of_rows = []

    for line in sys.stdin:

        line = line.strip()
        if not line:
            continue

        row_list = []
        for field in line.split(","):
            row_list.append(field)

        # convert list to tuple
        row_tuple = tuple(row_list)
        dataframe_list_of_rows.append(row_tuple)


    # generate column names
    schema = sys.argv[1]
    column_names = []
    schema_columns = schema.split("|")
    for column_name_with_type in schema_columns:
        column_name_with_type_split = column_name_with_type.split(":")
        column_names.append(column_name_with_type_split[0])

    # create dataframe from the input rows
    input_dataframe = pd.DataFrame.from_records(dataframe_list_of_rows, columns=column_names)

