Swagger REST APIs
=========

Fire Insights enables you to use **Swagger REST APIs**. It can be accessible only when the admin provides the privilege to access it.

This document outlines the steps to enable Swagger for REST APIs.

Follow the steps given below:

Step 1 : Enable Swagger in application.properties
++++++++++

#. Open the application.properties file.
#. Add the following line next to application.properties to enable Swagger:

   ::

       swagger.enable=true
    
#. After updating the **application.properties**, restart the Fire Insights server.

Step 2 : Enable Swagger from the Configurations Page
+++++++++++++++++++++++++++++

#. **Login** to Fire Insights using your **Credentials**.
#. Navigate to **Administration -> Configurations -> UI Settings**.
#. Find the **uiSettings.enableSwagger** setting and set its value to **true**. 

   .. figure:: ../../_assets/installation/metrics/swagger.PNG
      :alt: metrics
      :width: 60%

Step 3: Access Swagger REST APIs
++++++++++++++++++++++++++++++

Once Swagger is enabled and the server is running, you can access the Swagger REST API interface using the following URL:

::

    https://localhost:port/swagger-ui.html

    
.. figure:: ../../_assets/installation/metrics/ui.PNG
   :alt: metrics
   :width: 60% 

    
.. note::  Make sure to change the localhost with respective IP or domain name and the port on which the Fire Insights is running.    

