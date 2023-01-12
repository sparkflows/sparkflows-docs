JAR File Execution Examples
-----------------------------------

Let's take a scenario where through CI/CD pipeline, the application jar file is built successfully and pushed into the S3 bucket.


Below are steps to execute the jar file:

Step 1: Copy Jar File from s3 Path to /tmp Directory.
====================================================
::
    
      aws s3 cp s3://bucket-name/example-application.jar /tmp
      
      
Step 2: Execute Jar File from /tmp Directory.
============================================
::
    
      java -cp /tmp/example-application.jar MainClass

  
  
In Fire Insights, both steps can be run with UnixShellCommands Node.




.. figure:: ../../_assets/tutorials/quickstart/code.png
   :width: 90%
   :alt: UnixShellCommands Node



    
    
    
