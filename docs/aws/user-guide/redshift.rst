Integration with Redshift
========================

Fire is fully integrated with Redshift. Fire has a number of processors specifically for Redshift.

Read from Redshift and Write to Redshift
------

ReadJDBC and WriteJDBC nodes can be used for reading from and writing to Redshift. 

`Click here for more details on Using Redshift Node using JDBC <https://docs.sparkflows.io/en/latest/user-guide/connectors/jdbc.html>`_

`Click here for more details on Creating Redshift Connection <https://docs.sparkflows.io/en/latest/installation/connection/storage-connection/redshift.html>`_

NodeExecuteRedShiftStmt
------

NodeExecuteRedShiftStmt Node submit the SQL statement for execution on the Redshift cluster.

#. Cluster Identifier (clusterIdentifier): Identifies the Redshift cluster to connect to.
#. Database User (dbUser): The user executing the SQL statement.
#. Database (database): The Redshift database to run the query against.
#. SQL Statement (sqlStatement): The actual SQL query.

Example statement:
++++++++

#. Data Manipulation

   :: 

        INSERT INTO orders (order_id, product_id, quantity) VALUES (101, 1, 2);
        UPDATE orders SET quantity = 5 WHERE order_id = 101;
        DELETE FROM orders WHERE order_id = 101; 

   .. Note:: It Performs "INSERT, UPDATE, or DELETE" operations on the orders table.

#. DDL (Data Definition Language)

   ::

        CREATE TABLE employees (
        emp_id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(30),
        salary DECIMAL(10, 2)
        );
        DROP TABLE employees;
        ALTER TABLE employees ADD COLUMN hire_date DATE;

   .. Note:: It "Creates, drops, or alters" tables and their structure.

#. Attach the below policy to your Amazon EMR cluster IAm role

   ::

        {
            "Effect": "Allow",
            "Action": [
                "redshift:ExecuteStatement",
                "redshift:DescribeStatement",
                "redshift:GetStatementResult"
            ],
            "Resource": "*"
       }

.. Note:: 1. It will not run in Interactive mode, only work on Execution. 
          2. Job submitted to EMR should have required permission to execute that.
