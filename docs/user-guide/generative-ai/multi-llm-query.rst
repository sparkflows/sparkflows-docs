Multi LLM Query
===============

The **Multi LLM Query** node is the workhorse of Generative AI in Sparkflows — it sends each row (or a group of rows) of your DataFrame to a Large Language Model and adds the model's response as a new column. A single node covers summarization, question-answering, extraction, classification, translation, and image understanding, driven entirely by how you configure the prompt and the input/aggregation modes.

It is used both on its own (over any text column) and as the **answer-generation step of a RAG pipeline** (after retrieving context from a vector store).

Core configuration
------------------

.. list-table::
   :widths: 26 74
   :header-rows: 1

   * - Setting
     - Meaning
   * - **Connection**
     - The configured LLM connection (AzureOpenAI, OpenAI, Bedrock, Gemini, …). Provider, model, deployment, endpoint and key are taken from it at run time.
   * - **Input mode**
     - ``text`` (read a text column), ``image`` (read an image column), or ``text+image`` (multimodal). Set the **content column** for text and the **image column** for image input.
   * - **Prompt**
     - The system/instruction prompt that tells the model what to do (for example, *"Summarize this document in five bullet points"*).
   * - **User-query column**
     - Optional. A column whose value is appended as the user's question for each row — ideal for Q&A where each row carries its own question, or for RAG where the retrieved context is the content and the question comes from this column.
   * - **Aggregate mode**
     - ``none`` → one response **per row**; ``all`` → a **single** response over all rows combined; ``perfile`` → one response **per file** (requires a file-name column). Choose based on whether you want row-level, document-level, or corpus-level answers.
   * - **Temperature / Max tokens / Timeout**
     - Standard generation controls — lower temperature for factual/extraction tasks, higher for creative text.

Configuration scenarios
-----------------------

The same node behaves very differently depending on how you combine **prompt**, **input mode** and **aggregate mode**:

.. list-table::
   :widths: 34 66
   :header-rows: 1

   * - You want to…
     - Configure it as
   * - Summarize / classify **each row**
     - Input ``text``, aggregate ``none``, prompt describes the per-row task (e.g. *"Classify the sentiment as positive, negative or neutral."*).
   * - Produce **one** summary of a whole document
     - Input ``text``, aggregate ``all``, prompt *"Summarize the following text into a short paragraph."*
   * - Summarize **each file** in a folder
     - Input ``text``, aggregate ``perfile`` (+ file-name column), after **Document To Text** so each file's pages are grouped.
   * - **Question answering** where each row has its own question
     - Input ``text``, aggregate ``none``, set the **user-query column**; the content column supplies the context.
   * - **RAG answer** (grounded on retrieved chunks)
     - Content column = the retrieved chunks, user-query column = the question, prompt *"Answer using only the provided context; say so if it is not present."*
   * - **Extraction** (fields → structured output)
     - Prompt asks for the fields as JSON (e.g. *"Extract invoice_number, date and total as JSON."*); low temperature.
   * - **Translation**
     - Prompt *"Translate the text to French, preserving formatting."*
   * - **Image / multimodal understanding**
     - Input ``image`` or ``text+image``, set the image column; prompt *"Describe the image"* or *"Extract the table from this scanned page."*

Combination patterns
--------------------

Multi LLM Query is rarely used alone — it sits at the end of a short chain:

* **Document processing** — ``Document To Text`` → ``Multi LLM Query`` : read PDFs/DOCX, then summarize, translate, extract fields, or answer questions about them (use aggregate ``perfile`` for one result per document).
* **RAG answer** — ``Read from Pinecone/FAISS`` → ``Multi LLM Query`` : the retrieved chunks become the content, the question comes from the user-query column, and the prompt keeps the answer grounded.
* **Web + LLM** — ``SerperAI Search`` → ``Web Scraper`` → ``Multi LLM Query`` : research a topic on the web, then synthesize an answer.

.. tip::

   Keep the **prompt** specific and put variable data in columns rather than in the prompt. Switch **aggregate mode** — not the prompt — to move between per-row, per-document, and whole-corpus answers.
