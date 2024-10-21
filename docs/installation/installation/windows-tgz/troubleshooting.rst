Troubleshooting
^^^^^^^^^^^^^^^^

Running into an exception when saving files
++++++++++++++++++++++++++++

    org.apache.spark.SparkException: Job aborted due to stage failure: Task 1 in stage 33.0 failed 1 times, most recent failure: Lost task 1.0 in stage 33.0 (TID 131, localhost): java.io.IOException: (null) entry in command string: null chmod 0644 
    
If you run into an exception like above, then there is problem with the setup of ``winutils.exe``.


    
    

