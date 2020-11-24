Integrating with Databricks Notebook
=========================

The Web App in Fire Insights can trigger a Notebook in Databricks.

The Databricks Notebook can output text, tables and charts to be dispalyed in Fire Insights.

Below are the example for it.

Outputing Text
--------------

jobId = dbutils.widgets.get("job-id")
webserverURL = dbutils.widgets.get("postback-url")

print(webserverURL)
print(jobId)

from fire_notebook.output.workflowcontext import RestWorkflowContext

restworkflowcontext = RestWorkflowContext(webserverURL, jobId)
restworkflowcontext.outStr(9, "Test String")


Outputing Pyspark Dataframe as Table
---------------

input_df = spark.read.format("csv").option("header", "true").option("sep", ",").load("s3://fire-sample-data/data/cars.csv")
output_df = input_df.select("c1", "c2")
output_df.show()

restworkflowcontext.outDataFrame(9, "Names", output_df)


Outputing Pandas Dataframe as Table
-------------------

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst, columns=['name'])
print(df)

restworkflowcontext.outPandasDataframe(9, "Names", df)

