Shopify
======================

Sparkflows has provided the following processor for reading data from Shopify.

1. Read Shopify

Read Shopify Workflow
--------

A user can use this processor to read data from a Shopify resource.

**Example Workflow**
+++++++++++++++++++++

The below workflow does the following:

* Reads data from a Shopify resource.
* Prints a few records from the Shopify resource.

  .. figure:: ../../_assets/shopify/wf_read.png
     :alt: shopify
     :width: 60%

**Processor Configuration**
++++++++++++++++++++++++++++++

Below are the processor configuration details:

* ``CONNECTION``  : Connection created for Shopify.
* ``API Version`` : Shopify API Version.
* ``Use GraphQL Query`` : True/False.
* ``GraphQL Query`` : Field to add a GraphQL query if True is selected above.
* ``Resource Name`` : Shopify Resource Name.
* ``Add Filter`` : True/False to add filters on data.
* ``Filter`` : Field to add filters if True is selected above. 
  
  .. figure:: ../../_assets/shopify/ReadShopify.png
     :alt: shopify
     :width: 60%

**Processor Output**
++++++++++++++++++++++

The output of the processor is displayed as below:

  .. figure:: ../../_assets/shopify/processor_read.png
     :alt: shopify
     :width: 60%
