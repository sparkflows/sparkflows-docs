:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Customer</p>

Get a customer
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Customer</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_customer_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one Stripe customer by id and returns its email, name, phone, address, description, balance, currency and metadata. Use it when the customer id (cus\_...) is known; to find customers by email or creation date use Customer getMany.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **get** in the **Customer** row, then click **Add to agent**.

The agent now sees ``stripe_customer_get`` and calls it when a request needs it.

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
     - The Stripe customer id, which starts with cus\_; Customer getMany and the customer field of invoices, charges and subscriptions return it. Example: cus\_QzT2bLkdIwHu7i.

Other Customer tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="customer-getmany.html">List customers</a><a href="customer-create.html">Create a customer</a><a href="customer-update.html">Update a customer</a></div>
