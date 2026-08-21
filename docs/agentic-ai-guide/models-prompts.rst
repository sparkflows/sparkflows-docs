Models & Prompts
================

Models and prompts define much of an agent's reasoning and generation behavior. Sparkflows allows models to be configured as components within broader workflows, alongside enterprise data processing, retrieval, machine learning, tools, and deterministic business logic.

Different workflow steps may require different model capabilities. Teams can select supported LLM providers and models, configure available parameters, define system instructions, and pass dynamic workflow context into prompts. Where supported, routing or fallback patterns can be used to improve resilience or match tasks to appropriate models.

Sparkflows also enables traditional machine learning models to participate in agentic workflows. A predictive model can score a record, estimate risk or propensity, and pass the result to an agent or workflow rule for downstream reasoning and action.

Steps to Configure Models & Prompts
------------------------------------

Configure models and prompts by working through the following steps.

Step 1: Connect a Model Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the required model connection and validate it independently.

Step 2: Select the Model
~~~~~~~~~~~~~~~~~~~~~~~~~

Select the supported LLM provider and model appropriate for the workflow task.

Step 3: Configure Model Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the available generation and runtime parameters for the selected model.

Step 4: Define System Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define the agent's role, behavior, constraints, and objectives through system instructions.

Step 5: Create Prompts
~~~~~~~~~~~~~~~~~~~~~~

Create reusable prompts for the workflow and define how the model should process the required task.

Step 6: Add Dynamic Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pass dynamic workflow and user context into prompts using supported prompt variables.

Step 7: Test & Compare Prompts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test prompts with representative inputs and compare results to refine the agent's behavior.

Step 8: Configure Model Routing & Fallback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use routing or fallback patterns where supported to match tasks to appropriate models or improve resilience.

Step 9: Add ML Models to Agentic Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use predictive models and ML outputs within agentic workflows for downstream reasoning and action.

Step 10: Manage ML Models
~~~~~~~~~~~~~~~~~~~~~~~~~

Manage ML models using supported model registry and MLflow capabilities.

Next Step
---------

Once models and prompts are configured and validated, continue to build the agentic workflow by connecting the required data, knowledge, tools, and business logic.
