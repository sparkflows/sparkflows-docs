Backup and Recovery
------

Fire Insights stores the metadata into a Relational Database.

It comes with an embedded H2 database. It scales well for pretty heavy loads and upto 50 users. Sparkflows can be easily configured to run with a MySQL database.

When running with the H2 database, Sparkflows, by default, stores the database files in the user home directory which is running Sparkflows. There are 2 files :

- firedb.mv.db	
- firedb.trace.db

For backup, just copying these files to a backup location is enough. There is no need to stop Sparkflows. It is a good idea to copy it to another machine.


When configured with MySQL, the MySQL database named ``Fire`` needs to be backed up manually or by enabling RDS Auto Backup feature.

Automate Backup of H2 DB
================

Fire Insights enable Administrator to avail options for Automate Backup of H2 DB from UI and can be stored on same vm or in s3 bucket if its accessible from Fire Inisghts Machine.

Below are steps ::

1. Login to ``Fire Insights`` application -> ``Administration`` -> ``Configurations`` -> ``app.db.backup.location`` -> and update path where you want to take backup:

::


    app.db.backup.location /home/sparkflows

.. note:: The path updated should have sufficient permission to write, You may configure s3 bucket if Fire Insights have sufficient privilege to write.

.. figure:: ../_assets/operating/backup/bkp_1.PNG
   :alt: bkp
   :width: 60%

2. Go Back to ``Administration`` -> ``Operations`` and select ``Backup DB``, it will pop up new page with below details:

.. figure:: ../_assets/operating/backup/bkp_2.PNG
   :alt: bkp
   :width: 60%
   
.. figure:: ../_assets/operating/backup/bkp_3.PNG
   :alt: bkp
   :width: 60%   

3. Click on ``Backup``, it will backup the h2 db in zip format and pop up the success msg

.. figure:: ../_assets/operating/backup/bkp_4.PNG
   :alt: bkp
   :width: 60%   
   
.. figure:: ../_assets/operating/backup/bkp_5.PNG
   :alt: bkp
   :width: 60%      

4. You can scheduled depending on requirements on Daily, weekly or monthly basis.

Click on ``Schedule DB Backup`` tab and you will be able to schedule it and save.

.. figure:: ../_assets/operating/backup/bkp_6.PNG
   :alt: bkp
   :width: 60%
