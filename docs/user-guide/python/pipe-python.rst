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
    
    
Pandas Example
--------------

Below is an example script which reads in the input lines and converts it to a Pandas Dataframe.

```

#!/usr/bin/python

import sys
import pandas as pd

dataframe_list_of_rows = []
schema = ""
for line_with_data_schema in sys.stdin:

    line_with_data_schema = line_with_data_schema.strip()
    if not line_with_data_schema:
        continue

    line_with_data_schema_split = line_with_data_schema.split("\t")  # split on space
    line = line_with_data_schema_split[0]     # the actual data line
    schema = line_with_data_schema_split[1]   # in the format -  col1:datatype1|col2:datatype2|col3:datatype3

    row_list = []
    for field in line.split(","):
        row_list.append(field)

    # convert list to tuple
    row_tuple = tuple(row_list)
    dataframe_list_of_rows.append(row_tuple)


# generate column names
column_names = []
schema_columns = schema.split("|")
for column_name_with_type in schema_columns:
    column_name_with_type_split = column_name_with_type.split(":")
    column_names.append(column_name_with_type_split[0])
    
```

