NameFinder
===========

Fire provides NameFinder Processor to easily detect named entities and numbers in text. It takes in a column name in the input DataFrame containing text. It then detects the entities and stores them into a new column.

To be able to detect entities, the NameFinder needs a model. The model is dependent on the language and entity type it was trained for.

https://opennlp.apache.org/documentation/1.6.0/manual/opennlp.html#tools.namefind.recognition.cmdline

 
The OpenNLP project offers a number of pre-trained NameFinder models which are trained on various freely available corpora. Those can be downloaded here: http://opennlp.sourceforge.net/models-1.5/

 
Steps for installing the OpenNLP models in Fire can be found here: http://docs.sparkflows.io/en/latest/operating/installing-opennlp.html

Workflow
--------

Below is a workflow which uses the NameFinder Processor.

.. figure:: ../../_assets/tutorials/nlp/namefinder/nlp-wf.png
   :alt: Workflow
   :width: 65%
   
It consists of 3 Processors:

* TextFiles- It reads in the input text file and creates a row from each line of the text.
* OpenNLPNameFinder- It extracts the entities from each line of the text.
* PrintNRows- It prints the first 10 rows of the result.

Textfiles
---------

It reads in the input files from the directory data/ner-person. It places each line in the column 'line'.

Processor Configuration
++++++++++++++++++

.. figure:: ../../_assets/tutorials/nlp/namefinder/read-config.png
   :alt: Workflow
   :width: 75%
   
Processor Output
++++++++++++++++

.. figure:: ../../_assets/tutorials/nlp/namefinder/read-output.png
   :alt: Workflow
   :width: 75%   
   
OpenNLPNameFinder
-----------------

It extracts entities from the text in the input column 'line' and stores them in the output column 'ner'. When running on the Hadoop Cluster, the model file has to be on HDFS and users have to have access to it.

.. figure:: ../../_assets/tutorials/nlp/namefinder/nlp-config.png
   :alt: Workflow
   :width: 75%
   
PrintNRows
----------

It prints the first 10 rows from the result.

.. figure:: ../../_assets/tutorials/nlp/namefinder/print-config.png
   :alt: Workflow
   :width: 75%
   

