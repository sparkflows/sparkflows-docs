Remove Unwanted Characters Multiple
=========== 

This node removes unwanted characters

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRemoveUnwantedCharactersMultiple

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Columns
        - Input columns
      * - removeWhitespaces
        - Remove Whitespaces
        - Removes white space
      * - removeLetters
        - Remove Letters
        - Removes letters
      * - removeDigits
        - Remove Digits
        - Removes digits
      * - removeSigns
        - Remove Signs
        - Removes signs
      * - removeCommas
        - Remove Commas
        - Removes commas


Details
-------


This node removes unwanted characters from the specified input columns


Examples
-------


Incoming Dataframe has following row:

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | $12,500.00 |  Salary hiked by 10%

If removeunwantedcharactersmultiple is configured to remove unwanted characters [SIGNS] & [COMMAS] from [SALARY] & [DIGITS] and [SIGNS] from [COMMENTS] columns 
then outgoing Dataframe would result as below:

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | 1250000    |  Salary hiked by 

Below examples detail how data is processed based on selected options

REMOVE WHITESPACES is selected as [True]
+++++++++++++++

Whitespaces are removed from the selected columns [SALARY] and [COMMENTS]

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | $12,500.00 |  Salaryhikedby10%
 
REMOVE LETTERS is selected as [True]
+++++++++++++++

Alphabets are removed from the selected columns [SALARY] and [COMMENTS]

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | $12,500.00 |  10%

REMOVE DIGITS is selected as [True]
+++++++++++++++

Numbers are removed from the selected columns [SALARY] and [COMMENTS]

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | $,.        |  Salary hiked by %
 
REMOVE SIGNS is selected as [True]
+++++++++++++++

Special characters are removed from the selected columns [SALARY] and [COMMENTS]

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | 1250000    |  Salary hiked by 10
 
REMOVE COMMAS is selected as [True]
+++++++++++++++

Commas are removed from the selected columns [SALARY] and [COMMENTS]

 CUST_CD  |  CUST_NAME  |  SALARY    |    COMMENTS          
-------------------------------------------------------------
 C01      |  MIKE       | $12500.00  |  Salary hiked by 10%
