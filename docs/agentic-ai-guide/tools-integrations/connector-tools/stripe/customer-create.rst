:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Customer</p>

Create a customer
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Customer</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a Stripe customer and returns it with its new id (cus\_...). Use it to register a buyer before invoicing or subscribing them; to change an existing customer use Customer update.

Prerequisites
-------------

* **Connection:** Stripe connection. See :doc:`the Stripe prerequisites <../stripe>`.
* The connection's account must be allowed to change this data in Stripe.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``email``
     - text
     - No
     - The customer's email address; Stripe does not require it to be unique. Example: jane.doe@acme.com.
   * - ``name``
     - text
     - No
     - The customer's full name or business name. Example: Acme Corporation.
   * - ``phone``
     - text
     - No
     - The customer's phone number, with the country code. Example: +14155550123.
   * - ``description``
     - text
     - No
     - An internal note about the customer, shown in the Stripe Dashboard. Example: Wholesale account, net 30.
   * - ``addressLine1``
     - text
     - No
     - The first line of the customer's address: street and number. Example: 510 Townsend St.
   * - ``addressCity``
     - text
     - No
     - The city of the customer's address. Example: San Francisco.
   * - ``addressState``
     - text
     - No
     - The state, county, province or region of the customer's address. Example: CA.
   * - ``addressPostalCode``
     - text
     - No
     - The ZIP or postal code of the customer's address. Example: 94103.
   * - ``addressCountry``
     - text
     - No
     - The country of the customer's address, as a two-letter ISO code. Example: US.
   * - ``metadata``
     - JSON object
     - No
     - Key-value pairs to store on the customer, such as an id from another system; up to 50 keys, values as text. Example: {"crm\_id": "A-1042"}.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **create** in the **Customer** row. The model sees it as ``stripe_customer_create``. Each call waits for human approval before it changes anything.

Other Customer tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="customer-get.html">Get a customer</a><a href="customer-getmany.html">List customers</a><a href="customer-update.html">Update a customer</a></div>
