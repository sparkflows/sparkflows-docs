Installation
--------------------

How can I install Fire Insights?
===========

You can download Fire Insights from https://www.sparkflows.io/

Install documentation is at : https://docs.sparkflows.io/en/latest/installation/installation/index.html

Installation Pre-requisites
===========

Below are the pre-requisites for installing Fire:

* JDK 1.8+ installed on the machine.

* Java and JAR have to be in the PATH.

* If running on an Apache Spark cluster, Apache Spark 2.3+ is needed on the cluster.

* 8GB+ of RAM available on the machine.


With which user should Fire be installed?
===========

If Fire needs to be connected with an Apache Spark cluster the below is needed:

* Fire needs to be installed as a user which can impersonate other users. Impersonation for this user has to be set up in HDFS configs.
* If you disable impersonation in Fire, then the user with which Fire is installed needs to be able to submit jobs to the cluster.

More Details are available here : https://www.sparkflows.io/connecting-sparkflows-with-spark-cl



How can I log into Fire Insights after Installation?
============

The out of the box installation of Fire Insights comes with 2 users:

  * Username : admin   Password : admin
  * Username : test   Password : test
  
How can I load the sample projects?
===========

Fire Insights comes with 28+ Projects and 200+ examples out of the box.

As an admin, you can load all the sample projects or selected ones.

Follow the below steps for loading the sample projects:

  * Load in as the **admin** user.
  * Go to **Administration/Sample Projects**.
  * Use the page to load all the sample projects or selected ones.
  
  
  
