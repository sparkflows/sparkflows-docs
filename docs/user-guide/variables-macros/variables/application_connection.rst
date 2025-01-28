Variables in Application Connection 
==========

With Sparkflows, you can seamlessly manage dynamic variables within your Application Connection, enhancing their usage. This document demonstrates how to add dynamic variables to your Application Connection, using an example of a variable named **connectionUrl** that contains the database URL for a MySQL connection.

Follow the steps below:


Step 1 : Add the 'connectionUrl' Variable
------------------

#. Navigate to the **Administration** page and click on **Variables** card.
#. Click on **Add Variable** button from the variables list page. An 'Add Variable' form will be displayed as shown below:

   .. figure:: ../../../_assets/user-guide/variables/application-connection/connection-variable-create.png
      :alt: variables_userguide
      :width: 65%


#. To create a variable, enter the desired values in the above fields as follows and click on **Save** button.

   * **KEY:** Enter **connectionUrl**.
   * **VALUE:** Add the MySQL connection URL.
   * **DESCRIPTION:** It is optional.

Step 2 : Create a MySQL Connection using the 'connectionUrl' Variable
------------------------------

#. Navigate to the **Administration** page and click on the **Global/Group Connections** card.
#. Click on **Add Connection** button from the connections list page. An 'Add Connection' form will be displayed as shown below.

   .. figure:: ../../../_assets/user-guide/variables/application-connection/add-connection-using-variable.png
      :alt: variables_userguide
      :width: 65%

#. To create a connection, enter the desired values in the above required fields as follows:

   * Select **Storage** as the category.
   * Select **MySQL** as the connection type.
   * Eenter **${connectionUrl}** in URL to use the variable.
   * Fill the remaining fields with the required details. 

Step 3 : Test the Connection
------------------------------

#. After filling the required details in the previous step, click on **Test Connection** button.
#. If the 'connectionUrl' variable is correctly set and all other connection details are accurate, a message "Successfully Connected" will appear on the form as shown below, indicating that the variable’s value has been correctly replaced.

   .. figure:: ../../../_assets/user-guide/variables/application-connection/test-connection-using-variable.png
      :alt: variables_userguide
      :width: 65%

Now this connection containing dynamic variables can be used seamlessly throughout Sparkflows.

By following the steps above, you can seamlessly incorporate dynamic variables into your application connections. This allows the connections to adapt to changing conditions or input data, enhancing their flexibility and overall usability.




