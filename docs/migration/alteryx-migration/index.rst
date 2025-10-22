Alteryx to Sparkflows
====
The Alteryx to Sparkflows Migration feature provides a simple and direct way to **import existing Alteryx Designer workflows (.yxmd) into Sparkflows**. After upload, the file is automatically converted into a native Sparkflows workflow that can be executed immediately once the corresponding datasets are provided.
This allows teams to continue their existing analytics processes in Sparkflows without rebuilding workflows from scratch.

Purpose
----
This feature is intended for users who want to modernize their workflows and operate within an open, scalable environment while retaining control of their data and logic.

Key Benefits
++++

**1. Preserve Workflow Structure**: Automatically converts and maintains node connectivity, parameters, and logic from the original Alteryx workflow.

**2. Rapid Validation**: Quickly test migrated workflows by running them directly within Sparkflows, without additional setup or re-configuration.

**3. Flexible Deployment**: Run locally on a laptop or PC for validation, then scale to enterprise or cloud environments without modification.

**4. Reduced Re-engineering Effort**: Significantly decreases the manual work required to recreate complex workflows.

**5. Freedom and Portability**: Helps organizations avoid vendor lock-in by moving to an open, Spark-based platform where workflows can be customized, extended, and maintained independently.


.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`/migration/alteryx-migration/migration-process`

    Step-by-Step Guide to Migrating Alteryx Workflows to Sparkflows


.. toctree::
   :hidden:

   migration-process.rst
