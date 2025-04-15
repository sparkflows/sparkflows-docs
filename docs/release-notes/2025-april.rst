Version 3.2.99 - April 15th, 2025
=====

New Features
-----

Authentication & Security
+++++

* **Token Expiration Notification :** Advanced email notifications are now sent before a token expires. The **token creator** is also included in the notification list.

* **Snowflake Key-Pair Authentication :** Support for key-pair authentication in Snowflake has been implemented. Secret key names can now be configured in the **Credential Store**.

Cloud & Infrastructure
+++++

* **EBS Root Volume Support :** Introduced support for EBS root volumes, enhancing flexibility in infrastructure setup.

* **Guardian Integration :** Successfully integrated with Guardian to improve platform security and governance.

Data & Workflow Management
+++++

* **Import Variables from File :** Added the ability to import variables directly from a .INI or .JSON file Globally and for a Group.

* **Export Variables to JSON :** Users can now export variables to a JSON file for Global or Group Variables.

* **Curly Braces in Variables :** Enhanced variable parsing to support the use of curly braces in expressions.


Cloud Services Integration
+++++

* **Azure Service Principal Support :** Added support for using Azure Service Principals for API access in Databricks connections.

* **ADLS Support in PySpark :** Enabled ADLS support in PySpark workflows with the required JARs. Interactive mode now functions smoothly.


Enhancements
---------

Execution & Monitoring
+++++

* **Pipeline Execution Page Update :** The page now displays parameter values and connection details when Airflow is enabled, improving visibility during execution.

Databricks Integration
+++++

* **Create Databricks Cluster Enhancements :** Added features to terminate clusters after 30 minutes, enable Spot Instances, use Photon Acceleration, and more.

EMR Integration
+++++

* **Create EMR Pipeline Node :** Enhanced with new fields for Retries and Retry Delay, increasing execution robustness.


Bug Fixes
----

* **Livy Access over HTTPS :** Resolved an issue where Livy was not accessible over HTTPS. Secure access has been successfully validated.

Documentation
------
* **Import Variables using file :** Added documentation to import variables using a correctly formatted .INI or .JSON file for Global or selected Group.
* **Snowflake Key-Pair Authentication :**  Added documentation displaying the capability to create “Snowflake Connection” and use the connection to access various resources using Key-Pair Authentication.
* **Databricks Connection :** Updated documentation for OAuth related configuration setup in a databricks connection. 




















