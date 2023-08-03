PySpark Processor
=======

Fire Insights provides a PySpark processor for writing PySpark or Python code.

Interface
---------

In the PySpark Processor, we have to implement the **myfn** function which gets invoked::

  def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame):

  * spark : SparkSession object
  * workflowContext : Can be used for outputting results to the user
  * id : id of the current processor
  * inDF : Input PySpark dataframe


WorkflowContext
---------------

WorkflowContext offers the user the following methods to output data: ::
 
  * def outStr(self, text: str)
  * def outNameValue(self, nm: str, val: str)
  * def outSchema(self, id: int, title: str, df: DataFrame)
  * def outDataFrame(self, id: int, title: str, df: DataFrame)
  * def outPandasDataframe(self, id: int, title: str, df: pd.DataFrame)
  * def outNumpy1darray(self, id: int, title: str, arr: np.ndarray)
  * def outNumpy2darray(self, id: int, title: str, arr: np.ndarray)

Example 1
-------

Below is an example code for the PySpark Node:

.. code-block:: python
    :linenos:
   
    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *
    from workflowcontext import *

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame):
      house_type_udf = udf(lambda bedrooms: "big house" if int(bedrooms) >2 else "small house", StringType())
      filetr_df = inDF.select("id", "price", "lotsize", "bedrooms")
      outDF = filetr_df.withColumn("house_type", house_type_udf(filetr_df.bedrooms))
      return outDF
      
Example 2
---------

Below is another example which uses sklearn:

.. code-block:: python
    :linenos:
    
    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *
    from workflowcontext import *

    import numpy as np
    import pandas as pd

    from sklearn.linear_model import LinearRegression
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    from sklearn import metrics

    from joblib import dump, load

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame):
      # Convert the Spark DataFrame to a Pandas DataFrame using Arrow
      dataset = inDF.select("*").toPandas()

      dataset = dataset.fillna(method='ffill')

      X = dataset[
            ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
             'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].values

      y = dataset['quality'].values

      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

      # There are three steps to model something with sklearn
      # 1. Set up the model
      model = LinearRegression()
      # 2. Use fit
      ft = model.fit(X_train, y_train)
      print(ft)
      # 3. Check the score
      scr = model.score(X_test, y_test)
      workflowContext.outStr("Model Score : " + str(scr))

      # 4. Print model
      workflowContext.outStr("Model Coeffient : " + str(model.coef_))
      workflowContext.outStr("Model Intercept : " + str(model.intercept_))

      # 5. Predict test data
      y_pred = model.predict(X_test)

      # 6. See difference between actual and predicted value
      df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
      df1 = df.head(25)
      workflowContext.outPandasDataframe(id, "Actual - Predicted : ", df1)

      # 7. Evaluate the performance
      workflowContext.outStr("Mean Absolute Error:" + str(metrics.mean_absolute_error(y_test, y_pred)))
      workflowContext.outStr("Mean Squared Error:" + str(metrics.mean_squared_error(y_test, y_pred)))
      workflowContext.outStr("Root Mean Squared Error:" + str(np.sqrt(metrics.mean_squared_error(y_test, y_pred))))

      return inDF




