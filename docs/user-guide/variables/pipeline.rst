Pipeline
============
Sparkflows allows you to utilize dynamic variables in pipelines, enabling you to efficiently manage and adapt your data processing tasks. This capability empowers you to pass variables in a PySpark Node using defined parameters, enhancing the flexibility and effectiveness of your workflow. This document outlines the steps to pass variables in a PySpark Node using defined parameters.

Below are the steps:

Step 1: Defining Parameters in Pipeline
---------------------------------

#. Click on the **plus button** located at the top right corner to access the dialog box for defining parameters.

   .. figure:: ../../_assets/user-guide/variables/pipeline/plus-button-pyspark.png
      :alt: variables_userguide
      :width: 65%



#. In the **dialog box**, specify the **parameters** you wish to utilize. 

   For instance, if you want to filter cities such as 'Bangalore' and 'Pune', define a parameter named city and set its values accordingly.

   .. figure:: ../../_assets/user-guide/variables/pipeline/dialog-box-pyspark.png
      :alt: variables_userguide
      :width: 65%



Step 2: Accessing Variables in PySpark Code
----------------------------------------
#. In the PySpark code node, access the defined parameters using the **${variable_name}** notation as shown below:

   .. figure:: ../../_assets/user-guide/variables/pipeline/conditional-expression-pyspark.png
      :alt: variables_userguide
      :width: 65%



   In lines 20 and 21, you can see how parameters are passed. For example, if you want to filter cities like 'Bangalore' and 'Pune', you can map it as **citylst = ${city}**, where city comes from the defined parameter. This method uses ${variable_name} for passing parameters.


Output
--------------

The image below shows the data filtered after utilizing variable:

   .. figure:: ../../_assets/user-guide/variables/pipeline/changed-output-pyspark.png
      :alt: variables_userguide
      :width: 65%






