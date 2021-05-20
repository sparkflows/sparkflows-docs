Data Cleaning
==========

Fire Insights provide powerful capabilities for data cleanup.


Data Cleaning Processors in Fire Insights
----------------------------------------


.. list-table:: Data Cleaning Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Dedup
     - This node is used for problems like entity resolution or data matching. Entity resolution or Data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources
   * - Drop Duplicate Rows
     - When the user doesn't select any column, returns a new dataset that contains only the unique rows from this Dataset. Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
   * - Drop Rows With Null
     - This node creates a new DataFrame by dropping rows containing null values
   * - Find And Replace Using Regex
     - This node finds and replaces text in a column containing a string
   * - Find And Replace Using Regex Multiple
     - This node finds and replaces text in a column containing a string
   * - Remove Duplicate Rows
     - This node takes an array of fields, compares rows in those fields. If they full match, then it's a match. From the matches, it would randomly take one row and drop the rest.
   * - Remove Unwanted Characters
     - This node removes unwanted characters
   * - Remove Unwanted Characters Multiple
     - This node removes unwanted characters
 
