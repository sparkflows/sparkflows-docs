Count
=========== 

This node counts the number of records in the incoming Dataframe and puts the count into result page.

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
The incoming DataFrame is sent to the output

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCount

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - variable
        - Variable Name
        - Name of the Variable in which the count is stored
      * - printCount
        - PrintCount
        - Print the count into result page.


Details
-------


This node counts the number of records in the incoming Dataframe and puts the count into result page.

Variable Name to display count value and option to display it in the output can be specified in the node.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    LOCATION    |    DEPT         |    SALARY
-----------------------------------------------------------------------------
E01       |    DAVID       |    NEW YORK    |    HR           |    10000
E02       |    JOHN        |    NEW JERSEY  |    SALES        |    11000
E03       |    MARTIN      |    NEW YORK    |    MARKETING    |    12000
E04       |    TONY        |    NEW JERSEY  |    MARKETING    |    13000
E05       |    ROSS        |    NEW YORK    |    FRONT DESK   |    10000
E06       |    LISA        |    NEW JERSEY  |    FRONT DESK   |    11000
E07       |    PAUL        |    NEW YORK    |    MAINTENANCE  |    12000
E08       |    MARK        |    NEW JERSEY  |    MAINTENANCE  |    13000

if Count node is configured to display count value against [EMP_COUNT] variable then it would be displayed in the output as below:

EMP_COUNT      :    8
