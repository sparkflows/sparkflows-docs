:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Charge</p>

Get a charge
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Charge</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one charge by id and returns its amount and amount\_refunded (in the currency's smallest unit), currency, status, paid, refunded, customer, payment method details, receipt\_url and any failure\_message. Use it to check how a specific payment went; to find charges by customer or date use Charge getMany.

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
   * - ``chargeId``
     - text
     - Yes
     - The Stripe charge id, which starts with ch\_ (py\_ for some payment methods); Charge getMany returns it. Example: ch\_3QzT2bLkdIwHu7ix1a2b3c4d.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **get** in the **Charge** row. The model sees it as ``stripe_charge_get``.

Other Charge tools
------------------

.. raw:: html

   <div class="tool-related"><a href="charge-getmany.html">List charges</a></div>
