Bootstrap Script
========

This page lists common errors encountered when working with bootstrap scripts on EMR while using Sparkflows.

1. Facing Issues while Running PySpark workflow on Livy
------
**Problem**
++++++

I see below error:

::

    No Module Named 'fire'

**Solution**
++++++++++

Please check the EMR logs to verify the following:

#. Bootstrap Completion: Ensure that the bootstrap process completed successfully.
#. Fire Module Installation: Confirm that the Fire module was installed successfully.
#. Workflow Execution: Verify if the workflow was run before the package was installed.

2. Facing Issues while Running PySpark workflow with pipeline step function
------
**Problem**
++++++

I see below error:

::

    No Module Named 'fire'

**Solution**
++++++++++

Please check the EMR logs to verify the following:

#. Bootstrap Completion: Ensure that the bootstrap process completed successfully.
#. Fire Module Installation: Confirm that the Fire module was installed successfully.
#. Pipeline Execution: Verify if the Pipeline step with PySpark workflow was run before the package was installed.

3. Facing Issues while Running PySpark workflow on Livy
------
**Problem**
++++++

I see below error:

::

    No Module Named 'requests'

**Solution**
++++++++++

Please check the EMR logs to verify the following:

#. Bootstrap Completion: Ensure that the bootstrap process completed successfully.
#. Python Dependencies: Confirm that all Python dependencies were installed successfully.

4. Facing Issues while Running PySpark workflow with pipeline step function
------
**Problem**
++++++

I see below error:

::

    No Module Named 'requests'

**Solution**
++++++++++

Please check the EMR logs to verify the following:

#. Bootstrap Completion: Ensure that the bootstrap process completed successfully.
#. Python Dependencies: Confirm that all Python dependencies were installed successfully.
