AWS IAM AssumeRole
======
Fire Insights is integrated with AWS IAM Assume Role which can be Configured at Group level.

Advantage
-----
Assuming roles, instead of directly using the user, enforces the principle of least privilege. With roles, you can:

#. Restrict the use of elevated permissions to only those times when they are needed for specific tasks.
#. Explicitly grant the permission to the users to assume the role. Thus, not everyone is allowed to perform those tasks.

.. toctree::
   :maxdepth: 2

   architecture.rst
   assume-role-configuration.rst
   cross-account-iam-role.rst
   fire-configuration.rst
