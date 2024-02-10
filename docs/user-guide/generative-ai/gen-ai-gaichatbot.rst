GAI Chatbot Implementation
=======

**GAI Chatbot Implementation Steps**

* Embedding needs to be created using a document.
* Creation of embedding is performed by ‘Create Faiss Embeddings’ node in sparkflows. Langchain library is used to create embeddings.
* These embeddings would be used in the GenAI chatbot feature in sparkflows to respond to queries.

Embeddings Creation
-------------

**Workflow**

* ‘Create Faiss Embeddings’ node needs to be added to a pyspark workflow.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/sample-implementations/GAI-Workflow.png
     :alt: genai-implementations-userguide
     :width: 65%

**Configure “Faiss Embeddings node”**

* Path of pdf file needs to be selected using the browse button.
* Path to store vector db comprising of embeddings needs to be selected.
* Embeddings are created once workflow is executed.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/sample-implementations/GAI-Node-Config.png
     :alt: genai-implementations-userguide
     :width: 65%

GAI Chatbot Platform
-------------

**GAI Chatbot**

* GAI Chatbot can be accessed using the app option in the toolbar.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/sample-implementations/GAI-Chatbot-Access.png
     :alt: genai-implementations-userguide
     :width: 65%

**GAI Chatbot Embedding List**

* All created embeddings would be listed in the drop down.
* Select the embedding against which query needs to be submitted.
* Enter query/message in the ‘Send a message’ box and click send icon.
* Response to the query would be displayed in the chat.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/sample-implementations/GAI-Chatbot.png
     :alt: genai-implementations-userguide
     :width: 65%

**GAI Chatbot Historical Chats**

* All past chats would be list on the left. They can be selected and further queries can be added to them.
* To start a new chat select ‘New Chat’ option from left.
* To delete a chat select delete option against it.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/sample-implementations/GAI-Chatbot-Response.png
     :alt: genai-implementations-userguide
     :width: 65%
