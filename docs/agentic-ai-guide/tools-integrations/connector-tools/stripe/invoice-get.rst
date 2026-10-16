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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one invoice by id and returns its number, status, customer, amount\_due, amount\_paid and amount\_remaining (in the currency's smallest unit, such as cents), due\_date, hosted\_invoice\_url and lines. Use it when the invoice id (in\_...) is known; to find invoices by customer, status or date use Invoice getMany.

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
   * - ``invoiceId``
     - text
     - Yes
     - The Stripe invoice id, which starts with in\_; Invoice getMany returns it. Example: in\_1QzT2bLkdIwHu7ixV3pXw9Kd.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **get** in the **Invoice** row. The model sees it as ``stripe_invoice_get``.

Other Invoice tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="invoice-getmany.html">List invoices</a></div>
