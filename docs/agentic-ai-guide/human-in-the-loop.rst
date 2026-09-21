Human-in-the-Loop
=================

Some decisions should not be automatic. Human-in-the-loop nodes let an agentic
workflow **pause**, put a real decision in front of a real person, and then
carry on down a different path depending on what they chose.

Sparkflows gives you two nodes for this, both in the **Control** group:

.. list-table::
   :header-rows: 1
   :widths: 22 20 58

   * - Node
     - Anchors
     - Use it when
   * - **Human Approval**
     - **A** / **R**
     - A person must approve or reject before the run continues.
   * - **Human Input**
     - single
     - The run needs the person to *say something* before it can continue.

.. contents:: On this page
   :local:
   :depth: 1

Human Approval
--------------

The Human Approval node is a gate. When a run reaches it, the run **stops** and
waits — it shows as **Interrupted** and nothing further happens until a person
answers. When somebody approves or rejects, the run picks up where it left off
and continues down either the **Approved (A)** or the **Rejected (R)** branch.

.. important::

   **Both anchors should be wired.** A rejected run whose R branch leads nowhere
   simply stops, and nobody is told why.

The shape of an approval flow
-----------------------------

An approval gate is only useful if the decision in front of it is already made.
The pattern that works has three parts:

#. **Do the analysis first**, while nobody is waiting.
#. **Branch on risk** with a :doc:`Condition </agentic-ai-guide/control-flow>`,
   so only the cases that need a human reach the gate.
#. **Gate only that branch.**

.. figure:: ../_assets/agentic-ai-guide/hitl/po-approver-canvas.png
   :alt: The Purchase Order Approver canvas, where a Condition routes high-value orders to a Human Approval gate
   :width: 95%

   The **Purchase Order Approver** example. Two Agent Nodes validate the PO and
   its vendor, a Condition checks the amount, and only high-value orders stop at
   the approval gate before posting to the ERP.

.. caution::

   Do not put an approval gate in front of everything. An approval that fires on
   every run is a queue, not a control — people start approving without reading,
   and you have added latency while removing nothing. Gate the exceptions.

Adding the node
---------------

#. Open your agent on the **Agent Orchestration** canvas.
#. In the **Nodes** palette, open the **Control** group.
#. Drag **Human Approval** onto the canvas.

   .. figure:: ../_assets/agentic-ai-guide/hitl/palette-control.png
      :alt: The Control group of the node palette, containing Human Approval and Human Input
      :width: 300px

#. Connect the branch that needs sign-off into its input.
#. Wire both outputs:

   .. list-table::
      :header-rows: 1
      :widths: 20 80

      * - Anchor
        - Wire it to
      * - **Approved (A)**
        - The action that should only happen after sign-off — send the email,
          place the order, post the transaction.
      * - **Rejected (R)**
        - The fallback — log the decision, notify the requester, or route to an
          edit/retry step.

   .. figure:: ../_assets/agentic-ai-guide/hitl/approval-anchors.png
      :alt: Human Approval node showing the A and R output anchors
      :width: 290px

Configuration
-------------

Double-click the node.

.. figure:: ../_assets/agentic-ai-guide/hitl/approval-config.png
   :alt: Human Approval configuration dialog with Title and Prompt to Approver
   :width: 85%

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - What to put in it
   * - **Title** *(required)*
     - Short heading shown to the approver when the run stops. Keep it
       action-oriented — ``Approve purchase order``, ``Confirm customer
       refund``.
   * - **Prompt to Approver**
     - The longer message. Explain what the upstream node produced and exactly
       what decision is being asked for. Reference the values the reviewer needs
       — an amount, a draft, a validator's assessment — so the person can decide
       without leaving the screen.

Show the agent's own answer in the prompt
-----------------------------------------

The prompt is not just static text. Write ``${<node number>.<field>}`` and
Sparkflows substitutes that node's output before the reviewer sees it — so the
approver reads the agent's actual words, not a description of them.

