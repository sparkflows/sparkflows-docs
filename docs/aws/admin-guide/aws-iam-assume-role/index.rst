AWS IAM ASSUME ROLE
======

Fire Insights Integrated with AWS IAM Assume Role, which can be Configured at Group level.

Advantage
-----

Assuming roles instead of directly using the user enforces the principle of least privilege. With roles, you can

1. Restrict the use of elevated permissions to only those times when they are needed for specific tasks.
2. Explicitly grant your users permission to assume the role. This way, not everyone is allowed to perform those tasks.

.. toctree::
   :maxdepth: 2

   architecture.rst
   assume-role-configuration.rst
   fire-configuration.rst
