Models & Prompts
=============

Models and prompts define much of an agent's reasoning and generation behavior. Sparkflows allows models to be configured as components within broader workflows, alongside enterprise data processing, retrieval, machine learning, tools, and deterministic business logic.

Different workflow steps may require different model capabilities. Teams can select supported LLM providers and models, configure available parameters, define system instructions, and pass dynamic workflow context into prompts. Where supported, routing or fallback patterns can be used to improve resilience or match tasks to appropriate models.

Sparkflows also enables traditional machine learning models to participate in agentic workflows. A predictive model can score a record, estimate risk or propensity, and pass the result to an agent or workflow rule for downstream reasoning and action.

Start Here
-----------------

Start by configuring the required model connection and validating it independently. Define the agent's system instructions and reusable prompts, then test them with representative context before adding additional tools or workflow complexity.

Keep prompts focused on the model's role while using workflow logic for deterministic transformations, validations, routing, and actions whenever appropriate.

Documentation Topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Models Overview
     - Understand model use across Sparkflows agents and workflows.
   * - LLM Providers
     - Connect supported hosted and enterprise model providers.
   * - Configure & Select Models
     - Set up and choose models for different workflow tasks.
   * - Model Parameters
     - Configure supported generation and runtime settings.
   * - Model Routing & Fallback
     - Route tasks or use alternate models where supported.
   * - Private & Local Models
     - Connect private model endpoints where supported.
   * - Prompt Management Overview
     - Understand prompts and instructions used by agents.
   * - System Instructions
     - Define agent role, behavior, constraints, and objectives.
   * - Create Prompts
     - Create prompts for reusable workflow use.
   * - Prompt Variables
     - Insert dynamic workflow and user context.
   * - Prompt Templates
     - Create reusable prompt structures.
   * - Test & Compare Prompts
     - Evaluate prompts with representative inputs.
   * - Use ML Models in Agents
     - Use predictive models and ML outputs in agentic workflows.
   * - Model Registry & MLflow
     - Manage ML models using supported registry and MLflow capabilities.
   * - Troubleshooting
     - Diagnose prompt, provider, and model configuration issues.