The node number is the one in the blue circle on the canvas, and ``analysis`` is
the node's answer:

.. code-block:: text

   The Refund Reviewer said: ${2.analysis}

   Approve to issue the refund, or reject to send it back to the queue.

At run time that becomes:

.. figure:: ../_assets/agentic-ai-guide/hitl/approval-pending.png
   :alt: The approval prompt with the agent's answer substituted into it, above the comment boxes and the Approve and Reject buttons
   :width: 100%

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Reference
     - What it pulls in
   * - ``${2.analysis}``
     - Node 2's answer — the usual one.
   * - ``${2.confidence}``
     - Any other field that node published.
   * - ``${order_id}``
     - A value from the Input node, by name.

.. tip::

   Put the value the decision turns on directly in the prompt. A reviewer who
   has to go hunting for the amount will stop reading it and start clicking
   **Approve**.

.. note::

   The same ``${...}`` references work on the REST API Client, MCP Tool and
   Workflow Execution nodes. A reference that matches nothing is left in place
   as literal text, which is your clue that the node number or field name is
   wrong.

Writing the approver prompt
---------------------------

This field is the whole control. A reviewer who does not understand what they
are approving will approve everything.

A good prompt answers three questions. The Purchase Order Approver example
answers all three:

   *This purchase order is at or above the $10,000 manager-approval threshold.
   Review the vendor validation summary and approve or reject. Approval lets the
   run post the PO to D365; rejection cancels the run without touching the ERP.*

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - The question
     - How that example answers it
   * - **Why am I seeing this?**
     - "at or above the $10,000 manager-approval threshold"
   * - **What should I check?**
     - "Review the vendor validation summary"
   * - **What happens next?**
     - "Approval lets the run post the PO to D365; rejection cancels the run
       without touching the ERP"

.. tip::

   Name the **system that will be changed**, as that example names D365. The
   difference between "approve this" and "approve posting this to D365" is the
   difference between a rubber stamp and a decision.

What the reviewer actually does
-------------------------------

An approval is answered from the **run**, not from the builder. This is the
whole flow, from the reviewer's side.

**Step 1 — Find the waiting run.** On **Agents → Executions**, a run sitting at
a gate shows the status **Interrupted**. It stays there until somebody answers
it, and it survives a restart.

.. figure:: ../_assets/agentic-ai-guide/hitl/executions-interrupted.png
   :alt: The Executions tab with two runs showing the Interrupted status
   :width: 100%

**Step 2 — Open it.** An Interrupted row has three actions. The middle one is
**Resume Paused Run** *(boxed above)* — on a finished run the same position says
**Rerun** instead, so the icon tells you whether a run is waiting for you.
Either **Resume Paused Run** or **View Execution** takes you to the same place.

The run opens with an **approval panel** at the top, carrying the node's title,
the prompt you wrote, and two boxes — one for comments that travel with an
approval, one for the reason that travels with a rejection.

Everything the reviewer needs to judge is on the same page: scroll down and the
**Node Outputs** panel shows what each earlier step produced, including the
agent's own recommendation.

**Step 3 — Answer it.** Type a comment or a reason, then click **Approve** or
**Reject**. The run resumes immediately from where it stopped — it does not
start again — and continues down the **Approved (A)** or **Rejected (R)**
branch.

**Step 4 — The decision is part of the record.** The approval step keeps the
outcome and the comment, so months later the run still says who decided what,
and why.

.. figure:: ../_assets/agentic-ai-guide/hitl/approval-approved.png
   :alt: The approval step in a finished run, showing the approved status and the reviewer comment
   :width: 900px

.. note::

   Approvals are answered in the run view, not in a
   :doc:`chat assistant </agentic-ai-guide/chat>`. Send reviewers to
   **Agents → Executions**, or tell them a run is waiting with an
   :doc:`Email Notification </agentic-ai-guide/node-reference>` node. **Human
   Input** is the node for asking the person something mid-conversation.

