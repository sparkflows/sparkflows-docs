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
     <div><dt>Tool name</dt><dd><code>stripe_charge_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one charge by id and returns its amount and amount\_refunded (in the currency's smallest unit), currency, status, paid, refunded, customer, payment method details, receipt\_url and any failure\_message. Use it to check how a specific payment went; to find charges by customer or date use Charge getMany.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **get** in the **Charge** row, then click **Add to agent**.

The agent now sees ``stripe_charge_get`` and calls it when a request needs it.

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
   * - ``chargeId``
     - text
     - Yes
     - The Stripe charge id, which starts with ch\_ (py\_ for some payment methods); Charge getMany returns it. Example: ch\_3QzT2bLkdIwHu7ix1a2b3c4d.

Other Charge tools
------------------

.. raw:: html

   <div class="tool-related"><a href="charge-getmany.html">List charges</a></div>
