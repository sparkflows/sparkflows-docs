AWS Version Compatibility
==========

EMR Versions
-----------

The below page lists the version of Apache Spark used with various versions of AWS EMR.

https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Spark-release-history.html

It also lists the compatability matrix of Spark version and Delta lake version.

https://docs.delta.io/latest/releases.html

AWS EMR has a bootstrap script which gets executed when it comes up. Fire Insights uses the bootstrap script to install the needed python packages.

Updates to bootstrap and wheel file
-------------

Make the below updates to the example bootstrap script for different versions of EMR.

* For ``emr-6.2.1``, no changes to bootstrap script are needed. It uses ``h2o-pysparkling-3.0``
* For ``emr-6.6.0`` in the bootstrap script and the wheel file, the version of ``h2o-pysparkling`` needs to be updated to ``h2o-pysparkling-3.2==3.36.1.2.post1``
* For ``emr-6.9.0``, in the bootstrap script and the wheel file, the version of ``h2o-pysparkling`` needs to be updated to ``h2o-pysparkling-3.3``

Example Bootstrap Script : EMR 6.6.0
------------
  
  sudo yum install -y python3-devel

  sudo yum install -y libtiff-devel libjpeg-devel openjpeg2-devel zlib-devel freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel harfbuzz-devel fribidi-devel libraqm-devel libimagequant-devel libxcb-devel

  sudo pip3 install --user --upgrade pip setuptools

  sudo pip3 install -U astor==0.7.1 \
  Cython \
  grpcio==1.32.0 \
  h5py==2.10.0 \
  jedi==0.13.3 \
  Markdown==3.0.1 \
  mock==2.0.0 \
  numpy==1.19.5 \
  pandas==1.1.2 \
  parso==0.3.4 \
  pbr==5.1.3 \
  prompt-toolkit==2.0.10 \
  protobuf==3.9.2 \
  ptpython==2.0.4 \
  Pygments==2.3.1
  
  sudo pip3 install -U scikit-learn==0.23.2 \
  scipy==1.4.1 \
  six==1.15.0 \
  termcolor==1.1.0 \
  tornado==6.0.1 \
  wcwidth==0.1.7 \
  Werkzeug==0.14.1 \
  joblib==0.14.1

  sudo pip3 install -U boto3==1.0.0 \
  scorecardpy==0.1.9.2 \
  jmespath==0.7.1 \
  JayDeBeApi==1.2.1 \
  statsmodels==0.13.2 \
  h2o-pysparkling-3.2==3.36.1.2.post1 \
  markupsafe==2.0.0 \
  jinja2==3.0.3 \

  sudo pip3 install great_expectations==0.13.0

  sudo pip3 uninstall -y numpy

  sudo pip3 install -U numpy==1.20.0

  sudo pip3 install delta-spark==2.0.2

  sudo pip3 uninstall -y fire

  wget https://sparkflows-release.s3.amazonaws.com/fire/docker/docker-ubuntu/fire-3.2.0-py3-none-any.whl

  sudo pip3 install fire-3.2.0-py3-none-any.whl  

  sudo pip3 install -U numpy==1.20.0


Example Bootstrap Script : EMR 6.2.1
------------
  
  sudo yum install -y python3-devel

  sudo yum install -y libtiff-devel libjpeg-devel openjpeg2-devel zlib-devel freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel harfbuzz-devel fribidi-devel libraqm-devel libimagequant-devel libxcb-devel

  sudo pip3 install --user --upgrade pip setuptools

  sudo pip3 install -U astor==0.7.1 \
  Cython \
  grpcio==1.32.0 \
  h5py==2.10.0 \
  jedi==0.13.3 \
  Markdown==3.0.1 \
  mock==2.0.0 \
  numpy==1.19.5 \
  pandas==1.1.2 \
  parso==0.3.4 \
  pbr==5.1.3 \
  prompt-toolkit==2.0.10 \
  protobuf==3.9.2 \
  ptpython==2.0.4 \
  Pygments==2.3.1
  
  sudo pip3 install -U scikit-learn==0.23.2 \
  scipy==1.4.1 \
  six==1.15.0 \
  termcolor==1.1.0 \
  tornado==6.0.1 \
  wcwidth==0.1.7 \
  Werkzeug==0.14.1 \
  joblib==0.14.1

  sudo pip3 install -U boto3==1.0.0 \
  scorecardpy==0.1.9.2 \
  jmespath==0.7.1 \
  JayDeBeApi==1.2.1 \
  statsmodels==0.13.2 \
  h2o-pysparkling-3.0 \
  markupsafe==2.0.0 \
  jinja2==3.0.3 \

  sudo pip3 install great_expectations==0.13.0

  sudo pip3 uninstall -y numpy

  sudo pip3 install -U numpy==1.20.0

  sudo pip3 install deltalake==0.8.0

  sudo pip3 uninstall -y fire

  wget https://sparkflows-release.s3.amazonaws.com/fire/docker/docker-ubuntu/fire-3.1.0-py3-none-any.whl

  sudo pip3 install fire-3.1.0-py3-none-any.whl  

  sudo pip3 install -U numpy==1.20.0


Delta Support
------------

For delta support, in Spark workflow include the below jars in Livy connection.

 * For ``emr-6.2.1`` include the JAR with the exact version: ``delta-core_2.12-0.8.0.jar``

 * For ``emr-6.6.0`` include the two JARs with the exact version: ``delta-core_2.12-2.0.1.jar`` and ``delta-storage-2.0.1.jar``

 * For ``emr-6.9.0`` include the two JARs with the exact version: ``delta-core_2.12-2.1.0.jar`` and ``delta-storage-2.1.0.jar``


For delta support, in the Pyspark workflow include the below in the EMR Bootstrap script::

  aws s3 cp s3://sparkflows-release/fire/delta/delta-core_2.12-0.8.0.jar /usr/lib/spark/jars/


In Pyspark REPL/node, include the below to import and use the delta packages::

  spark.sparkContext.addPyFile("s3://sparkflows-release/fire/delta/delta-core_2.12-0.8.0.jar")




