Configuring Max Upload File Size
--------------------------------

Fire allows users to upload files into HDFS/S3/DBFS etc. through their Browser.

The settings which controls it is in ``conf/application.properties``::

    # max file size
    multipart.maxFileSize: 10Mb
    multipart.maxRequestSize: 10Mb

