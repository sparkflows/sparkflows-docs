Integrating with Databricks Notebook
=========================

The Analytics App in Fire Insights can trigger a Notebook in Databricks whose output will be displayed in the Analytical Apps.

Fire Insights passes 2 parameters to the Notebook:

* postback-url
* job-id

Add wheel file to your Databricks Notebook
------------------

Add the wheel file to your Databricks Notebook. This is to enable using the Fire Insights API for sending data to it. 

Download Wheel File at:  https://sparkflows-release.s3.amazonaws.com/fire/common/spark_3.2.1/fire_notebook-3.1.0-py3-none-any.whl


Output details to Analytical Apps
---------------------

The Databricks Notebook can output texts, tables, charts, HTML code and progress bar to be displayed in the analytical app.


Step One: Create a RestWorkflowContext Object
+++++++++++++++++++++++

First create a ``RestWorkflowContext`` for communicating with Fire Insights server. ::

    jobId = dbutils.widgets.get("job-id")
    webserverURL = dbutils.widgets.get("postback-url")

    print(webserverURL)
    print(jobId)

    from fire_notebook.output.workflowcontext import RestWorkflowContext

    restworkflowcontext = RestWorkflowContext(webserverURL, jobId)

Step Two: Understand the Output Functions
+++++++++

Output as Text
+++++++++


Below is how to output text to Fire Insights. ::

    restworkflowcontext.outStr(9, "Test String", text="text")


Output PySpark Dataframe as Table
+++++++++


The below code outputs the contents of PySpark DataFrame to Fire Insights as a table. By deafult 10 rows will be displayed. ::
    
    from pyspark.sql.types import *

    schema = StructType([StructField("c1", DoubleType())\
                      ,StructField("c2", IntegerType())])
    test_list = [[0.0, 2], [1.0, 4], [2.0, 8], [3.0, 16], [4.0, 32], [5.0, 64], [6.0, 128]]
    df = spark.createDataFrame(test_list,schema=schema)
    restworkflowcontext.outDataFrame(9, "PySpark Dataframe", df)

    #To display 3 rows
    restworkflowcontext.outDataFrame(9, "PySpark Dataframe", df, 3)

Output Pandas DataFrame as Table
+++++++++


The below code outputs the contents of Pandas DataFrame to Fire Insights as a table.  By deafult 10 rows will be displayed. ::

    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']

    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst, columns=['name'])
    print(df)

    restworkflowcontext.outPandasDataframe(9, "Names", df)
    
    #To display 3 rows
    restworkflowcontext.outDataFrame(9, "Names", df, 3)
    
Output as Charts
+++++++++


Output the chart in fire by selecting x & y column. We can display Column , Bar & Line chart types as outputs. ::
    
    from pyspark.sql.types import *

    schema = StructType([StructField("c1", DoubleType())\
                      ,StructField("c2", IntegerType())])
    
    test_list = [[0.0, 2], [1.0, 4], [2.0, 8], [3.0, 16], [4.0, 32], [5.0, 64], [6.0, 128]]
    
    df = spark.createDataFrame(test_list,schema=schema)
    
    restworkflowcontext.outDataframeChart(title= "Example Chart", x_column = "c1", y_columns = ["c2"],
                                      chart_type ="LINECHART", df = df, numRowsToDisplay = 10)
 
 
Output as HTML
+++++++++


Below is how to output HTML to Fire Insights. ::
    
    htmlstr1 = "<h3>You can view HTML code in notebooks.</h3>"
 
    restworkflowcontext.outHTML(9, title="Example HTML", text = htmlstr1)
       
Plotly with Fire Insights
+++++++++++++


Below is how to output plotly to Fire Insights. ::
    
    import plotly.graph_objs as go
    import plotly
    
    test = plotly.offline.plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], 
                     output_type='div', 
                    include_plotlyjs=False)
    example_plotly = f'{test}'
    
    restworkflowcontext.outPlotly(9, title="Example Plotly", text = example_plotly)
    
Output Parameters
+++++++++++++++++++++


When we want to display a list of values we use the below code to generate the output: ::
    
    parameters = [("radio", "Industries", "Natural Resources, Construction, IT, Services, Finance, Real Estate, Others"), 
              ("checkbox", "Education, Position", "Graduate, Manager"),
              ("select", "Select country", "INDIA, USA, UK, Germany"),
              ("textarea", "Province", ""),
              ("text", "Region Code", ""),
             ]

    restworkflowcontext.outParameters(9, "Display Parameters In Dictionary To Table", parameters)

Output Messages
++++++++++++++


This output is used by the analytical app to show the Execution Status of the job. 


::

    message = "Sending the success message."
    
    restworkflowcontext.outSuccess(9, title="Success", text=message)
    
::

    message = "Sending the failure message."
    
    restworkflowcontext.outFailure(9, title="Failure", text=message)
    
::

    message = "Sending the running message."
    
    restworkflowcontext.outRunning(9, title="Running", text=message)
    
Output Progress Message
++++++++++++++


You can share the current progress of the Notebook run in percentage terms to the analytical app. This is useful to keep the user updated with the progress of the job execution.

::

    message = "50"
    restworkflowcontext.outputProgress(9, title="Progress", progress=message)


Get Input Value
++++++++++++++

Analytical apps also allow us to pass a variable value as an input parameter to the notebook execution.

If a user doesn’t enter a value within 120 seconds, it will return a default response.

::

    title = "Name of the Country:"
   
    country_name = restworkflowcontext.getTextInput(9, title=title, url=webserverURL)
    

Conclusion
---------------------

This way we can use analytical apps to interface our Databricks Notebook with a user-friendly interface to business and other project stakeholders.

DataBricks NoteBook Code Example
+++++++++++

::

    import sklearn
    import pandas as pd
    from sklearn.datasets import load_boston 
    from fire_notebook.output.workflowcontext import RestWorkflowContext

    boston = load_boston() # load the database

    # Create Widgets
    dbutils.widgets.text("job-id", "100")
    dbutils.widgets.text("postback-url", "")

    jobId = dbutils.widgets.get("job-id")
    webserverURL = dbutils.widgets.get("postback-url")

    restworkflowcontext = RestWorkflowContext(webserverURL, jobId)

    message="30" # Implies that 30% job execution has been completed
    restworkflowcontext.outputProgress(9, title="Progress", progress=message)

    boston_df = pd.DataFrame(boston.data)  #load data into pandas. 
    boston_df.columns = boston.feature_names
    boston_df = boston_df.describe()
    boston_df

    message="60"
    restworkflowcontext.outputProgress(9, title="Progress", progress=message)
    restworkflowcontext.outPandasDataframe(9, "DataFrame Describe Values ", boston_df)
    restworkflowcontext.outputProgress(9, title="Progress", progress=message)
    message="100"
    restworkflowcontext.outputProgress(9, title="Progress", progress=message)
    message = "Job Execution Done."
    restworkflowcontext.outSuccess(9, title="Success", text=message)
