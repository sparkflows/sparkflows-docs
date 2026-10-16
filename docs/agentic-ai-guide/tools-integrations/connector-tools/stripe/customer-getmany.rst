:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Customer</p>

List customers
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

   Lists customers, newest first, up to 100 in one call. Returns id, email, name, phone, created (Unix seconds) and metadata for each. Use it to find customers by exact email or creation date; for one known id use Customer get.

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
   * - ``email``
     - text
     - No
     - Only the customer whose email is exactly this address; Stripe matches it case-sensitively. Example: jane.doe@acme.com.
   * - ``createdAfter``
     - whole number
     - No
     - Only customers created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only customers created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``limit``
     - whole number
     - No
     - How many customers to return at most; one call returns 100 at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **list** in the **Customer** row. The model sees it as ``stripe_customer_getmany``.

Other Customer tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="customer-get.html">Get a customer</a><a href="customer-create.html">Create a customer</a><a href="customer-update.html">Update a customer</a></div>
