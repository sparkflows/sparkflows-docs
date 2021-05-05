Debug Mode
----------

Fire Insights allows you to run the workflow in Debug mode.

In the debug mode a count is performed on the output from each Processor. This helps to know which Processor is exactly taking more time.

Apache Spark in general executes the DAG lazily. It starts the execution of the DAG only when it hits an Action. Hence, many times we do not know which Processor is actually taking more time.

Forcing Action with count in Debug mode forces execution of that step and insights into the time taken by the Processor.
