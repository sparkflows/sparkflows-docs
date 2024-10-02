Chatbot
=======

**A Retrieval-Augmented Generation (RAG) based chatbot** 
It combines retrieval-based and generative models to provide more informative, contextually accurate, and fluent responses. Here’s how it works in detail:

1. Retrieval Component:
Search and Retrieval: The first step involves searching a database or external sources (like documents, FAQs, or web pages) for relevant information based on the input query.
Rank Results: Once relevant information is retrieved, it ranks the results based on relevance to the query.
Passage Selection: The most relevant passages are selected to be passed on to the generative model.

2. Generative Component (Language Model):
Contextual Generation: The selected passages are used as input to a generative model (such as GPT or similar models) along with the user's query.
Response Generation: The generative model uses the retrieved content to generate a coherent and contextually relevant response. This process enables the chatbot to provide more informed answers than a purely generative model, which relies only on pre-trained knowledge.

3. Augmentation and Integration:
Combining Retrieval and Generation: The retrieval results augment the generative model’s response, allowing it to generate answers grounded in the most relevant and up-to-date information.
Improved Accuracy: Since the generative model works with retrieved data, it is more likely to generate accurate and reliable responses, especially for factual or specific domain queries.

**Key Benefits of RAG-Based Chatbots:**
Dynamic Knowledge Base: Unlike static generative models, RAG-based chatbots can dynamically pull information from a large, evolving knowledge base.
Up-to-Date Information: By leveraging real-time or frequently updated data sources, the chatbot can respond to queries with the most current information.
Reduced Hallucination: The retrieval component helps ground the chatbot’s responses, reducing the chance of the model hallucinating or making up inaccurate information.

**Key Chatbot features:**
- Ability to create, save, edit, search and manage various Chat Sessions
- Ability to upload files and save them into RAG Database
- Ability to apply search filters on RAG Database
- Ability to do Ask questions and see the References

**Chat Dashboard**

*Create New Chat Sessions.
Start a Chat Session for driving a conversation.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Create_New.png
     :alt: create-new-chat-session
     :width: 65%

*View and Manage Chat Sessions.
Edit, Delete and Search conversations.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Dashboard.png
     :alt: view-manage-chat-sessions
     :width: 65%

**Conversation UI**
This is the main UI for Q&A against selected resources

*Upload files needed for Conversastion. The files are indexed into the Vector Database. 

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Select_Files.png
     :alt: select-files
     :width: 65%

*Use filters Chat Sessions.
User can configure the filter condition and select required files. User can also search files.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Use_Filters.png
     :alt: search-filters-chat-sessions
     :width: 35%

*Ask Questions in a new / existing Chat Sessions

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Edit_Save.png
     :alt: ask-questions-chat-sessions
     :width: 65%
