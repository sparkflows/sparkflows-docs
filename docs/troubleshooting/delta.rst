Delta Files
===========

Issue: Failed to find data source `delta` when running the job on EMR cluster
--------

**Description:** Issue with delta jar being used on EMR or version mismatch.

**Resolution:** Make sure to copy appropriate delta jar and pass it on livy connection with comma separated in Fire Jar. 

.. note:: you can check version support from below page

https://docs.delta.io/latest/releases.html
