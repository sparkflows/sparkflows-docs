Farmer's Market Prediction
=========================

It demonstrates to predict "the number of farmer's markets in a given zip code” based on the income and taxes paid in a given area using the past data. It seems plausible that areas with higher income have more farmer's markets simply because there is more of a market for those goods. Of course there are many potential holes in this idea, but that's the part of the desire to test it.

DataBricks has published a clean approach to build this use case. It features a Python notebook that demonstrates how to create ML Pipeline to preprocess a dataset, train a Machine Learning model and make predictions.

Using Fire Insights Visual Designer, you can try to execute this approach visually and declaratively. This note speaks to that.

As the DataBricks link highlights:

- The first of the two datasets that you can work on is the Farmer's Markets Directory and Geographic Data. This dataset contains information on the longitude and latitude, state, address, name, and zip code of the Farmer's Markets in the United States. The raw data is published by the Department of Agriculture. The version of the data that is found in Databricks (and is used in this tutorial) was updated by the Department of Agriculture on Dec 01, 2015.

- The second you can work on is the SOI Tax Stats - Individual Income Tax Statistics - ZIP Code Data (SOI). This study provides detailed tabulations of individual income tax return data at the state and zip code level and is provided by the IRS. This repository only has a sample of the data of 2013 and includes "AGI". The ZIP Code data shows selected income and tax items classified by state, zip code, and size of the adjusted gross income. The Data is based on individual income tax returns filed with the IRS and are available for Tax Years 1998, 2001, 2004 through 2013. The data includes items, such as:

   - Number of returns, which approximates the number of households.
   - Number of personal exemptions, which approximates the population.
   - Adjusted gross income.
   - Wages and salaries.
   - Dividends before exclusion.
   - Interest received.

Below is an overview of the workflow that you can create using the Fire Insights Visual Designer.

This workflow was simply created via the drag and drop capabilities of the Fire Insights Designer UI. The ability to construct this data processing pipeline (or any DAG - Distributed Acyclic Graph, for that matter) in a WYSIWYG Plug-and-Play manner is a key innovation to continue our community's collective march to on-demand-instant-analytics. The benefits include:

- It opens up the power of ETL and ML (such pre-packaged functionality is available as a catalog of "Nodes") to a wider audience of analysts and semi-technical resources.
- The actual execution can either be local (testing) or can be submitted to a Apache Spark cluster.
- You can see during the adoption that a single workbench improves collaborative iteration across data engineers, data scientists and analysts, which in turn accelerates time-to-market.
- As one might observe, the visual approach doubles up as workflow documentation and hence contributes in the solving of the data-lineage problem.

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/WF.png
   :alt: Fire Market Prediction
   :width: 65%
   
This workflow:

- **Uses the DatasetStructured Node:** Reads in the data from 2 different datasets - Farmer's Markets and Income Tax Return data per zip code (both are comma separated files).

  - Instead of a CSV, one can easily read it from a data-lake or a Persistence Store (HDFS/RDBMS/NoSQL).
  
- **Uses the ColumnFilter Node:** Filters out the following columns from the Income Tax Return dataset and passes it to a SQL query node, so that we can do further computation.
  
  - State
  - Zip code
  - MARS1 - Single Returns
  - MARS2 - Joint Returns
  - NUMDEP - Number of Dependents
  - A02650 - Tota Income Amount
  - A00300 - Taxable Interest Amount
  - A00900
  - A01000
  
- **Uses the SQL Node:** Execute the following SQL to get the various aggregates from the filtered data from the Income Tax Return dataset.
  
  - Select zipcode, sum(MARS1) as single_returns, sum(MARS2) as joint_returns, sum(NUMDEP) as numdep, sum(A02650) as total_income_amount, sum(A00300) as taxable_interest_amount from fire_temp_table group by zipcode.

- **Uses another SQL Node:** Extracts certain columns from the Farmer's_Market dataset using the below SQL query.
  
  - Selects cast (zip as int) as zip, count(*) as count from fire_temp_table group by zip.
  
- **Uses the AllJoin Node:** Joins the two filtered datasets using the below query.
  
  - Selects  a.zipcode , a.single_returns, a.joint_returns, a.numdep, a.total_income_amount, a.taxable_interest_amount, b.count, b.zip from  fire_temp_table1 a LEFT OUTER JOIN fire_temp_table2 b ON(a.zipcode=b.zip)
  
- **Uses the CastColumnType Node:** Changes the column type of the count column from Long to Double.

- Uses the ImputingWithConstant Node: Fills the blanks across all the columns with constants.

- **Uses the VectorAssembler Node:** Concatenate columns single_returns, joint_returns, numdep, total_income_amount, taxable_interest_amount into a feature vector feature_vector.

- **Uses Split Node:** Splits the dataset into (.7, .3).

  - 70% rows are used for training and 30% are used for prediction.
  
  - The model is evaluated based on how it predicts on the remaining 30%.

- **Uses the LinearRegression Node:** Performs the LinearRegression.

  - This is a Spark MLLib provided algorithm that Sparkflows exposes to you as a plug-and-play “node”. LinearRegression from SparkML.
  
- **Uses Predict Node:** Performs prediction using the model generated on the remaining 30% dataset.

- **Uses PrintNRows Node:** Evaluates the result using the PrintNRows Node.

First Dataset
--------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/first-dataset.png
   :alt: Fire Market Prediction
   :width: 65%

ColumnFilter
-------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/column-filter-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
SQL
---

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/sql1-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
Second Dataset
--------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/second-dataset.png
   :alt: Fire Market Prediction
   :width: 65%
   
SQL
---

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/sql2-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
AllJoin - Join the Two Datasets
-------------------------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/join-using-sql-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
CastColumnType
--------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/castcolumntype-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
ImputingWithConstant
--------------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/impute-with-constant-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
VectorAssembler
---------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/vector-assembler-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
Split
-----

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/split-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
LinearRegression
----------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/linear-regression-config.png
   :alt: Fire Market Prediction
   :width: 65%
   
Predict
--------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/predict-config.png
   :alt: Fire Market Prediction
   :width: 65%

Print N Rows
-------------

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/print-config.png
   :alt: Fire Market Prediction
   :width: 65%

Now, you can execute the workflow and it will come up with predictions for the number of farmer's markets in a zip code.

.. figure:: ../../../_assets/tutorials/machine-learning/farmer-market-prediction/execute-result.png
   :alt: Fire Market Prediction
   :width: 65%
   
   
