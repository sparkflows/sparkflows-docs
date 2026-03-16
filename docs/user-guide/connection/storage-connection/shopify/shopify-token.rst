Installing Shopify App and Creating Token
=================================================

This document explains how to generate and use a **Shopify API client ID** and **client secret** using the Shopify Dev Dashboard.


1. Create an App in Shopify
-------------------------------------------

Follow the steps below to create an app in Shopify:

1. Log in to the store Admin: https://admin.shopify.com/store/<store-name>

2. Go to: **Settings -> Apps**

3. Click: **Develop apps** (may require enabling it first)

4. Click: **Build Apps in Dev Dashboard**

   This would then redirect you to the DEV DASHBOARD page with a link similar to: https://dev.shopify.com/dashboard/xxxx/apps

5. Click on **Create App**

   .. figure:: ../../../../_assets/shopify/dev-dashboard-create-app.png
     :alt: shopify
     :width: 50%

6. Enter a name like: **sparkflows-bulk-exporter** (or your organization naming convention)

7. In the **Access** section, click **Select scopes** on the right hand side of the field, select the required scopes and then click **Release**.

   .. figure:: ../../../../_assets/shopify/dev-dashboard-choose-scopes.png
     :alt: shopify
     :width: 50%

8. Next, click the **Settings** button in the left sidebar. Here, we can get access to the **client_id** and **client_secret** of the application, which would have the permissions to access data based on the scopes selected in the previous step.

   .. figure:: ../../../../_assets/shopify/dev-dashboard-settings.png
     :alt: shopify
     :width: 50%

9. Next, install the app in your store. To do this, click the app name in the left sidebar.

   .. figure:: ../../../../_assets/shopify/dev-dashboard-install-app.png
     :alt: shopify
     :width: 50%

10. Click **Install** app, this will take you to the **login or store selection** page.

    .. figure:: ../../../../_assets/shopify/store-login-page.png
       :alt: shopify
       :width: 50%

11. After logging in, click on **Install**.

    .. figure:: ../../../../_assets/shopify/app-install-page.png
       :alt: shopify
       :width: 50%


12. You should then be able to see the installed app on the **Settings -> Apps** page of your store.

    .. figure:: ../../../../_assets/shopify/installed-app-on-settings-page.png
       :alt: shopify
       :width: 50%
