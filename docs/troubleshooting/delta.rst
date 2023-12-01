Delta Files
===========

This document explains some of the common issues and corresponding resolutions related to Delta Files.

1. EMR Cluster Job Failure: Unable to Locate 'delta' Data Source
-------------------------------------

**Problem**
++++++

Failed to find the 'delta' data source when running the job on the EMR cluster, indicating a potential issue with the Delta JAR being used on EMR or a version mismatch.

**Solution**
++++++

Make sure to copy appropriate Delta JAR and pass it on livy connection with comma separated in Fire JAR. 

.. note:: You can check version support from below page:

           https://docs.delta.io/latest/releases.html
