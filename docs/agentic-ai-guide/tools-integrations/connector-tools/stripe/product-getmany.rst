:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Product</p>

List products
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Product</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists products in the Stripe catalog, newest first, from one Stripe page of up to 100. Returns id, name, description, active, default\_price and metadata for each. Use it to see what is sold; prices are separate Stripe objects and are not listed here.

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
   * - ``active``
     - true or false
     - No
     - true lists only products available for purchase, false only archived ones; blank lists both.
   * - ``createdAfter``
     - whole number
     - No
     - Only products created at or after this moment, as Unix time in seconds. Example: 1788220800.
   * - ``createdBefore``
     - whole number
     - No
     - Only products created at or before this moment, as Unix time in seconds. Example: 1790812800.
   * - ``pageSize``
     - whole number
     - No
     - How many products Stripe returns in its single page, 1 to 100; Stripe's own default is 10, so keep it at or above limit. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many products to return at most, up to 100, since one call reads a single Stripe page. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **list** in the **Product** row. The model sees it as ``stripe_product_getmany``.
