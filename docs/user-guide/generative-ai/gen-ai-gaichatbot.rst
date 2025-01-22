Chatbot
=======

This document explains how to use the **RAG-based chatbot**, including managing chat sessions, uploading files, and asking questions. It covers key features and workflows for effective, accurate interactions.

Overview of RAG-Based Chatbot
++++++++++++++++++

**Introduction and Operational Framework**

A Retrieval-Augmented Generation (RAG) based chatbot seamlessly integrates retrieval-based and generative models to deliver highly accurate, context-aware, and fluent responses. Its functionality can be better understood by examining the roles of its individual components, as follows:


**1. Retrieval Component**

It focuses on finding and ranking the most relevant information from external sources to address the user's query. It involves the following steps:

* Search and Retrieval: This step involves searching a database or external sources (like documents, FAQs, or web pages) for relevant information based on the input query.
* Rank Results: This step involves evaluating and ranking the retrieved information to determine its relevance to the query. 
* Passage Selection: This step involves selecting the most relevant passages to serve as input for the generative model.

**2. Generative Component (Language Model)**

It uses the information retrieved in combination with the user's query to produce a coherent response. It involves the following steps:

* Contextual Generation: This step involves taking the selected passages and the user’s query as input to a generative language model (e.g., GPT or similar models).
* Response Generation: This step involves generating a coherent and contextually relevant response based on the retrieved information. This process enables the chatbot to provide more informed answers compared to a purely generative model, which relies solely on pre-trained knowledge.

**3. Augmentation and Integration**

It brings together the retrieval and generative components to ensure responses are both factually accurate and contextually relevant. It involves the following steps:

* Combining Retrieval and Generation: This step involves augmenting the generative model's response with retrieval results, enabling it to generate answers grounded in the most relevant and up-to-date information.

* Improved Accuracy: This step ensures that, by working with retrieved data, the generative model is more likely to produce accurate and reliable responses, particularly for factual or domain-specific queries.

**Key Benefits**

* Dynamic Knowledge Access: RAG-based chatbots can dynamically retrieve information from a vast and evolving knowledge base, unlike static generative models.
* Real-Time Updates: They leverage real-time or frequently updated data sources to provide responses that reflect the most current information.
* Reduced Hallucinations and Enhanced Accuracy: The retrieval component grounds the chatbot's responses in factual data, significantly reducing the likelihood of the model generating inaccurate or fabricated information.

**Key Features**

* Chat Session Management: Create, save, edit, search, and manage multiple chat sessions effortlessly.
* File Uploads and Database Integration: Upload files and store them directly into the RAG database for future reference.
* Advanced Search Filters: Apply filters on the RAG database to retrieve specific and relevant information efficiently.
* Context-Aware Q&A: Ask questions and receive accurate answers along with referenced sources.

Using Chat Dashboard Features
+++++++++

#. **Create and Start New Chat Session**

   Easily create new chat sessions to begin conversations and start engaging in meaningful interactions, as shown below:

   .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Create_New.png
     :alt: create-new-chat-session
     :width: 65%

#. **View and Manage Chat Sessions**
    
   **Search** the ongoing or previous conversations and **Edit** or **Delete** them via **Actions** menu, as shown below:

   .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Dashboard.png
     :alt: view-manage-chat-sessions
     :width: 65%

#. **Conversation UI**
    
   Engage in Q&A using this main interface for selected resources. Upload necessary files for the conversation as shown below. The files are indexed into the vector database.

   .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Select_Files.png
     :alt: select-files
     :width: 65%

#. **Use Filtered Chat Sessions**

   Configure filter conditions to select required files for use in chat sessions and also, search and retrieve files efficiently, as shown below:

   .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Use_Filters.png
     :alt: search-filters-chat-sessions
     :width: 35%

#. **Ask Questions** 

   Pose questions within new or existing chat sessions for precise and context-aware responses, as shown below:

   .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/ChatSession_Edit_Save.png
     :alt: ask-questions-chat-sessions
     :width: 65%
