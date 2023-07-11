Generative AI
=======

Sparkflows empowers users to leverage the remarkable Generative AI capabilities by offering numerous processors based on Hugging Face Library. It allows users to host their models and infrastructure either in-house (on-premises or on the cloud within a Virtual Private Cloud) or access licensed models such as GPT-4 through APIs. This versatility ensures that customers can seamlessly harness the power of Generative-AI in a manner that best suits their specific needs and preferences.

Generative AI Processors
---------

The following table enlists the Huggging Face Library-powered processors available in Fire Insights :

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Hugging Face Sentiment Analysis
     - This node classifies the classes in this task as either “acceptable” or “unacceptable”.

   * - Hugging Face Natural Language Inference
     - This node performs the following. Given a pair of sentences - a premise and a hypothesis, the aim is to determine whether the hypothesis is true (entailment), false (contradiction), or undetermined (neutral) based on the premise.
   
   * - Hugging Face Question Natural Language Inference
     - QNLI node performs the task of determining if the answer to a certain question can be found in a given document. If the answer can be found the label is “entailment”. If the answer cannot be found the label is “not entailment".
     
   * - Hugging Face Grammatical Correctness
     - This node infers the Sentiment of the text using the model chosen. The model returns the label with the score.


Hugging Face Sentiment Analysis
-------------

Below is a sample workflow which contains Hugging Face Sentiment Analysis processor in Fire Insights. It demonstrates the usage of Hugging Face Sentiment Analysis node to classify text data into two classes: "acceptable" and "unacceptable." 

It does the following processing of data :

* Reads the incoming dataset.
* Performs the task of sentiment analysis and computes the accuracy score.
* Saves and Prints the result.

Hugging Face Sentiment Analysis Sample Workflow
--------------------


  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/workflow.png
     :alt: data-quality-userguide
     :width: 65%

Incoming Dataset
--------

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/input-data.png
     :alt: data-quality-userguide
     :width: 65%

Hugging Face Sentiment Analysis Node Configuration
--------------

Hugging Face Sentiment Analysis is configured as below :

* Input of this node is the incoming dataset.
* Column on which the sentiment anlysis is to be performed needs to be selected in the **COLUMN TO ANALYSE SENTIMENT** box.
* Pre-loaded LLM Model to be used for computing sentiment is to be selected in the **MODEL TO BE USED FOR SENTIMENT ANALYSIS** box.
* Alternatively, any other Hugging Face model can be used to perform the analysis by entering the model name in the **CUSTOM MODEL NAME** box.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/hf-config.png
     :alt: data-quality-userguide
     :width: 65%


Hugging Face Sentiment Analysis Node Output
--------

The output of the Hugging Face Sentiment Analysis node includes a score column, indicating the confidence level with which the text is classified as positive, negative, or neutral.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/output.png
     :alt: data-quality-userguide
     :width: 65%


















