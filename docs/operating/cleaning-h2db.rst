Cleaning H2 DB
==============

Fire Insights by default uses the H2 embedded database.

It is important to keep the size of the database in control. All the Fire Insights tables are relatively small except those which store the result of workflow execution.

Cleaning Old Workflow Executions
----------------------

It is important to regularly delete the old workflow executions in order to keep the size of the H2 DB in control.

- Go to the Workflow Executions/List page.
- Click on Delete old Workflow Executions in order to delete the old executions.

