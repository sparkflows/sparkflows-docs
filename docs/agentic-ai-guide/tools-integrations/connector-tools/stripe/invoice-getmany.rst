:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Invoice</p>

List invoices
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Invoice</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_invoice_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists invoices, newest first, from one Stripe page of up to 100. Returns id, number, customer, status, amount\_due, amount\_paid, currency, due\_date and created for each. Use it to find the open or paid invoices of a customer, a subscription or a period; for one known invoice use Invoice get.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **list** in the **Invoice** row, then click **Add to agent**.

The agent now sees ``stripe_invoice_getmany`` and calls it when a request needs it.

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
   * - ``customer``
     - text
     - No
     - Only invoices of this customer id (cus\_...); Customer getMany returns it. Example: cus\_QzT2bLkdIwHu7i.
   * - ``status``
     - text
     - No
     - Only invoices in this status: open is issued and awaiting payment, uncollectible is written off. One of: draft, open, paid, uncollectible, void.
   * - ``subscription``
     - text
     - No
     - Only invoices of this subscription id (sub\_...); Subscription getMany returns it. Example: sub\_1QzT2bLkdIwHu7ixAbCdEfGh.
   * - ``collectionMethod``
     - text
     - No
     - Only invoices paid automatically from a saved payment method, or only those emailed for the customer to pay. One of: charge\_automatically, send\_invoice.
   * - ``createdAfter``
     - whole number
     - No
     - Only invoices created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only invoices created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``pageSize``
     - whole number
     - No
     - How many invoices Stripe returns in its single page, 1 to 100; Stripe's own default is 10, so keep it at or above limit. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many invoices to return at most, up to 100, since one call reads a single Stripe page. Default: 50.

Other Invoice tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="invoice-get.html">Get an invoice</a></div>
