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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one subscription by id and returns its status, customer, items with their prices, billing period, trial dates, cancel\_at\_period\_end and metadata. Use it when the subscription id (sub\_...) is known; to find subscriptions by customer, price or status use Subscription getMany.

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
   * - ``subscriptionId``
     - text
     - Yes
     - The Stripe subscription id, which starts with sub\_; Subscription getMany returns it. Example: sub\_1QzT2bLkdIwHu7ixAbCdEfGh.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **get** in the **Subscription** row. The model sees it as ``stripe_subscription_get``.

Other Subscription tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="subscription-getmany.html">List subscriptions</a><a href="subscription-cancel.html">Cancel a subscription</a></div>
