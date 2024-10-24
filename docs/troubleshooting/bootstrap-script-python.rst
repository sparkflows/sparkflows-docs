Bootstrap Script
========

This page lists common errors when working with Boostrap script on emr while using in Fire Insights.

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

