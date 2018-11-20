OCR with Tesseract
==============

In order to run Tesseract, the below Installation Steps have to be performed.

Download & Install the Tesseract Language Data  files
-----------------------------------------------------

* Download and Install the tesseract language data files for Version 3.X on each of the worker nodes of the cluster::

    https://github.com/tesseract-ocr/tessdata/releases
    wget https://github.com/tesseract-ocr/tessdata/archive/3.04.00.tar.gz
  
* Install them in the same directory on each of the worker nodes::

    git clone https://github.com/tesseract-ocr/tessdata.git
  

Include TESSDATA_PREFIX in spark configs when submitting the job
-------------------------

* Include the following in spark submit configs when running workflows containing the OCR node::

    --conf spark.executorEnv.TESSDATA_PREFIX=/home/ec2-user/tessdata
    
* where the tesseract language data files are in ``/home/ec2-user/tessdata`` directory on each of the worker nodes

Error if TESSDATA_PREFIX is not set correctly
------------------

If TESSDATA_PREFIX is not set, the spark program would run into the error below::

    Error opening data file /Users/saudet/projects/bytedeco/javacpp-presets/tesseract/cppbuild/macosx-x86_64/share/tessdata/eng.traineddata
    Please make sure the TESSDATA_PREFIX environment variable is set to the parent directory of your "tessdata" directory.
    Failed loading language 'eng'
    Tesseract couldn't load any languages!
  
  

