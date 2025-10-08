GenerativeAI Connections
===================
Enable GenerativeAI Connections in Sparkflows

   * Login to Sparkflows application i.e **Fire Insights**.
   * Go to  **Administration -> Configurations -> Connection**
   * Enable Glue connection by setting the below parameter to **true** and save the configuration.

     ::
   
       connection.gen.ai.enabled : true

   * These connections can be created to interact with LLM model exposed via APIs.



.. toctree::
   :maxdepth: 2

   open-ai.rst
   azure.rst
   gemini.rst
   nvidia.rst
   databricks-llm.rst
   palm-api.rst
   bedrock.rst

