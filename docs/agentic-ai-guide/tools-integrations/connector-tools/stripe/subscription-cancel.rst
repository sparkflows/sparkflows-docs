:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Subscription</p>

Cancel a subscription
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Subscription</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Cancels a subscription immediately and returns it with status canceled; billing stops and the subscription cannot be reactivated. Use it only when the customer must lose the plan now, since ending it at the period end is a subscription update this connector does not offer.

Prerequisites
-------------

* **Connection:** Stripe connection. See :doc:`the Stripe prerequisites <../stripe>`.
* The connection's account must be allowed to change this data in Stripe.

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
   * - ``invoiceNow``
     - true or false
     - No
     - true bills any un-invoiced metered usage and pending proration items in a final invoice now; default false.
   * - ``prorate``
     - true or false
     - No
     - true credits the unused time left in the current period as a proration item; default false.
   * - ``comment``
     - text
     - No
     - Why the subscription is being canceled, kept on the subscription for reference. Example: Customer moved to the annual plan on another account.
   * - ``feedback``
     - text
     - No
     - The reason the customer gave for canceling. One of: customer\_service, low\_quality, missing\_features, other, switched\_service, too\_complex, too\_expensive, unused.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Stripe**, connect, and tick **cancel** in the **Subscription** row. The model sees it as ``stripe_subscription_cancel``. Each call waits for human approval before it changes anything.

Other Subscription tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="subscription-get.html">Get a subscription</a><a href="subscription-getmany.html">List subscriptions</a></div>
