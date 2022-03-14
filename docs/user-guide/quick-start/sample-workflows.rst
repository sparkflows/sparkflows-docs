Sample Workflows
==========

Fire Insights provide an array of sample workflows to showcase capabilities and usage of processors.

These workflows are bundled together in following projects that can be accessed in Sample Projects tab.

Data Preparation Project
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Workflow Name
     - Description
   * - DateTimeFieldExtract
     - Extraction of Year, Month, Day of month, Hour, Minute, Second values from incoming column of TimeStamp datatype using DataTimeFieldExtract node. 
   * - Columns Rename
     - Renames incoming columns using ColumnsRename node.
   * - Remove Special Characters
     - It searches for a String Pattern in incoming dataset and replaces it with another using FindAndReplaceUsingRegex node. Find and Replace is performed using Regex pattern match. 
   * - Data Preparation - 1
     -   -	Convers a String value to Date using MultiStringToDate node
	      
         -	Evaluates multiple conditional expressions to compute value using CaseWhen node. 	
	      
         -	Filters incoming dataset using RowFilter node. 	
   * - Column Filter
     - Creates output dataset by selecting a set of columns from incoming dataset. 
   * - Remove Duplicate Rows
     - Removes duplicate rows from incoming dataset based on combination of values present in selected columns. 
   * - Titanic Data Cleaning
     -   -	Drop rows having null values using DropRowsWithNull node
	      
         -	Filters rows having data length for selected column within a given range using FilterByStringLength.
	      
         -	Converts datatype of selected columns to specified type using CastColumnType node.
         
         -	Filters rows using specified Conditional Expression using RowFilter node.
   * - OCR
     - This workflow uses OCR node to read binary file containing OCR data by performing Optical Character Recognition using the Tesseract Library. 
   * - String Functions
     - This workflow performs variouss transformation such as converting data to Upper Case and Trimming incoming data using StringFunctionsMultiple node.
   * - REST Read and Parse JSON
     - This workflow parses single record JSON from specified URL location and creates an output dataset using URLSingleRecordJSONReader node.
   * - REST - CSV Reader and Parse
     -   -	Reads a Text file from the URL location provided using URLTextFileReader node.
     
         -	Splits data present in a column using a separator to multiple fields using FieldSplitter node. 	
      
         -	Selects Rows having specified Index values using RowFilterByIndex node. 	

   * - Profiling - Correlation
     - 	-	Displays correlation between selected columns using Correlation node.
     
     	-	Displays Summary of selected incoming column data by calculating and printing spreads such as Count, Mean, Min, Max and so on.
   * - Data Cleaning
     - 	-	Imputin missing values with constants. Each column can be configured for imputing.
     
     	-	Converts String Categorical data to Index value as a part of Feature Engineering.
	
	-	Evaluates a conditional expression to compute values using CaseWhen node.
	
	-	Evaluates a Regex expression to find and replace a string pattern using FindAndReplaceUsingRegexMultiple node.
   * - Drop Rows With Null
     - Drop rows having null values using DropRowsWithNull node.
   * - Dedup Customers
     - Compares and identifies whether data from multiple sources refer to same entity or not using Dedup node. Dedup node can be configured to used specific algorithm to compare.
   * - Data Wrangling
     - Performs multiple transformation on incoming data using DataWrangling node. Some of the transformation performed are Substring, Dropping a column, Renaming a column, Changing Case of a column and so on.
   * - Data Validation
     - Validates incoming data whether it looks ok or not. Some of the validation checks that are performed are to check whether Address data is a valid US address or not, email data is a valid email address or not.
   * - Convert to Timestamp
     - Converts a String value to Timestamp value using StringToDate node. 
   * - Concat Columns
     - Joins data from multiple columns into one output column using ConcatColumns node. Data from different columns are separated uisng a Separator in the output. 
