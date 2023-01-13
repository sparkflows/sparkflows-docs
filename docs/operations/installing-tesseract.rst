Configure Tesseract
=====================

In order to run Tesseract, perform the below installation steps:

Download & Install the Tesseract Language Data Files
-------
 
* Download and install the Tesseract language data files on each of the worker nodes of the cluster.
* Install them in the same directory on each of the worker nodes.

  * ``git clone https://github.com/tesseract-ocr/tessdata.git``
* Make sure that the tessdata directory is accessible to all the users.  


Set TESSDATA_PREFIX as an Environment Variable and Restart the Sparkflows Server
-----

* Point the environment variable TESSDATA_PREFIX to the tessdata directory.

  * ``export TESSDATA_PREFIX=/home/centos/tessdata``
* Restart the Sparkflows server.

*  If the above steps are not executed correctly, then the Sparkflows server would exit while running any OCR node.


Include TESSDATA_PREFIX in Apache Spark Configurations When Submitting the Job
--------

Include the following in Apache Spark configurations when running workflows containing the OCR node:

* ``--conf spark.executorEnv.TESSDATA_PREFIX=/home/centos/tessdata``
* The Tesseract language data files are in ``/home/centos/tessdata`` directory on each of the worker nodes.


Error if TESSDATA_PREFIX is not Set Correctly
-----

 
If ``TESSDATA_PREFIX`` is not set correctly, the Apache Spark program would run into the error while displaying error messages as below :

* Error opening data file /Users/saudet/projects/bytedeco/javacpp-presets/tesseract/cppbuild/macosx-x86_64/share/tessdata/eng.traineddata
* Please make sure the TESSDATA_PREFIX environment variable is set to the parent directory of your "tessdata" directory.
* Failed loading language 'eng'.
* Tesseract couldn't load any languages!
