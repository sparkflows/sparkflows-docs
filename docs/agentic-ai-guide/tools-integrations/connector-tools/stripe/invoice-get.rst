:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Invoice</p>

Get an invoice
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Invoice</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_invoice_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one invoice by id and returns its number, status, customer, amount\_due, amount\_paid and amount\_remaining (in the currency's smallest unit, such as cents), due\_date, hosted\_invoice\_url and lines. Use it when the invoice id (in\_...) is known; to find invoices by customer, status or date use Invoice getMany.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **get** in the **Invoice** row, then click **Add to agent**.

The agent now sees ``stripe_invoice_get`` and calls it when a request needs it.

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
   * - ``invoiceId``
     - text
     - Yes
     - The Stripe invoice id, which starts with in\_; Invoice getMany returns it. Example: in\_1QzT2bLkdIwHu7ixV3pXw9Kd.

Other Invoice tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="invoice-getmany.html">List invoices</a></div>
