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
* To view the chat tab inside the project, the following configuration need to be enabled by setting its value to **true**, as shown below.

  ::
     
     module.enableChatbot = true


  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/chat-tab-configuration.png
     :alt: create-new-chat-session
     :width: 65%


* In roles, you need to **enable** these two permissions: **chatbot.view** and **chatbot.modify**, as shown below.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/config2.png
     :alt: create-new-chat-session
     :width: 65%



**Step 2 :  Creating Chat Assistant** 
++++++++++++++++++++++++++++++++++++++++++

* You can quickly create a chatbot assistant by providing **essential details** in the required fields as follows:

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/create-chat1.png
     :alt: create-new-chat-session
     :width: 65%

 * **NAME:** Enter the name of the chatbot.
 * **DESCRIPTION:** Provide a description of the chatbot.
 * **GEN AI CONNECTION:** Select the OpenAI connection from the list.
 * **VECTOR DB:** Select the VectorDB connection from the list.
 * **VECTOR DB INDEX:** Enter the VectorDB index name where the embedding should be done.
 * **VECTOR DB INDEX NAMESPACE:** Enter the VectorDB index namespace where the embedding should be done.
 * **SAVE TO DATABASE:** Enabling this option should allow the chatbot to upload files to the VectorDB in the selected chatbot topic.
 * **START CHAT WITH FILE:** Enabling this option should allow the chatbot to chat with selected files in the chatbot thread.

* Once the chatbot is created, you will get an **option to add files and their embeddings** to the VectorDB. These embeddings will be used to retrieve query responses from the VectorDB.


  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/editchat.png
     :alt: create-new-chat-session
     :width: 65%


* Once chatbots(chat assistants) are created, they will be **visible inside each project within the chat tab** in the format shown below:
 
  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/list.png
     :alt: create-new-chat-session
     :width: 65%

**Step 3 : Managing Chatbot Assistant Page**
+++++++++++++++++++++++++++++++++++++++++++++

* Click on the name of a particular chatbot from the list to be redirected to the **chat assistant page** as shown below, where you can submit **queries** and receive **responses**.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/chat-assistant1.png
     :alt: create-new-chat-session
     :width: 65%

**Step 4 : Creating and Managing Topics**
+++++++++++++++++++++++++++++++++++++++++++

* Enter a **topic name** to create a topic for the selected chatbot, as shown below. This topic will only be visible to logged-in users.
 
  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/create-topic.png
     :alt: create-new-chat-session
     :width: 65%

  
  .. note:: If no topic is selected or created, and the user attempts to submit a query, a **default topic** will automatically be created. All related threads will be visible under this default topic.


* Clicking on a **topic** provides the option to **add files** and their **embeddings** to the selected VectorDB, as shown below.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/topic1.png
     :alt: create-new-chat-session
     :width: 65%

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/add-file.png
     :alt: create-new-chat-session
     :width: 65%


* All the **threads for a particular topic** will be displayed, as shown below. By clicking on a **thread**, users can view all related queries and their responses. 

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/thread1.png
     :alt: create-new-chat-session
     :width: 65%

* You can **rename** or **delete** a specific topic, as shown below. Deleting a topic will also remove all its associated threads and thread items.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/rename-delete.png
     :alt: create-new-chat-session
     :width: 65%

* You can **delete** a specific thread within a selected topic as shown below, which will also remove all associated thread items.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/chatbot/delete-thread.png
     :alt: create-new-chat-session
     :width: 65%













  
