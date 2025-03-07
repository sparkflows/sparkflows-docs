Salesforce Setup for JDBC Connection
===================================

This document outlines the steps to configure a Salesforce account for JDBC access.

1. **Create a Connected App**
-----------------------------------
- Log in to **Salesforce** → **Setup** → **App Manager** → **New Connected App**.
- Fill in details:
  - **App Name**: `SalesforceJDBC`
  - **API Name**: `SalesforceJDBC`
  - **Contact Email**: Your Email
- **Enable OAuth Settings**:
  
  - **Callback URL**: http://localhost:8080/callback
  
  - **OAuth Scopes**:
    - `Access and manage your data (API)`
    - `Perform requests on your behalf (refresh_token, offline_access)`
    - `Full access (full)`
  
  - **Enable Username-Password OAuth Authentication Flow**
- **Save & Continue** (Wait 5-10 min)
- Copy **Consumer Key** & **Consumer Secret**.

2. **Configure App Permissions**
-----------------------------------
- Go to **Setup** → **Manage Connected Apps** → **SalesforceJDBC**.
- Click **Manage Profiles** → Assign **System Administrator**.
- Go to **Setup** → **Security** → **Connected Apps OAuth Usage**.
- Find **SalesforceJDBC**, click **Manage**, 
And then, set:  
  - **Permitted Users**: `All users may self-authorize`
  
  - **IP Relaxation**: `Relax IP restrictions`
- **Save Changes**.

3. **Adjust Security & Field History Tracking**
-----------------------------------------------
- **Security**:
  - **Setup** → **Session Settings** → **Relax IP Restrictions**.
- **Field History Tracking**:
  - **Setup** → **Object Manager** → Select Object → **Fields & Relationships** → **Set History Tracking**.
  - Enable tracking for relevant fields.

4. **Get Security Token**
--------------------------
- **Profile Icon** → **Settings** → **Reset My Security Token**.
- Click **Reset**, check your email.
- Append the **security token** to your password when logging in (e.g., `passwordSECURITYTOKEN`).

5. **Obtain OAuth Access Token**
---------------------------------
Retrieve a token using cURL:

.. code-block:: sh

    curl --location 'https://login.salesforce.com/services/oauth2/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=password' \
    --data-urlencode 'client_id=YOUR_CLIENT_ID' \
    --data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
    --data-urlencode 'username=YOUR_SALESFORCE_USERNAME' \
    --data-urlencode 'password=YOUR_PASSWORD_SECURITYTOKEN'

**Example Response:**

.. code-block:: json

    {
        "access_token": "00Dxx0000001234!AQEAQEXX",
        "instance_url": "https://your-instance.salesforce.com",
        "token_type": "Bearer"
    }

6. **JDBC Connection Setup**
-----------------------------
Here's the git repository for Salesforce data cloud jdbc: https://github.com/forcedotcom/datacloud-jdbc

**JDBC URL Format:**
- OAuth Authentication:

  .. code-block:: sh

      jdbc:salesforce-datacloud://login.salesforce.com;AuthType=OAuth;AccessToken=YOUR_ACCESS_TOKEN;

- Username & Password:

  .. code-block:: sh

      jdbc:salesforce-datacloud://login.salesforce.com;User=YOUR_USERNAME;Password=YOUR_PASSWORD_SECURITYTOKEN;


Install the JDBC Driver
--------

In order to install the JDBC driver copy the driver jdbc jar file into ``fire-user-lib`` and ``fire-server-lib`` directories under the Fire installation home directory.

Restart Fire Server
------------

Once you have copied the JDBC driver into the required folder, restart the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.

This will restart the Fire services automatically.

Or else, you can also wait for 60 minutes and the JDBC driver would be automatically registered with Fire Insights.

Create the Salesforce datacloud Connection
-----

Create the Salesforce Data Cloud Connection at Global, Group or Project level.

Connection Details
++++

In Fire Insights UI, go to Administration, then navigate to `Global/Group Connections` and then on `Add Connection`. Enter the configuration details with the help of table given below and click on ``Add Connection``.
                         
Test Connection and Save
+++++

Once you have entered the connection details, click on ``Test Connection``. If the connection is successful,  click on ``Save`` to save the connection. 

Now, you are ready to start using the Connection in workflows.

  .. Note:: Make sure that salesforce datacloud URL should be accessible from Sparkflows web server URL.

7. **Troubleshooting**
-----------------------

- **No authentication settings provided**  
  
  - **Cause:** Incorrect JDBC URL format  
  
  - **Solution:** Ensure `AuthType=OAuth` and `AccessToken` are set  

- **INVALID_LOGIN** 

  - **Cause:** Incorrect credentials or missing security token

  - **Solution:** Append the security token to your password  

- **No suitable driver found**  
  - **Cause:** Missing JDBC JAR file  

  - **Solution:** Ensure `jdbc-0.24.0.jar` is correctly referenced in Spark or Java  

- **invalid_grant**  

  - **Cause:** OAuth app permissions issue  

  - **Solution:** Ensure OAuth scopes include `full, api, refresh_token`  


**Summary**
=============
1. **Create a Connected App** 
2. **Assign OAuth Scopes & Permissions** 
3. **Relax Security & Enable Field Tracking** 
4. **Obtain Security Token** 
5. **Get OAuth Access Token via API** 
6. **Use JDBC Connection** 


