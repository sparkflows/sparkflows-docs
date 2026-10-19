:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Customer</p>

Update a customer
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Customer</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_customer_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes fields on an existing Stripe customer and returns the updated customer; fields left out stay as they are. Use it to correct contact details or add metadata; to add a new customer use Customer create.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.
* The account behind the connection must be allowed to change this data in Stripe.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **update** in the **Customer** row, then click **Add to agent**.

The agent now sees ``stripe_customer_update`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``customerId``
     - text
     - Yes
     - The Stripe customer id, which starts with cus\_; Customer getMany returns it. Example: cus\_QzT2bLkdIwHu7i.
   * - ``email``
     - text
     - No
     - The customer's new email address. Example: jane.doe@acme.com.
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
     - An internal note about the customer, shown in the Stripe Dashboard. Example: Moved to annual billing.
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
     - Key-value pairs to add or change on the customer; a key sent with an empty value is removed. Example: {"crm\_id": "A-1042"}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Stripe.

Other Customer tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="customer-get.html">Get a customer</a><a href="customer-getmany.html">List customers</a><a href="customer-create.html">Create a customer</a></div>
