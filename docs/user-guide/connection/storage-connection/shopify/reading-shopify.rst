Read from Shopify
======================

Sparkflows has provided the following processor for reading data from Snowflake.

1. Read Shopify

Read Shopify Workflow
--------

A user can use this processor to read data from a Shopify resource.

**Processor Configuration**
++++++++++++++++++++++++++++++

Below are the processor configuration details:

* ``CONNECTION``  : Connection created for Shopify.
* ``API Version`` : Shopify API Version.
* ``Use GraphQL Query`` : True/False.
* ``GraphQL Query`` : Field to add GraphQL Query if selected True above.
* ``Resource Name`` : Shopify Resource Name.
* ``Add Filter`` : True/False to add filters on data.
* ``Filter`` : Field to add filters if selected True above. 

  .. figure:: ../../../../_assets/shopify/ReadShopify.png
     :alt: shopify
     :width: 60%


**Example Workflow**
+++++++++++++++++++++

The below workflow does the following:

* Reads data from a Shopify resource.
* Prints a few records of the Shopify resource.

  .. figure:: ../../../../_assets/shopify/wf_read.png
     :alt: shopify
     :width: 60%

Processor Output
++++

  .. figure:: ../../../../_assets/shopify/processor_read.png
     :alt: shopify
     :width: 60%
