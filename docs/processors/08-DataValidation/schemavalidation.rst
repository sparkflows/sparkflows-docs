Node Schema Validation
=========== 

This node to do the defined schema validation.

Type
--------- 

transform

Class
--------- 

fire.nodes.validation.NodeSchemaValidation

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - validation
        - Validation
        - Column Name, Column Type, Required & Default Value to check separated by ,


Details
-------


This node compares schema of the incoming Dataframe against one defined in the node and creates two outgoing DataFrames

*  schema validation Dataframe
*  Dataframe after imputing default values.  


Validation definition for multiple columns can be entered in separate row.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
string    |    string      |    string  |    string    |    integer    
------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40
E02       |    LISA        |    HR      |              |    35
E03       |    MARTIN      |            |    20000     |    25
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |      
E06       |    JOE         |    SALES   |    40000     |      
E07       |    BELLA       |    HR      |    60000     |    24

if following Validation Rules are defined in SchemaValidation node:
EMP_NAME,string,true,NO NAME
DEPT,string,true,ORG EMPLOYEE
SALARY,integer,false,1
AGE,integer,true,25

then outgoing Dataframes would be created as below:

 SchemaValidation created after comparing Schema of incoming Dataframe against Rules defined
+++++++++++++++

Column Name    |    Column Type    |    Input Column Type
--------------------------------------------------------------
EMP_NAME       |    string         |    string
DEPT           |    string         |    string
SALARY         |    string         |    integer
AGE            |    integer        |    integer

 outgoing Dataframe created after imputing missing values with Default values mentioned in Validation Rules
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT                |    SALARY    |    AGE    
---------------------------------------------------------------------------------
string    |    string      |    string              |    string    |    integer    
---------------------------------------------------------------------------------
E01       |    ANTHONY     |    HR                  |    50000     |    40
E02       |    LISA        |    HR                  |    1         |    35
E03       |    MARTIN      |    ORG EMPLOYEE        |    20000     |    25
E04       |    DAVID       |    SALES               |    55000     |    40
E05       |    MARK        |    SALES               |    60000     |    25  
E06       |    JOE         |    SALES               |    40000     |    25  
E07       |    BELLA       |    HR                  |    60000     |    24
