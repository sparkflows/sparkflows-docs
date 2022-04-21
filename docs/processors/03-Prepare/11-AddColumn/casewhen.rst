Case When
=========== 

Sets values based on conditions

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCaseWhen

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCol
        - Output Column Name
        - output column name
      * - whenConditions
        - When Condition
        - When Condition
      * - values
        - Value
        - Value when this condition is true
      * - finallyElse
        - Else
        - else


Details
-------


This node creates a new Dataframe with new output column appended to the incoming dataframe.

Value of the new column is set based on the Condition met and corresponding value fetched.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    PERFORMANCE     |    SALARY    
------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    GOOD            |    12000     
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    VERY GOOD       |    11000     
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    AVERAGE         |    34000     
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    VERY VERY GOOD  |    12500     
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    BAD             |    78999     

if CaseWhen node is configured as below to compute values for the output column:

WHEN CONDITION                        |        VALUE 	
------------------------------------------------------------------
SALARY < 12500                        |        'FIRST_GRADE'
SALARY>= 12500 AND SALARY < 30000     |        'SECOND_GRADE'
SALARY >- 30000 AND SALARY < 70000    |        'THIRD_GRADE'
ELSE                                  |        'FOURTH_GRADE'

[ELSE] is the default condition processed if no other condition is met

then output Dataframe would be created as below where value of [SALARY] is compared against [WHEN CONDITION] and [VALUE] is fetched for the output column [SALARY_GRADE]:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    PERFORMANCE     |    SALARY    |    SALARY_GRADE
---------------------------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    GOOD            |    12000     |    FIRST_GRADE
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    VERY GOOD       |    11000     |    FIRST_GRADE
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    AVERAGE         |    34000     |    THIRD_GRADE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    VERY VERY GOOD  |    12500     |    SECOND_GRADE
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    BAD             |    78999     |    FOURTH_GRADE
