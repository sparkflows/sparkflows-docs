Parse
======

Fire Insights provide processors that parse the values of the selected columns.


Parse Processors in Fire Insights
----------------------------------------


.. list-table:: Parse Processors
   :widths: 50 50
   :header-rows: 1

   * - Title
     - Description
   * - Apache Logs
     - Reads in Apache Log files from a given path, parses them, and loads them into a DataFrame
   * - Field Splitter
     - This node splits the string of the specified input column using the specified delimiter
   * - Fixed Length Fields
     - Fixed Length for the selected columns 
   * - Multi Regex Extractor
     - This node extract pattern from input columns
   * - OCR
     - Performs Optical Character Recognition using the Tesseract library
   * - Parse JSON Col
     - Parses JSON content in a given Col
   * - Regex Tokenizer
     - This node creates a new DataFrame by the process of taking text (such as a sentence) and breaking it into individual terms (usually words) based on regular express  
