Glue Connections
----------------

Sparkflows enabled you to create Aws Glue Connection and use the connection to submit job on Aws Glue.

Connections can be at various levels:

  * Global : Everyone has access to these connections
  * Group : Users belonging to the group have access to these connections
  * Project : The owner of the project and the groups with which the Project has been shared with have access to the Project level connections

Below are steps on how to create Glue Connection:

1. Enable Glue in Sparkflows

Login to ``Sparkflows`` application -> ``Administration`` -> ``Configurations`` -> ``Connection`` -> and enable Glue connection by setting the below parameter:

::

    connection.glue.enabled : true

2. Create Global Connections

Once you save the above Configuration, navigate to ``Administration`` -> ``Global Connections`` -> ``Add Connections`` as shown below:

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/administration.PNG
   :alt: livy
   :width: 60%

3. Add Connection For Group

Navigate to ``Administration`` -> ``Global Connections`` -> ``Add Connections`` -> ``Add Connection For Group`` which pop up a new windows -> Select ``Compute Connection`` and other parameters as shown below:


4. Update below parameter as per our configurations

Now update below parameter as per AWS configurations

GENERAL Tab :

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Connection name
     - Connection name
     - Connection name
   * - Postback Url
     - Postback Url
     - Postback Url
   * - Title
     - Title
     - Title
   * - Description
     - Connection Description

GLUE Tab :

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Script Location
     - Glue script location
     - s3://aws-glue-scripts/scripts/FireGlueApp.scala
   * - IAM Role
     - AWS IAM Role
     - AWSGlueServiceRole-Sparkflows
   * - Glue Main Class  
     - Glue Main class to execute
     - FireGlueApp
   * - Default Arguments
     - Pass any parameters as default arguments
     - --TempDir s3://aws-glue-temporary
   * - Glue Version
     - Glue Version. If empty it takes default glue version.
     - 2.0
   * - Glue Language
     - Glue Language. Input should scala or python
     - scala
   * - Extra Jars
     - Extra Jar file path pass in default arguments
     - s3://aws-glue-scripts/fire-spark_2.4-core-3.1.1-jar-with-dependencies.jar
   * - S3 Path
     - S3 bucket location where workflow json file gets uploaded for execution
     - s3://aws-glue-scripts/workflow-json
   * - Glue Connections
     - Glue connection names. Input the glue connection names as comma separated value like Glue-conn, Glue-conn1
     - Glue-Fire
   * - AWS Region
     - AWS Region of Glue
     - AWS Region
   * - Workflow Files Directory
     - Directory used for Writing the workflow files
