Local FileSystem
=====

Fire Insights enables you to use the Local FileSystem by default when no Compute is enabled or S3 is configured.

By default, Fire Insights bundles sample data within its binary, located in the data folder of the Fire home directory.

If you wish, you can copy the data folder to your preferred location and configure the path for Fire Insights to use. 

To configure the path, follow the steps below :

Step 1 : Login to Fire Insights
-----------

#. Go to Fire Insights Login Page.
#. Enter your credentials to sign in.

Step 2 : Go to Administration Page
----------
From the Fire Insights home page, click on the **ADMINISTRATION** tab located in the top bar.

Step 3 : Go to Configurations Page
------------
From the administration page, click on the **Configurations** option.

Step 4 : Go to HDFS Page
--------------
From the configurations page, click on the **HDFS** tab located in the upper-middle bar.

Step 5 : Update the Path
-----------
#. Click on the **edit icon** connected to the field named as **hdfs.localHomeDirForAllUsers**.
#. Enter the path in the **Value** column. 

   ::

          hdfs.localHomeDirForAllUsers: $PATH of data configured


   .. figure:: ../../_assets/user-guide/access-filesystem/hdfs_config.PNG
      :alt: userguide
      :width: 60% 

#. Click on the **Save Configurations** button to save and update the path.

Step 5 : Access the File System
------------
Once you save the above configuration, go to **DATA/File System**, and it will point to the same location you configured earlier.

    .. figure:: ../../_assets/user-guide/access-filesystem/hdfs_local.PNG
       :alt: userguide
       :width: 60% 

Now, you can easily upload data and use it in your workflow or dataset.
