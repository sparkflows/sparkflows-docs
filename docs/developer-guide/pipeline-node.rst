Pipeline Nodes
====================================

Fire Insights supports Pipelines.

Below is an example Pipeline:


A Pipeline can have the following node types:

* workflow
* spark-submit
* shell
* spark-submit-with-parameters

``workflow`` node in a pipeline enables executing a workflow in the project.

``spark-submit`` node in a pipeline enables executing a spark-submit job.

``shell`` node in a pipeline enables executing a shell command.

``spark-submit-with-parameters`` node in a pipeline enables executing a spark-submit job. However, it also enables specifying the various parameters of the spark-submit job.

spark-submit-with-parameters
------------------------

Multiple spark-submit-with-parameters nodes can be added to Fire Insights by adding multiple JSON files.

Below is an example JSON for a spark-submit-with-parameters node which parses XML files.

```
JSON
```

