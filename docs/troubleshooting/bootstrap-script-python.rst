Bootstrap Script
========

This page lists common errors encountered when working with bootstrap scripts on EMR while using Fire Insights.

1. Facing Issues while Running PySpark workflow on Livy
------
**Problem**
++++++

I see below error:

::

    No Module Named fire

**Solution**
++++++++++

Do check in the logs of EMR If the bootstrap completed successfully and ``fire`` module got installed successfully and do you run workflow before the package got installed.

2. Facing Issues while Running PySpark workflow with pipeline step function
------
**Problem**
++++++

I see below error:

::

    No Module Named fire

**Solution**
++++++++++

Do check in the logs of EMR If the bootstrap completed successfully and ``fire`` module got installed successfully and do you run pipeline step before the package got installed.

3. Facing Issues while Running PySpark workflow on Livy
------
**Problem**
++++++

I see below error:

::

    No Module Named 'requests'

**Solution**
++++++++++

Do check in the logs of EMR If the bootstrap completed successfully and all python dependency successfully got installed.

4. Facing Issues while Running PySpark workflow with pipeline step function
------
**Problem**
++++++

I see below error:

::

    No Module Named 'requests'

**Solution**
++++++++++

Do check in the logs of EMR If the bootstrap completed successfully and all python dependency successfully got installed.
