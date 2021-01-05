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

    input_df = spark.read.format("csv").option("header", "true").option("sep", ",").load("s3://fire-sample-data/data/cars.csv")
    output_df = input_df.select("c1", "c2")
    output_df.show()

    restworkflowcontext.outDataFrame(9, "Names", output_df)


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

