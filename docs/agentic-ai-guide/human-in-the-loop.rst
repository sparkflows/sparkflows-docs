Human-in-the-Loop
=================

Human-in-the-loop (HITL) controls allow an agentic workflow to pause for human review, approval, correction, or additional input before continuing. This is useful when an automated decision has financial, operational, regulatory, or customer impact that requires human judgment.

In Sparkflows, human decision points can be incorporated into the workflow rather than managed outside the process. The agent can perform the initial analysis, prepare the relevant context or recommendation, and route the case to a reviewer. The workflow can then continue based on the human decision.

HITL is not limited to simple approve/reject steps. It can also support exception handling, escalation, additional information requests, and workflows where only selected high-risk cases require manual review.

Steps to Add Human-in-the-Loop
------------------------------

Add human oversight to an agentic workflow by working through the following steps.

Step 1: Identify Human Decision Points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify the decisions that genuinely require human judgment within the workflow.

Step 2: Add Approval or Review Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add approval or review points where the workflow should pause for human input.

Step 3: Prepare Reviewer Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define and provide the information the reviewer needs to understand and evaluate the case.

Step 4: Configure Review Outcomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify what should happen when the reviewer approves, rejects, escalates, or provides additional input.

Step 5: Configure Conditional Approval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Require human approval only for selected cases, such as sensitive or high-risk scenarios.

Step 6: Configure Escalation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Route sensitive or exceptional cases to the appropriate reviewer.

Step 7: Request Additional Input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allow users or reviewers to provide additional information required for the workflow to continue.

Step 8: Resume Workflow Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continue workflow execution based on the human decision or input.

Step 9: Handle Timeouts & Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define behavior when a review is not completed or an exception occurs, where supported.

Step 10: Review Approval History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Review human decisions made during workflow execution.

Step 11: Add HITL to Agentic Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use Agentic App Builder to provide controlled review and approval experiences for users.

Next Step
---------

Once human decision points have been configured and tested, continue to Evaluate to validate approvals, escalations, and workflow behavior.
