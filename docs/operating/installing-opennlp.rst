Running OpenNLP Model Jars in Sparkflows
=====================

When running locally
-------------------

* Create a directory called opennlp-models-1.5 on the local file system
* Download the OpenNLP model jar from : http://opennlp.sourceforge.net/models-1.5/

  * eg: wget http://opennlp.sourceforge.net/models-1.5/en-ner-person.bin
* Copy the OpenNLP model jar into the opennlp-models-1.5 directory created

 

When running on a Spark cluster
--------------------------------

* Copy the model file onto HDFS into a directory called opennlp-models-1.5
* For example /user/centos/opennlp-models-1.5/en-ner-person.bin
* The model file should be accessible by all the users who would use it


.. figure:: ../../_assets/operating/opennlp.png
   :alt: OpenNLP
   :align: center
   
   