What waiting actually means
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Behaviour
     - What to expect
   * - **Waiting**
     - The run stops at the node and shows as **Interrupted** on the Executions
       tab. It uses nothing while it waits.
   * - **How long**
     - Indefinitely. A waiting approval survives a restart of Sparkflows, so
       nothing is lost if the server is bounced overnight.
   * - **Resuming**
     - The run continues from the node it stopped at. Earlier steps are not
       repeated, so nothing is charged or sent twice.
   * - **Who can answer**
     - Anyone who can open the run. Approval is not routed to a named person —
       if that matters, tell the right person with an
       :doc:`Email Notification </agentic-ai-guide/node-reference>`.

Skipping the gate while you test
--------------------------------

Waiting for yourself to click **Approve** gets tedious while you are still
building. Add a parameter named ``auto_approve`` with the value ``true`` on the
**Input** node and every gate in that run approves itself, so the flow runs
straight through.

.. caution::

   Remove it before anyone else uses the agent. An agent with ``auto_approve``
   set looks exactly like one with a working gate, right up until the moment it
   matters.

Deciding what needs approval
----------------------------

Put a Condition before the gate and branch on an explicit expression:

.. code-block:: python

   amount >= 10000

Thresholds that work in practice:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Domain
     - A rule worth gating on
   * - Procurement
     - Order value above a monetary threshold
   * - Customer service
     - Refunds above an amount, or any goodwill credit
   * - HR
     - Any rejection, or any offer outside the approved band
   * - Legal
     - Any clause the review flagged as non-standard
   * - Finance
     - Anything scored as high risk, or any new payee

Worked examples
---------------

**Purchase order over threshold.** A validator flags a PO above the auto-approval
limit. Title: *Approve high-value purchase order*. On approve, execution flows
down A to the "place order" step; on reject, down R to "notify requester".

**Approve an AI-drafted email.** An Agent Node drafts customer outreach. Title:
*Send this outreach email?*

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Decision
     - Anchor taken
     - Downstream action
   * - Approve
     - Approved (A)
     - An Email Notification node sends the draft
   * - Reject
     - Rejected (R)
     - Routes back to the Agent to redraft

That second pattern — reject loops back to redraft — is worth copying. It turns
a rejection into an improvement rather than a dead end.

Human Input
-----------

**Human Input** is the conversational pause. It parks the run, shows the person
whatever the upstream step emitted as its response message, and captures the raw
reply into ``user_input``.

.. note::

   Human Input **carries no configuration at all** and does no interpretation.
   It does not extract fields, validate, or decide business actions.
   Understanding the reply — a part request, a yes/no, a selection, a
   confirmation — is the **agent's job on the next turn**.

So the quality of a Human Input step is decided by the node that speaks *before*
it and the agent that reads the answer *after* it. Make the upstream message say
exactly what is needed and in what form, and give the downstream agent explicit
instructions for interpreting the reply.

It also pairs naturally with a blocked Guardrails check: wire **Blocked (B)**
back to a Human Input node and the person gets to revise and retry.

Checklist before you ship an approval flow
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 8 92

   * - ✓
     - Check
   * - ☐
     - The analysis happens **before** the gate.
   * - ☐
     - A Condition limits the gate to cases that genuinely need it.
   * - ☐
     - The **Title** is scannable in a list of twenty.
   * - ☐
     - The prompt says why, what to check, and what each choice causes.
   * - ☐
     - The **R** branch leads somewhere that tells someone.
   * - ☐
     - ``auto_approve`` is **not** left switched on.
   * - ☐
     - You have run it once as the reviewer and read your own prompt cold.

Next: approvals in production
-----------------------------

:doc:`/agentic-ai-guide/control-flow` covers the Condition and Router nodes that
decide which cases reach your gate.
