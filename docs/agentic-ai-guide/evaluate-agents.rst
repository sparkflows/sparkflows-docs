Evaluate
===========
After building an agent, evaluate its behavior using representative inputs, business scenarios, and repeatable test cases. Evaluation helps determine not only whether a workflow executes successfully, but whether the agent produces useful, grounded, and appropriate results for the intended task.

A technically successful run can still produce an incomplete answer, select an inappropriate tool, retrieve irrelevant context, or return an output that does not satisfy business requirements. Sparkflows evaluation should therefore combine execution inspection with response review, tool and retrieval analysis, and supported quality metrics.

Evaluation is also iterative. Teams can refine prompts, models, tools, retrieval settings, and workflow logic, then compare the resulting behavior before approving an agent for production.

Start here
----------------
Start by testing the agent interactively with representative inputs. Review the execution trace, tool calls, retrieved context, intermediate workflow outputs, and final response. For important use cases, create repeatable evaluation datasets or test scenarios so changes can be compared consistently.

Once the agent meets the expected functional and business criteria, proceed to Deploy. Where guardrails or human approvals are required, validate those controls as part of evaluation rather than waiting until production.

Documentation Topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Evaluation Overview
     - Understand how Sparkflows can be used to validate agent behavior before production.
   * - Interactive Testing
     - Run an agent with representative questions and inputs.
   * - Chat with Agents
     - Test conversational behavior and actions interactively.
   * - Workflow Testing
     - Test complete workflows and individual stages.
   * - Test Cases
     - Create repeatable scenarios for agent validation.
   * - Evaluation Datasets
     - Evaluate agents against representative datasets and questions.
   * - Evaluation Criteria & Metrics
     - Use supported criteria and metrics to assess agent outputs.
   * - Compare Runs
     - Compare outputs across prompts, models, tools, or workflow configurations.
   * - Trace Analysis
     - Inspect the execution steps taken by an agent.
   * - Tool Execution Review
     - Review selected tools, their inputs, and returned results.
   * - RAG Evaluation
     - Inspect retrieved context and validate grounded responses.
   * - Regression Testing
     - Re-test important scenarios after agent changes.
   * - Guardrail Testing
     - Validate behavior against configured controls.
   * - Human Review
     - Include reviewer feedback where business judgment is required.
   * - Evaluation Results
     - Review and interpret evaluation outcomes.
   * - Troubleshooting
     - Diagnose testing, tracing, and evaluation issues.



