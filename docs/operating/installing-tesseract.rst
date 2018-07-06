Running Tesseract in Sparkflows
=====================

In order to run Tesseract, perform the below installation steps:

Download & Install the Tesseract Language Data  files
-------
 
* Download and Install the tesseract language data files on each of the worker nodes of the cluster
* Install them in the same directory on each of the worker nodes
  * git clone https://github.com/tesseract-ocr/tessdata.git


Set TESSDATA_PREFIX as an Environment Variable and restart the Sparkflows server
-----

* Point the environment variable TESSDATA_PREFIX to the tessdata directory
* export TESSDATA_PREFIX=/home/centos/tessdata
* Restart the sparkflows server

*  If the above is not done correctly, then the Sparkflows server would exit when any OCR node is run


Include TESSDATA_PREFIX in spark configs when submitting the job
--------

Include the following in spark configs when running workflows containing the OCR node:

* --conf spark.executorEnv.TESSDATA_PREFIX=/home/centos/tessdata
* where the tesseract language data files are in /home/centos/tessdata directory on each of the worker nodes



