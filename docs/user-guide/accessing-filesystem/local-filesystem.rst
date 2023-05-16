Local FileSystem
=====

Fire Insights enable you use Local FileSystem by default when there is no Compute is enabled or s3 is configured.

By default Fire Insights sample data is being bundled in Fire Insights binary with `data` folder in home directory.

you can copy ``data`` folder to your specified location and configured the path to use in Fire Insights.

you can login to Fire Insights go to ``Administration/Configurations`` and update below in ``HDFS`` tab:

::

    hdfs.localHomeDirForAllUsers : $PATH of data configured

.. figure:: ../../_assets/user-guide/access-filesystem/hdfs_config.PNG
   :alt: userguide
   :width: 60% 
   
Once the above configuration got saved, you can go to ``DATA/File System``, it would point you the same location configured earlier.

.. figure:: ../../_assets/user-guide/access-filesystem/hdfs_local.PNG
   :alt: userguide
   :width: 60% 

Now you can upload data and use it in workflow, dataset.
