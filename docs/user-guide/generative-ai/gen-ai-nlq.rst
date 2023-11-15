Generative AI NLQ Processor And Apps
=======

The following table enlists the OpenAI powered processor and application for NLQ (Natural Language Query) available in Fire Insights :

.. list-table:: 
   :widths: 40 60
   :header-rows: 1

   * - Title
     - Description
   * - Gen AI SQL Query
     - Powered by Generative AI this node can be used to query the connected database using Natural Language Query.

   * - NLQ Application
     - This application provides a User Interface to submit Query against the connected RDBS.
   

Natural Language Query (NLQ)
-------------

Powered by Generative AI NLQ can be used to query a connected RDBS using a query submitted in Natural Language rather than complex SQL statement. Query can be as simple as **Show me the count of employees**. 

Below is a NLQ **Gen AI SQL Query** processor in Fire Insights.

It does the following processing :

* It accepts a query submitted in Natural Language.
* It makes a Generative AI call to the OpenAI API and receives a SQL Statement in response.
* SQL Statement is executed against the connected RDBS to render the output.

Gen AI SQL Query processor configuration
--------------------


  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/nlq/NLQ-Gen-Sql-Query-1.png
     :alt: genai-nlq-userguide
     :width: 65%

* Connection - Select the RDBS connection.
* Query - Enter a query in Natural Language that needs to be executed against the connected database.
* Include Tables - This is an optional field. Enter the database table names.


  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/nlq/NLQ-Gen-Sql-Query-2.png
     :alt: genai-nlq-userguide
     :width: 65%

* Connection - Select the OpenAI connection.

NLQ Application
--------

**NLQ App Introduction**

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/nlq/NLQ-App-Introduction.png
     :alt: genai-nlq-userguide
     :width: 65%

**NLQ App Query Interface**

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/nlq/NLQ-App-Query.png
     :alt: genai-nlq-userguide
     :width: 65%

**NLQ App Query Result**

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/nlq/NLQ-App-Query-Result.png
     :alt: genai-nlq-userguide
     :width: 65%

* User needs to enter a query in the Query Box.
* On clicking **Run** button result would be displayed.
