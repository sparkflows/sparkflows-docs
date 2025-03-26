Chat Assistant
======
This guide outlines the features and steps for effectively using the AI-powered Chat Assistant to enhance customer interactions and improve support efficiency.

**Sparkflows AI-Powered Chat Assistant - Enhancing Interactions**

Our AI-powered Chat Assistant is designed to revolutionize customer interactions by delivering seamless, efficient, and accurate responses. This intelligent assistant enhances user engagement through the following capabilities:

* **Instant Query Resolution :** The chatbot effectively handles frequently asked questions, providing prompt and relevant answers.

* **Document-Based Assistance :** It efficiently processes document-related inquiries, ensuring users receive accurate information quickly.

* **Streamlined Customer Support :** The assistant enhances support operations by automating repetitive tasks and guiding users through solutions, reducing response time and improving satisfaction.

**Highlighted Features**
 
1. Easy Chat Assistant Creation
2. Topic-Based Query Handling
3. Smart File Indexing for Enhanced Responses
4. Seamless Query Resolution

Steps for Using Our Chat Assistant Feature 
-------------
**Step 1 : Configuring Chatbot in Fire Insights**
+++++++++++++++++++++++++++++++++++++++++++++++++++++
* Login to **Fire Insights**.
* Navigate to **Administration -> Configurations -> Module**.
* To view the **chat tab** inside the project, the following configuration need to be enabled by setting its value to **true**, as shown below.

  ::
     
     module.enableChatbot = true


  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/chat-tab-configuration.png
     :alt: create-new-chat-session
     :width: 65%

* Now, navigate to **Administration -> User Management -> Role Tab** and click on **ADMIN** from the roles list, as shown below:

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/role-list.png
     :alt: create-new-chat-session
     :width: 65%



* In Admin roles, you need to **enable** these two permissions: **chatbot.view** and **chatbot.modify**, as shown below.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/config2.png
     :alt: create-new-chat-session
     :width: 65%



**Step 2 :  Creating Chat Assistant** 
++++++++++++++++++++++++++++++++++++++++++
* Go to **Projects -> ITSM-Chatbot -> Chat Tab**.
* Click on **Create Chat Assistant** button located in the right corner, as shown below.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/create-chat-assistant1.png
     :alt: create-new-chat-session
     :width: 65%

* Now, you can quickly create a chatbot assistant depending on your data type (unstructured or structured). Select the appropriate configuration details in the required fields as follows and click on **Create** button.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/create-chat-assistant.png
     :alt: create-new-chat-session
     :width: 65%

  

For Unstructured Data
***************************
Unstructured data includes content that lacks a predefined format, such as text files, PDFs, or images. If you want the chatbot to process documents, analyze text-based data, or provide insights from unorganized content, this is the ideal configuration.

 **Chatbot Basic**

 * **NAME:** Enter the name of the chatbot.
 * **DESCRIPTION:** Provide a description of the chatbot.
 * **GEN AI CONNECTION:** Select the required connection from the list, which includes Open AI, Gemini, Bedrock, etc.

 **Data Source Configuration**

 * **VECTOR DB:** Select the VectorDB connection from the list like pinecone, milvus etc.
 * **VECTOR DB INDEX:** Enter the VectorDB index name where the embedding should be done.
 * **VECTOR DB INDEX NAMESPACE:** Enter the VectorDB index namespace where the embedding should be done.

 
 **Privileges**

 * **SAVE TO DATABASE:** Enabling this option will allow the chatbot to upload files to the VectorDB in the selected chatbot topic.
 * **START CHAT WITH FILE:** Enabling this option will allow the chatbot to chat with selected files in the chatbot thread.
 
 .. note:: Here **selected file** refers to a file that you choose to upload or attach in the chat. For example, if you upload a PDF, spreadsheet, or text file, that becomes the "selected file". Enabling the "START CHAT WITH FILE" option allows the chatbot to read, analyze, and respond based on the contents of the selected file. A **thread** is a conversation session within the chat. So, if you start a new chat, it creates a new thread and if you continue chatting without starting fresh, you’re staying in the same thread.


  


  
  
 


**For Structured Data**

Structured data is organized and stored in relational databases, making it ideal for querying specific records, performing analytics, or extracting information from well-defined tables. If you want the chatbot to interact with data stored in structured formats like SQL databases, choose this option.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/structured-data-option.png
      :alt: create-new-chat-session
      :width: 65%


 * **NAME:** Enter the name of the chatbot.
 * **DESCRIPTION:** Provide a description of the chatbot.
 * **GEN AI CONNECTION:** Select the required connection from the list, which includes Open AI, Gemini, Bedrock, etc.
 * **DATABASE CONNECTION:** Select the required connection from the dropdown list.




* Once chatbots (chat assistants) are created, they will be **visible inside each project within the chat tab** in the format shown below:
 
  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/lists.png
     :alt: create-new-chat-session
     :width: 65%

* Once the chatbot is created, click on **Edit Chat** icon from the chatbot list page, as shown below. You will get an **option to add files and their embeddings** to the VectorDB. These embeddings will be used to retrieve query responses from the VectorDB.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/editchat-icon.PNG
     :alt: create-new-chat-session
     :width: 65%
 
  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/edit-chat.png
     :alt: create-new-chat-session
     :width: 65%






**Step 3 : Managing Chatbot Assistant Page**
+++++++++++++++++++++++++++++++++++++++++++++

* Click on a **specific chatbot** from the chat list, as shown below:

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/lists.png
     :alt: create-new-chat-session
     :width: 65%



  You will be directed to the **Chat Assistant page** as shown below, where you can submit **queries** and receive **responses**.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/chat-assistant-page.png
     :alt: create-new-chat-session
     :width: 65%

**Step 4 : Creating and Managing Topics**
+++++++++++++++++++++++++++++++++++++++++++

* Enter a **topic name** to create a topic for the selected chatbot, as shown below. This topic will only be visible to logged-in users.
 
  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/create-topic.png
     :alt: create-new-chat-session
     :width: 65%

  
  .. note:: If no topic is selected or created, and the user attempts to submit a query, a **default topic** will automatically be created. All related threads will be visible under this default topic.


* Clicking on a **topic** provides the option to **add files** and their **embeddings** to the selected VectorDB, as shown below.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/add-file-in-chat.png
     :alt: create-new-chat-session
     :width: 65%

  On clicking **Add Files** option, you can easily upload the required files.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/chat-add-files.png
     :alt: create-new-chat-session
     :width: 65%


* All the **threads for a particular topic** will be displayed, as shown below. By clicking on a **thread**, you can view all related queries and their responses. 

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/chatbot-query.png
     :alt: create-new-chat-session
     :width: 65%

* You can **rename** or **delete** a specific topic by clicking on the **horizontal ellipsis (...)** icon, as shown below. 

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/rename-delete.png
     :alt: create-new-chat-session
     :width: 65%

* You can **delete** a specific thread within a selected topic as shown below, which will also remove all its associated threads and thread items.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/chatbot/delete-thread.png
     :alt: create-new-chat-session
     :width: 65%
