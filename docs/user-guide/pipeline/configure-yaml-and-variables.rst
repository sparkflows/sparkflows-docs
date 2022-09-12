Configure Yaml files and Variables
==================================


Sparkflows provides a node using which yaml files and variables can be configured.

Yaml File Configuration
----------------------

1. In ``configFilePath`` field, add the names of the config yaml files.

2. In ``airflowConfigKey`` field, add the variable key name defined in airflow.The variables from airflowConfigKey gets the higher precedence.

3. In ``variablesList`` field, add the variable names and variable values.


**Configuration details in UI can be seen as below:**

.. figure:: ../../_assets/user-guide/pipeline/pipeline_upload_config_files.PNG
   :alt: configuration
   :width: 30%
   
   
**Below is an example of yaml file and variables.**

**Yaml file example :**


.. code-block:: bash

   dev:
      input:
         bucketname: fire-sample-data
         keyname: inputlocation
           
      output:
         bucketname: fire-sample-data
         keyname: outputlocation
   prod:
      input:
         bucketname: fire-sample-data
         keyname: inputlocation
           
      output:
         bucketname: fire-sample-data
         keyname: outputlocation
   customer_id: 62300



In below examples ENV = dev, INPUTPATH = input and OUTPUTPATH = output variables should be defined in airflow.

.. code-block:: bash

 1.input_bucketname {{ENV}}.{{INPUTPATH}}.bucketname 
 2.output_bucketname {{ENV}}.{{OUTPUTPATH}}.bucketname
 3.input_key {{ENV}}.{{INPUTPATH}}.keyname
 4.output_key {{ENV}}.{{OUTPUTPATH}}.keyname
 


Now ``input_bucketname`` and ``output_bucketname`` variables can be used with single curly(i.e {variable_name}) braces to define the complete paths.

.. figure:: ../../_assets/user-guide/pipeline/pipeline_define_variable.PNG
   :alt: variables used
   :width: 30%



**The spark-submit command would look like below**

.. code-block:: bash

   spark-submit --master,yarn,--deploy-mode,client,--class,com.fire.SparkApp,s3://fire-sample-data/jar/fire-xml-parse-1.0-jar-with-dependencies.jar,--pipelineName,TestCustomXMLParser,--inputXmlLocation,s3://{input_bucketname}/{input_key},--outputFormat,parquet,--outputLocation,s3://{output_bucketname}/{output_key}, --customer_id {customer_id}
  


**In airflow, define the variables ``ENV``, ``INPUTPATH``, ``OUTPUTPATH`` and ``customer_id`` used in the configuration node as below:**

.. figure:: ../../_assets/user-guide/pipeline/airflow_variable.PNG
   :alt: airflow variables
   :width: 30%


