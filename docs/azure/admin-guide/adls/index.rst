Azure Data Lake Storage Guide
====

Fire Insights integrates with various data systems, including Azure Data Lake Storage (ADLS), allowing users to configure and automate the flow of data to and from ADLS.

Azure Data Lake Storage (ADLS) can be configured and accessed using two primary methods for authentication and authorization: Service Principal and Managed Identity. Here's a description of each:

#. Using Service Principal

   A Service Principal is a security identity within Azure Active Directory (Azure AD) that can be used to authenticate applications or services. When configuring ADLS with 
   a Service Principal, you typically create an Azure AD application, assign it the necessary permissions (such as read, write, or manage access to ADLS), and use the 
   application's credentials (client ID and client secret or certificate) to authenticate programmatically.

   Service Principal is often used for non-human (application or service) access scenarios where you need to interact with ADLS from an external service, automation script, 
   or third-party system.

#. Using Managed Identity

   A Managed Identity is a feature of Azure Active Directory that provides an identity to an Azure service (e.g., Virtual Machines, Azure Functions, Azure App Service, etc.) 
   without needing to manage credentials explicitly.


.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
    
    :doc:`/azure/admin-guide/adls/service-principal`

    Service Principal setup
    
    ---

    :doc:`/azure/admin-guide/adls/adls-configuration`

    ADLS Configuration In Sparkflows
     


.. toctree::
   :hidden:

   service-principal.rst
   adls-configuration.rst
   
