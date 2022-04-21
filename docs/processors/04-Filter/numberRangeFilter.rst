Filter By Number Range
=========== 

This node filter Rows in the given Number Range

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFilterByNumberRange

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column Name
        - input column name
      * - lowestValue
        - Lowest Value
        - input lowest value
      * - highestValue
        - Highest Value
        - input highest value


Details
-------


This node filters Rows in the given Number Range.

New outgoing Dataframe is created based on filtered rows and it is passed to next node.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40
E02       |    LISA        |    HR      |    50000     |    35
E03       |    MARTIN      |    HR      |    20000     |    25
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |    45
E06       |    JOE         |    SALES   |    40000     |    25
E07       |    BELLA       |    HR      |    60000     |    24

If FilterByNumberRange node is configured as below:

INPUT COLUMN NAME    :    AGE
LOWEST VALUE         :    35
HIGHEST VALUE        :    45

then outgoing Dataframe would be created as below with rows falling in the given number range:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40
E02       |    LISA        |    HR      |    50000     |    35
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |    45
