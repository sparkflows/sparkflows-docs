Python Examples
----------------------

Fire provides a Pyspark processer in which Python code can be written. The Pyspark processor can only be written in a Pyspark workflow.

Below are a few code examples in Python.

Adding House Type Field
======================================

::

    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *
    from fire.workflowcontext import *

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
      house_type_udf = udf(lambda bedrooms: "big house" if int(bedrooms) >2 else "small house", StringType())
      filetr_df = inDF.select("id", "price", "lotsize", "bedrooms")
      outDF = filetr_df.withColumn("house_type", house_type_udf(filetr_df.bedrooms))
      return outDF


Linear Regression 
===========================================================

::

    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *

    import numpy as np
    import pandas as pd

    from sklearn.linear_model import LinearRegression
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    from sklearn import metrics

    from joblib import dump, load

    from fire.workflowcontext import *

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
      # Convert the Spark DataFrame to a Pandas DataFrame using Arrow
      dataset = inDF.select("*").toPandas()
  
      print(dataset.head)
      print(dataset.shape)
      print(dataset.describe())
      dataset = dataset.fillna(method='ffill')
    
      X = dataset[
          ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
         '  total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']].values
      print(X)

      y = dataset['quality'].values
      print(y)

      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

      # There are three steps to model something with sklearn
      # 1. Set up the model
      model = LinearRegression()
      # 2. Use fit
      ft = model.fit(X_train, y_train)
      print(ft)
      # 3. Check the score
      scr = model.score(X_test, y_test)
      workflowContext.outStr(id, "Model Score : " + str(scr))

      # 4. Print model
      workflowContext.outStr(id, "Model Coeffient : " + str(model.coef_))
      workflowContext.outStr(id, "Model Intercept : " + str(model.intercept_))

      # 5. Predict test data
      y_pred = model.predict(X_test)

      # 6. See difference between actual and predicted value
      df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
      df1 = df.head(25)
      workflowContext.outPandasDataframe(id, "Actual - Predicted : ", df1)

      # 7. Evaluate the performance
      workflowContext.outStr(id, "Mean Absolute Error:" + str(metrics.mean_absolute_error(y_test, y_pred)))
      workflowContext.outStr(id, "Mean Squared Error:" + str(metrics.mean_squared_error(y_test, y_pred)))
      workflowContext.outStr(id, "Root Mean Squared Error:" + str(np.sqrt(metrics.mean_squared_error(y_test, y_pred))))
    
      return inDF
  
PandasDataFrame to SparkDataFrame
=================================
::

    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *

    import numpy as np
    import pandas as pd
    
    from fire.workflowcontext import *

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
      # Convert the Spark DataFrame to Pandas DataFrame
      dataset = inDF.select("*").toPandas()
      # Select fixed acidity & volatile acidity columns
      X = dataset[['fixed acidity', 'volatile acidity']]
      #Convert Pandas Dataframe to Spark Dataframe
      outDF = spark.createDataFrame(X)
      return outDF

Numpy 2D Array to PandasDataFrame and PandasDataFrame to SparkDataFrame
===================================================================
::

    from pyspark.sql.types import StringType
    from pyspark.sql.functions import *
    from pyspark.sql import *

    import numpy as np
    import pandas as pd
    
    from fire.workflowcontext import *

    def myfn(spark: SparkSession, workflowContext: WorkflowContext, id: int, inDF: DataFrame, cust_dict):
      # Create the numpy 2d array
      example_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
      # Convert to Pandas Dataframe
      pandas_dataframe = pd.DataFrame(example_array, columns=['a', 'b', 'c', 'd'])
      # Convert Pandas Dataframe to Spark Dataframe
      spark_dataframe = spark.createDataFrame(pandas_dataframe)
      return spark_dataframe
