:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Subscription</p>

Get a subscription
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Subscription</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_subscription_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one subscription by id and returns its status, customer, items with their prices, billing period, trial dates, cancel\_at\_period\_end and metadata. Use it when the subscription id (sub\_...) is known; to find subscriptions by customer, price or status use Subscription getMany.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **get** in the **Subscription** row, then click **Add to agent**.

The agent now sees ``stripe_subscription_get`` and calls it when a request needs it.

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
   * - ``subscriptionId``
     - text
     - Yes
     - The Stripe subscription id, which starts with sub\_; Subscription getMany returns it. Example: sub\_1QzT2bLkdIwHu7ixAbCdEfGh.

Other Subscription tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="subscription-getmany.html">List subscriptions</a><a href="subscription-cancel.html">Cancel a subscription</a></div>
