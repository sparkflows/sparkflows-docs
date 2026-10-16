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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one Stripe customer by id and returns its email, name, phone, address, description, balance, currency and metadata. Use it when the customer id (cus\_...) is known; to find customers by email or creation date use Customer getMany.

Prerequisites
-------------

* **Connection:** Stripe connection. See :doc:`the Stripe prerequisites <../stripe>`.

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
   * - ``customerId``
     - text
     - Yes
     - The Stripe customer id, which starts with cus\_; Customer getMany and the customer field of invoices, charges and subscriptions return it. Example: cus\_QzT2bLkdIwHu7i.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **get** in the **Customer** row. The model sees it as ``stripe_customer_get``.

Other Customer tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="customer-getmany.html">List customers</a><a href="customer-create.html">Create a customer</a><a href="customer-update.html">Update a customer</a></div>
