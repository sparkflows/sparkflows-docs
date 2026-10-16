:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../stripe.html">Stripe</a> › Balance</p>

Get the account balance
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/stripe.svg" alt="Stripe logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Stripe</dd></div>
     <div><dt>Resource</dt><dd>Balance</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>stripe_balance_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the account's current balance: the available and pending amounts per currency, in the currency's smallest unit. Use it to see what can be paid out now; for the movements behind the balance use Balance getMany.

Before you start
----------------

* A Stripe connection. See :doc:`how to set one up <../stripe>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Stripe** under **Connectors** and connect your Stripe connection.
#. Tick **get** in the **Balance** row, then click **Add to agent**.

The agent now sees ``stripe_balance_get`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Other Balance tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="balance-getmany.html">List balance transactions</a></div>
