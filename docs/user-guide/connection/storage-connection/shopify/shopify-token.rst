Creating Shopify Token 
===========================

This document explains how to generate and use a **Shopify Admin API access token** using a Custom App.

A Custom App Admin API access token is a token generated inside a Shopify store’s Admin for a custom app.

Step-by-Step Guide to Create the Token
-------------------------------------------

Follow the steps below:

**Step 1: Create a Custom App in the Shopify Admin**
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Log into the store Admin: https://admin.shopify.com/store/<store-name>

2. Go to: Settings → Apps and sales channels

3. Click: Develop apps (may require enabling it)

4. Click: Create an app

5. Give it a name like: sparkflows-bulk-exporter (or your org naming convention)

6. Choose the app owner (a staff account)

 .. figure:: ../../../../_assets/shopify/shopify-create-token-1.png
     :alt: shopify
     :width: 50%

**Step 2: Configure Admin API scopes (permissions)**
+++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Open the app you created.
2. Go to **Configuration**.
3. Under **Admin API integration**, click **Configure**.
4. Select the scopes your connector needs.

Typical scopes include (example only):

- Orders: read_orders

- Products: read_products

- Customers: read_customers (note: customer PII access is restricted by Shopify plan / approval, BASIC plan restricts customer PII information)

 .. figure:: ../../../../_assets/shopify/shopify-create-token-2.png
   :alt: shopify
   :width: 50%


**Step 3: Install the app on the store**
+++++++++++++++++++++++++++++++++++++++++++++

1. In the app page, click **Install app**.
2. Approve the requested scopes.

This “install” step is what actually enables token generation.



**Step 4: Generate / Copy the Admin API access token**
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. After installation:

  - Go to the app page
  - Find **Admin API access token**
  - Copy it and store it securely

 **Treat this token like a password**. Anyone who has it can call Admin APIs within the granted scopes.

 .. figure:: ../../../../_assets/shopify/shopify-create-token-3.png
   :alt: shopify
   :width: 50%


