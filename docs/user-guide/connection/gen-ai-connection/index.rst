GenerativeAI Connections
===================
Enable GenerativeAI Connections in Sparkflows:

   * Login to Sparkflows application i.e **Sparkflows**.
   * Go to  **Administration -> Configurations -> CONNECTION**.
   * Enable Gen AI connection by setting the below parameter to **true** and save the configuration.

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

