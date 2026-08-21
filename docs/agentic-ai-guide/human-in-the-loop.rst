Human-in-the-Loop
=============

Human-in-the-loop (HITL) controls allow an agentic workflow to pause for human review, approval, correction, or additional input before continuing. This is useful when an automated decision has financial, operational, regulatory, or customer impact that requires human judgment.

In Sparkflows, human decision points can be incorporated into the workflow rather than managed outside the process. The agent can perform the initial analysis, prepare the relevant context or recommendation, and route the case to a reviewer. The workflow can then continue based on the human decision.

HITL is not limited to simple approve/reject steps. It can also support exception handling, escalation, additional information requests, and workflows where only selected high-risk cases require manual review.

Start here
-----------------

Start by identifying the decisions that genuinely require human judgment. Add approval or review only at those points, define the information the reviewer needs, and specify what should happen for approval, rejection, escalation, or missing input.

For user-facing review experiences, combine HITL workflows with Agentic App Builder so reviewers can see the relevant context and take action in a controlled interface.

Documentation topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - HITL Overview
     - Understand human oversight within agent workflows.
   * - Add Approval Steps
     - Pause execution for human approval.
   * - Review Agent Output
     - Allow a reviewer to inspect generated results.
   * - Approve or Reject
     - Capture a decision before workflow continuation.
   * - Request Additional Input
     - Collect information from a user or reviewer.
   * - Conditional Approval
     - Require approval only for selected cases.
   * - Escalation
     - Route sensitive or exceptional cases to reviewers.
   * - Reviewer Assignment
     - Direct tasks to appropriate reviewers where supported.
   * - Resume Execution
     - Continue workflow execution after human input.
   * - Timeout & Exception Handling
     - Define behavior when review is not completed where supported.
   * - Approval History
     - Review human decisions made during execution.
   * - HITL in Agentic Apps
     - Embed review and approval experiences in applications.
   * - Troubleshooting
     - Diagnose approval, routing, and resume issues.
