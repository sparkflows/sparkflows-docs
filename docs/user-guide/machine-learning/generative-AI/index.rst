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
