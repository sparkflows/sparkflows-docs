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

from fire_notebook.output.output_text import OutputText
from fire_notebook.output.workflowcontext import RestWorkflowContext
from fire.output.output_text import OutputText

restworkflowcontext = RestWorkflowContext(webserverURL, jobId)
curNodeId = 1
nm = "Testing"
val = "Starting Program"
outputText = OutputText(curNodeId, nm, "title", val, resultType=3, visibility="EXPANDED")
restworkflowcontext.outText(outputText)

Outputing Pyspark Dataframe as Table
---------------

input_df = spark.read.format("csv").option("header", "true").option("sep", ",").load("s3://fire-sample-data/data/cars.csv")

output_df = input_df.select("c1", "c2")

output_df.show()

from fire.output_notebook.output_table import OutputTable

restworkflowcontext.outDataFrame(9, "Names", output_df)


Outputing Pandas Dataframe as Table
-------------------

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst, columns=['name'])

print(df)


