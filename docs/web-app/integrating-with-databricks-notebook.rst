Integrating with Databricks Notebook
=========================

The Web App in Fire Insights can trigger a Notebook in Databricks.

Fire Insights passes 2 parameters to the Notebook:

* postback-url
* job-id

Add wheel file to your Databricks Notebook
------------------

Add the wheel file to your Databricks Notebook. This is to enable using the Fire Insights API's for sending data to it.


Outputing details to Fire Insights
---------------------

The Databricks Notebook can output text, tables and charts to be dispalyed in Fire Insights.

Below are the examples for it.

Create a RestWorkflowContext Object
+++++++++++++++++++++++

First create a ``RestWorkflowContext`` for communicating with Fire Insights Server ::

    jobId = dbutils.widgets.get("job-id")
    webserverURL = dbutils.widgets.get("postback-url")

    print(webserverURL)
    print(jobId)

    from fire_notebook.output.workflowcontext import RestWorkflowContext

    restworkflowcontext = RestWorkflowContext(webserverURL, jobId)

Outputing Text
+++++++++

Below is how to output text to Fire Insights ::

    restworkflowcontext.outStr(9, "Test String")


Outputing PySpark Dataframe as Table
+++++++++

The below code outputs the contents of PySpark Dataframe to Fire Insights as a table ::
    
    from pyspark.sql.types import *

    schema = StructType([StructField("c1", DoubleType())\
                      ,StructField("c2", IntegerType())])
    test_list = [[0.0, 2], [1.0, 4], [2.0, 8], [3.0, 16], [4.0, 32], [5.0, 64], [6.0, 128]]
    df = spark.createDataFrame(test_list,schema=schema)
    restworkflowcontext.outDataFrame(9, "PySpark Dataframe", df)


Outputing Pandas Dataframe as Table
+++++++++

The below code outputs the contents of Pandas Dataframe to Fire Insights as a table ::

    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']

    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst, columns=['name'])
    print(df)

    restworkflowcontext.outPandasDataframe(9, "Names", df)


Outputing CHART
+++++++++


Output the chart in fire by selecting x & y column and Different type of chartType: COLUMNCHART, BARCHART & LINECHART

    
    from pyspark.sql.types import *

    schema = StructType([StructField("c1", DoubleType())\
                      ,StructField("c2", IntegerType())])
    
    test_list = [[0.0, 2], [1.0, 4], [2.0, 8], [3.0, 16], [4.0, 32], [5.0, 64], [6.0, 128]]
    
    df = spark.createDataFrame(test_list,schema=schema)
    
    restworkflowcontext.outDataframeChart(title= "Example Chart", x_column = "c1", y_columns = ["c2"],
                                      chart_type ="LINECHART", df = df, numRowsToDisplay = 10)
 
 
Outputing HTML
+++++++++

Below is how to output html to Fire Insights ::
    
    htmlstr1 = "<h3>You can view HTML code in notebooks.</h3>"
 
    restworkflowcontext.outHTML(9, title="Example HTML", text = htmlstr1)
    
    
    
Outputing Plotly
+++++++++++++

Below is how to output plotly to Fire Insights ::
    
    import plotly.graph_objs as go
    import plotly
    
    test = plotly.offline.plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], 
                     output_type='div', 
                    include_plotlyjs=False)
    example_plotly = f'{test}'
    
    restworkflowcontext.outPlotly(9, title="Example Plotly", text = example_plotly)

