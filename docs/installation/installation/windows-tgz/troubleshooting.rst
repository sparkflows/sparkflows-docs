Troubleshooting
^^^^^^^^^^^^^^^^

Could not create Java Virtual Machine
+++++++++++++++++++++++++

Problem
-------

When starting the fire server, running into the error "Could not create Java Virtual Machine".

Solution
-------

This problem can be because ::

  * JDK 32 bit instead of 64 bit
  * OR Java 8 is not installed. Some other version of Java is installed.

Running into an exception when saving files
++++++++++++++++++++++++++++

Problem
-------

org.apache.spark.SparkException: Job aborted due to stage failure: Task 1 in stage 33.0 failed 1 times, most recent failure: Lost task 1.0 in stage 33.0 (TID 131, localhost): java.io.IOException: (null) entry in command string: null chmod 0644 

Solution
-------

If you run into an exception like above, then there is problem with the setup of ``winutils.exe``.


    
    

