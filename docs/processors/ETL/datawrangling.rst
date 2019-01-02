DataWrangling
=========== 

This node creates a new DataFrame by applying each of the Rules specified

Input
--------------
It takes in a DataFrame as Input

Output
--------------
It creates the output DataFrame by applying the data wrangling rules provided

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDataWrangling

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - rules
        - Rules
        - Rules to be applied on column and rows


Details
======


Rename one column to another
rename col:c1 to c2;

Drop Column
drop col:col4

Delete columns with some condition
delete col:col3 > 44

Substring col:col2 0,3
get substring between 0 and 3rd column from the column col2

Trim Values : Removes leading and trailing whitespace from a string value. 

set col:Name value: trim(Name)

Sets the new value of Name column to be trim(Name)


