Hugging Face
============

Hugging Face NLP library provides various resources like datasets, transformers, and tokenizers, etc. 

Hugging Face models provide many different configurations and great support for a variety of use cases, but here are some of the basic tasks that it is widely used for:

1. Sequence classification
Given a number of classes, the task is to predict the category of a sequence of inputs. It is a predictive modeling problem and has a broad range of applications. Some real-world use cases are – Understanding the sentiment behind a review, detecting spam emails, correcting grammatical mistakes, etc.

2. Question & answer
Providing an answer for a given contextual question. The idea is to build a system that can automatically answer questions posed by humans. The questions can be open or close-ended and the system should be designed to be compatible with both. The answers can be constructed either by querying a structured database or searching through an unstructured collection of documents.

3. Named entity recognition
Named entity recognition is the task of identifying a token as a person, place, or organization. It is being used in many fields in NLP and helps solve many real-world problems. In this technique, we can scan articles and extract fundamental entities and categorize them into defined classes.

4. Summarization
Do you remember writing a summary report in school or college? Well, this task is the same, given a document, with the help of NLP, it can be converted into a concise text. It is a process of creating a short, coherent, and fluent version of a longer text. There are two approaches that can be used for text summarization – Extractive and Abstractive. In the extractive approach, we extract the important sentences and phrases whereas, during the abstractive approach, we are required to interpret the context and reproduce the text keeping core information intact. 

5. Translation
It is the task of translating a text from one language to another. Replacing atomic words is not enough as we want to create a system that is able to translate the text like a human translator. We need a corpus that takes into account phonetic typology, translations of idioms, etc. to conduct complicated translations.

6. Language modelling
Language modeling involves generating text to make sense of a sequence of tokens or predicting some phrases that can be used to complete a text. These tasks can be categorized as – Masked Language Modelling and Casual Language modeling. 

There is more to NLP tasks other than just working with written text, it also covers solutions related to Speech Recognition, Computer Vision, Generating Transcripts, etc. NLP tasks are difficult to handle with Machine Learning and a lot of research has been done to improve the accuracy of these models. 

TEXT Models
--------------

Transformers are increasingly the model of choice for NLP problems and this is the reason there have been many developments in this area. Many models that Hugging Face supports are based on the transformer’s architecture. 
The following NLP recipes are available for a text column.

* BERT

* DistilBERT

* XLNet

* RoBERTa

* XLM

* XLM-RoBERTa

* AIBERT

* CamemBERT
