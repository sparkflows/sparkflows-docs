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
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_subscription_cancel</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Cancels a subscription immediately and returns it with status canceled; billing stops and the subscription cannot be reactivated. Use it only when the customer must lose the plan now, since ending it at the period end is a subscription update this connector does not offer.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.
* The account behind the connection must be allowed to change this data in Stripe.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **cancel** in the **Subscription** row, then click **Add to agent**.

The agent now sees ``stripe_subscription_cancel`` and calls it when a request needs it.

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

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Stripe.

Other Subscription tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="subscription-get.html">Get a subscription</a><a href="subscription-getmany.html">List subscriptions</a></div>
