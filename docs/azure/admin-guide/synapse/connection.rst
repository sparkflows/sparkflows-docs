Azure Synapse Connection
=======

Sparkflows enable you to create Azure Synapse as a Compute Connection and submit the Job onto it.

Inorder to Create Azure Synapse Compute Connection in Sparkflows, User need to have below pre-requisites in Azure while configuring.

Azure pre-requisites
++++

The Azure pre-requisites needed to Create Azure Synapse Compute Connection in Sparkflows:

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Client Id	
     - Client Id
     - Client Id for ADLS Configuration
   * - Client Secret Key
     - Client Secret Key generated during registration of app in Azure portal.
     - Client Secret Key
   * - Azure Synapse URL	
     - Azure Synapse URL	
     - Synapse URL
   * - Pool Name	
     - Synapse Pool Name	
     - Synapse Pool Name
   * - Tenant Id	
     - Azure Tenant Id	
     - Azure Tenant Id

Azure Synapse Connection
++++++++++++++

Sparkflows enables you to create "Azure Synapse Connection" and use it to submit jobs/workflows. Connections can be at various levels:

  * Global  : Everyone has access to these connections.
  * Group   : Users belonging to the group have access to these connections.
  * Project : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This page show how to create a "Azure Synapse Connection" in Sparkflows.

Enable Azure Synapse in Sparkflows
===========

Login to ``Sparkflows`` application -> ``Administration`` -> ``Configurations`` -> ``Connection`` -> and enable Azure Synapse connection by setting the below parameter:

::

    connection.synapse.enabled : true
