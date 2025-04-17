Version 3.2.99 - April 15th, 2025
=====

New Features
-----

Authentication & Security
+++++

* **Token Expiration Notification :** Users now receive an advanced email notification before a token expires. By default, notifications are sent only to the *token creator*. Configuration available under Configurations → App to customize recipients.

* **Snowflake Key-Pair Authentication :** Support for key-pair authentication in Snowflake has been implemented. 

Pipeline
+++++

* **EBS Root Volume Support :** Added fields related to EBS Root Volume in the Create EMR pipeline node for enhanced configuration.


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

Pipeline
+++++

**Execution & Monitoring**

  * **Pipeline Execution Page Update :** The page now displays parameter values and connection details when Airflow is enabled, improving visibility during execution.

**Databricks Integration**

  * **Create Databricks Cluster Enhancements :** Added features to terminate clusters, enable Spot Instances, use Photon Acceleration, and more.

**EMR Integration**

  * **Create EMR Pipeline Node :** Enhanced with new fields for Retries and Retry Delay, increasing execution robustness.


Bug Fixes
----

* **Livy Access over HTTPS :** Resolved an issue where Livy was not accessible over HTTPS. 

Documentation
------
* **Import Variables using file :** Added documentation to import variables using a correctly formatted .INI or .JSON file for Global or selected Group.
* **Export Variables to JSON file :** Added detailed documentation for exporting Global and Group-level variables to JSON, including visibility settings, steps, and structured export formats.
* **Snowflake Key-Pair Authentication :**  Added documentation displaying the capability to create 'Snowflake Connection' and use the connection to access various resources using Key-Pair Authentication.
* **Databricks Connection :** Updated documentation for OAuth related configuration setup in a databricks connection. 
* **Variables in Pipelines :** Updated documentation for using dynamic pipeline parameters in PySpark nodes with ${variable_name} and {variable_name} syntax to enhance flexibility and reuse across workflows.



















