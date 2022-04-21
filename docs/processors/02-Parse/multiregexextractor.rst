Multi Regex Extractor
=========== 

This node to extract pattren from input columns

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node extract pattren from input columns as specified

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMultiRegexExtractor

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColNames
        - InputColumnsName
        - Columns
      * - outputColNames
        - OuputColumnsName
        - name of the output column
      * - patterns
        - Patterns
        - patterns or regex to extract the input column name
      * - groups
        - Groups
        - An regular expression group number starting with 1, defining which portion of the matching string will be returned


Details
-------


This node extracts data from columns present in the incoming Dataframe based on provided pattern and add them as new columns in outgoing Dataframe.


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY
-------------------------------------------------------------------------------------
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00

If MultiRegexExtractor node is configured to extract data based on patterns as mentioned below:

INPUTCOLUMNSNAME    |    OUPUTCOLUMNSNAME    |    PATTERNS    |    GROUPS 	
---------------------------------------------------------------------------
CUST_CD             |    Cust_ID             |    \d{1,2}     |    0
DATE_OF_JOINING     |    DOJ_Year            |    \d{4}       |    0
SALARY              |    Currency            |    \w{3}       |    0

then outgoing Dataframe would be created as below:

CUST_CD    |    CUST_NAME    |    AGE    |    DATE_OF_JOINING    |    SALARY         |    Cust_ID    |    DOJ_Year    |    Currency
------------------------------------------------------------------------------------------------------------------------------------
C01        |    MATT         |    50     |    12-02-2002         |    USD 200000.00  |    01         |    2002        |    USD
C02        |    LISA         |    45     |    15-11-2020         |    GBP 100000.00  |    02         |    2020        |    GBP
C03        |    ROBIN        |    30     |    10-10-2015         |    EUR 15000.00   |    03         |    2015        |    EUR
C04        |    MARCUS       |    35     |    01-01-2021         |    AUD 350000.00  |    04         |    2021        |    AUD
