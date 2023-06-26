Sample Workflows
==========

Fire Insights provides an array of sample workflows to showcase capabilities and usage of processors.

These workflows are bundled together in the following projects that can be accessed in Sample Projects tab.

Data Preparation Project
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Workflow Name
     - Description
   * - Column Filter
     - -  Creates output dataset by selecting a set of columns from incoming dataset. 
   * - Columns Rename
     - - Renames incoming columns using ColumnsRename node.
   * - Concat Columns
     - - Joins data from multiple columns into one output column using ConcatColumns node. Data from different columns are separated uisng a Separator in the output.       
   * - Convert to Timestamp
     - - Converts a String value to Timestamp value using StringToDate node.     
   * - DateTimeFieldExtract
     - - Extraction of Year, Month, Day of month, Hour, Minute, Second values from incoming column of TimeStamp datatype using DataTimeFieldExtract node. 
   * - Data Preparation
     -   -	Converts a String value to Date using MultiStringToDate node.
	      
         -	Evaluates multiple conditional expressions to compute value using CaseWhen node. 	
	      
         -	Filters incoming dataset using RowFilter node.    
   * - Data Cleaning
     - 	-	Imputing missing values with constants. Each column can be configured for imputing.
     
     	-	Converts String Categorical data to Index value as a part of Feature Engineering.
	
	-	Evaluates a conditional expression to compute values using CaseWhen node.
	
	-	Evaluates a Regex expression to find and replace a string pattern using FindAndReplaceUsingRegexMultiple node.
   * - Data Wrangling
     - - Performs multiple transformation on incoming data using DataWrangling node. Some of the transformation performed are Substring, Dropping a column, Renaming a column, Changing Case of a column and so on.
   * - Data Validation
     - - Validates incoming data whether it looks ok or not. Some of the validation checks that are performed are to check whether Address data is a valid US address or not, email data is a valid email address or not.	
   * - Dedup Customers
     - - Compares and identifies whether data from multiple sources refer to same entity or not using Dedup node. Dedup node can be configured to used specific algorithm to compare.      
   * - Drop Rows With Null
     - - Drop rows having null values using DropRowsWithNull node.    
   * - OCR
     - - This workflow uses OCR node to read binary file containing OCR data by performing Optical Character Recognition using the Tesseract Library. 	
   * - Profiling - Correlation
     - 	-	Displays correlation between selected columns using Correlation node.
     
     	-	Displays Summary of selected incoming column data by calculating and printing spreads such as Count, Mean, Min, Max and so on.     
   * - - Remove Special Characters
     - - It searches for a String Pattern in incoming dataset and replaces it with another using FindAndReplaceUsingRegex node. Find and Replace is performed using Regex pattern match. 	
   * - Remove Duplicate Rows
     - - Removes duplicate rows from incoming dataset based on combination of values present in selected columns. 
   * - REST - Read and Parse JSON
     - - This workflow parses single record JSON from specified URL location and creates an output dataset using URLSingleRecordJSONReader node.
   * - REST - CSV Reader and Parse
     -   -	Reads a Text file from the URL location provided using URLTextFileReader node.
     
         -	Splits data present in a column using a separator to multiple fields using FieldSplitter node. 	
      
         -	Selects Rows having specified Index values using RowFilterByIndex node. 
   * - String Functions
     - - This workflow performs various transformation such as converting data to Upper Case and Trimming incoming data using StringFunctionsMultiple node.
   * - Titanic Data Cleaning
     -   -	Drop rows having null values using DropRowsWithNull node.
	      
         -	Filters rows having data length for selected column within a given range using FilterByStringLength.
	      
         -	Converts datatype of selected columns to specified type using CastColumnType node.
         
         -	Filters rows using specified Conditional Expression using RowFilter node.


Data Quality Project
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Workflow Name
     - Description
   * - Employee - Data Cleaning and Data Quality
     -	-	Performs data transformation such as Text Case change to Upper and Lower using StringFunctionMultiple node.
     
     	-	Converts incoming data to desired value by executing Case When statement in SQL Node.
	
	-	Performs various data validations.
	
   * - Employee - Data Profiling
     - 	-	Displays Summary of selected incoming column data by calculating and printing spreads such as Count, Mean, Min, Max and so on.
     
     	-	Identifies coorelation between selected columns using Coorelation node.
	
	-	Plots distribution of data for different Gender value using GraphGroupByColumn node.
	
	-	Plots distribution of data for different City value using GraphGroupByColumn node.
	
	-	Plots yearly distribution of data for different Date Of Birth value using GraphYearDistribution node.	
		
   * - Request Correlation Summary Validation
     - 	-	Identifies coorelation between selected columns using Coorelation node.
     
     	-	Displays Summary of selected incoming column data by calculating and printing spreads such as Count, Mean, Min, Max and so on.
	
	-	Validates whether email address in the incoming dataset is a valid one or not.
		

Read Write Files Project
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Workflow Name
     - Description
   * - PDF Image OCR
     - - Reads incoming PDF file containing OCR image using ReadPDFImageOCR node.
     
   * - Retail example
     - - Reads incoming JSON files using ReadJSON node.
		
   * - Read PDF File
     - - Reads incoming PDF file using ReadPDF node.
     
   * - Read Parquet File
     - - Reads incoming dataset in Parquet format.
	 
   * - Read Multi-line JSON
     - - Reads incoming Multi-Line JSON file using ReadJSON node with Multiline flag set to True.
	 
   * - Read Excel File
     - - Reads incoming Excel file using ReadExcel node.     
		
   * - Save As Parquet Files
     - - Saves dataset in Parquet format using SaveParquet node.
	 
   * - Save As JSON Files
     - - Saves dataset in JSON format using SaveJSON node.
	 
		
Visualization Project
----------------------------------------


.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Workflow Name
     - Description
   * - BoxPlot & SubPlots
     - 	-	Plots distribution of data for Churn values using GraphGroupByColumn node.
     
     	-	Plots variation of data between multiple data series using GraphValues node.
	
	-	Dipicts variation between multiple pairs of data series in separate chart using GraphSubPlots node.
	
	-	Plots variation between two data series in Box Chart format using BoxPlot node.     
		
   * - Churn Data Analysis
     - 	-	Displays Summary of selected incoming column data by calculating and printing spreads such as Count, Mean, Min, Max and so on.
     
     	-	Identifies coorelation between selected columns using Coorelation node.
	
	-	Plots distribution of data for Churn values using GraphGroupByColumn node.
	
	-	Plots variation of data between multiple data series using GraphValues node.
		
   * - DistributionGraphs
     - 	-	Plots yearly distribution of two data series using GraphYearDistribution node.
     
     	-	Plots monthly distribution of two data series using GraphMonthDistribution node.
	
	-	Plots week day distribution of two data series using GraphWeekDayDistribution node.
	
   * - Graph column values by count
     - - Plots distribution of data across various categories in Bar Chart, Line Chart and Histogram Chart format using GraphGroupByColumn node.	
		
   * - NYC Taxi Average Speed
     - 	-	Extracts Hour and Minute values from incoming data using DateTimeFieldExtract node.
     
     	-	Executes a SQL statement using SQL node.
	
	-	Aggregates data using GroupBy node.
	
	-	Sorts incoming data using Sort node.
	
	-	Plots variation of data between multiple data series using GraphValues node.
	 
   * - Train Data - Graph values
     - - Plots variation of data between multiple data series in various formats using GraphValues node.
	 	
