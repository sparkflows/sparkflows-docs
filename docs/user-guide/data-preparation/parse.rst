Parse
======

Fire Insights provide processors that parse the values of the selected columns.


Parse Processors in Fire Insights
----------------------------------------


.. list-table:: Parse Processors
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Apache Logs
     - Reads in Apache Log files from a given path, parses them, and loads them into a DataFrame
   * - Field Splitter
     - This node splits the string of the specified input column using the specified delimiter
   * - Fixed Length Fields
     - It extracts data of fixed length from a column and appends them as new columns to the outgoing Dataframe.
   * - Multi Regex Extractor
     - It extracts data from columns based on provided pattern and adds them as new columns in outgoing Dataframe.
   * - OCR
     - Performs Optical Character Recognition using the Tesseract library
   * - Parse JSON Col
     - It parses JSON data present in a column and extracts data. Extracted data are appended as new columns in the outgoing Dataframe.
   * - Regex Tokenizer
     - This node creates a new DataFrame by the process of taking text (such as a sentence) and breaking it into individual terms (usually words) based on regex expressions  
