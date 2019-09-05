Split With Stratified Sampling
=========== 

This node splits the incoming DataFrame into 2. It takes in the fraction to use in splitting the data by Stratified Sampling.

Input
--------------
It takes in a DataFrame as input

Output
--------------
The input DataFrame is split into 2 DataFrames and output

Type
--------- 

transform

Class
--------- 

fire.nodes.util.SplitWithStratifiedSampling

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - keyInputCol
        - Column Name
        - column that defines strata
      * - fraction
        - Fraction
        - sampling fraction for each stratum. If a stratum is not specified, we treat its fraction as zero
      * - seed
        - Seed
        - random seed


Details
-------


Split With Stratified Sampling, which is the preferred way to sample from populations with varing subpopulation sizes.

More details are available at : https://spark.apache.org/docs/latest/api/python/_modules/pyspark/sql/dataframe.html#DataFrame.sampleBy


