Generative AI Processors
=======

The following table enlists the Huggging Face Library-powered processors available in Fire Insights :

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Create Faiss Embeddings
     - It creates embeddings (Vector DB) from the content of a file. GAI (Generative AI) Platform can use these embeddings to implement chatbots.

   * - Hugging Face Custom Category Sentiment Analysis
     - It performs Sentiment Analysis with Custom Category using models hosted in Hugging Face repository.

   * - Hugging Face Grammatical Correctness
     - This node checks the Grammatical Correctness of the selected column using models hosted in Hugging Face repository.

   * - Hugging Face Natural Language Inference
     - This node evaluates hypothesis based on a given pair of sentences - a premise and a hypothesis, the aim is to determine whether the hypothesis is true (entailment), false (contradiction), or undetermined (neutral) based on the premise.

   * - Hugging Face Question Natural Language Inference
     - QNLI node performs the task of determining if the answer to a certain question can be found in a given document. If the answer can be found the label is “entailment”. If the answer cannot be found the label is “not entailment”.

   * - Hugging Face Sentiment Analysis
     - This node performs Sentiment Analysis using the Hugging Face models. This node classifies the classes in this task as either “acceptable” or “unacceptable”.

   * - Hugging Face Summarization
     - This node summarizes input data create from a file or a text.
   
   * - Hugging Face Tone Analysis
     - This node performs Tone Analysis using the Hugging Face models. It outputs tone of a sentence in the input file.
     
   * - Natural Language Query
     - This node processes a query submitted in natural language against a database using a LLM model.


Hugging Face Sentiment Analysis
-------------

Below is a sample workflow which contains Hugging Face Sentiment Analysis processor in Fire Insights. It demonstrates the usage of Hugging Face Sentiment Analysis node to classify text data into two classes: "acceptable" and "unacceptable." 

It does the following processing of data :

* Reads the incoming dataset.
* Performs the task of sentiment analysis and computes the accuracy score.
* Saves and Prints the result.

Hugging Face Sentiment Analysis Sample Workflow
--------------------


  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/workflow.png
     :alt: data-quality-userguide
     :width: 65%

Incoming Dataset
--------

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/input-data.png
     :alt: data-quality-userguide
     :width: 65%

Hugging Face Sentiment Analysis Node Configuration
--------------

Hugging Face Sentiment Analysis is configured as below :

* Input of this node is the incoming dataset.
* Column on which the sentiment anlysis is to be performed needs to be selected in the **COLUMN TO ANALYSE SENTIMENT** box.
* Pre-loaded LLM Model to be used for computing sentiment is to be selected in the **MODEL TO BE USED FOR SENTIMENT ANALYSIS** box.
* Alternatively, any other Hugging Face model can be used to perform the analysis by entering the model name in the **CUSTOM MODEL NAME** box.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/hf-config.png
     :alt: data-quality-userguide
     :width: 65%


Hugging Face Sentiment Analysis Node Output
--------

The output of the Hugging Face Sentiment Analysis node includes a score column, indicating the confidence level with which the text is classified as positive, negative, or neutral.

  .. figure:: ../../_assets/user-guide/machine-learning/generative-ai/output.png
     :alt: data-quality-userguide
     :width: 65%


















