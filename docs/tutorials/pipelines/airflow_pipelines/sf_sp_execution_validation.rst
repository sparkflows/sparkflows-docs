Snowflake Stored Procedure Execution & Validation
====
This tutorial demonstrates how to execute and validate a Snowflake stored procedure using Sparkflows and Airflow.
  
Overview
----
This pipeline demonstrates end-to-end orchestration of a Snowflake stored procedure from Sparkflows through Airflow.

1. Executes a Snowflake stored procedure that logs its own run status.
2. Monitors that status table until completion using a Snowflake Sensor.
3. Evaluates the stored procedure’s JSON return value using a Branch Python Operator to decide the next workflow path.

Stored Procedure Definition
++++
**Name: SPARKFLOWSDB.SPFSCHEMA.SP_STORED_PROC**

**Purpose:**

* Insert job metadata as **RUNNING** into SP_STATUS_TABLE.
* Wait for the defined duration (180 seconds = 3 minutes).
* Update the same job record to **SUCCESS** once finished.
* Return a JSON object summarizing execution outcome.

**Stored Procedure**
++++++++++++++++++++++

.. code-block:: sql

  CREATE OR REPLACE PROCEDURE SPARKFLOWSDB.SPFSCHEMA.SP_STORED_PROC(PARAM1 STRING)
  RETURNS VARIANT
  LANGUAGE JAVASCRIPT
  EXECUTE AS CALLER
  AS
  $$
      var job_name = PARAM1;
      var start_time = new Date().toISOString();
  
      try {
          // Insert RUNNING record
          var insert_sql = `
              INSERT INTO SPARKFLOWSDB.SPFSCHEMA.SP_STATUS_TABLE (JOB_NAME, STATUS, START_TIME)
              VALUES ('${job_name}', 'RUNNING', '${start_time}')
          `;
          snowflake.createStatement({ sqlText: insert_sql }).execute();
          snowflake.createStatement({ sqlText: "COMMIT" }).execute();
  
          // Simulated work
          snowflake.createStatement({ sqlText: "SELECT SYSTEM$WAIT(180)" }).execute();
  
          // Mark SUCCESS
          var end_time = new Date().toISOString();
          var update_sql = `
              UPDATE SPARKFLOWSDB.SPFSCHEMA.SP_STATUS_TABLE
              SET STATUS = 'SUCCESS', END_TIME = '${end_time}'
              WHERE JOB_NAME = '${job_name}' AND STATUS = 'RUNNING'
          `;
          snowflake.createStatement({ sqlText: update_sql }).execute();
          snowflake.createStatement({ sqlText: "COMMIT" }).execute();
  
          return {
              "status": "SUCCESS",
              "job_name": job_name,
              "start_time": start_time,
              "end_time": end_time,
              "message": "Job execution completed after 3-minute wait."
          };
      } catch (err) {
          snowflake.createStatement({ sqlText: "ROLLBACK" }).execute();
          return { "status": "FAILED", "job_name": job_name, "error": err.message };
      }
  $$;

**Trigger Command**
++++++++++++++++++++++
     
.. code-block:: sql

    CALL SPARKFLOWSDB.SPFSCHEMA.SP_STORED_PROC('ETL_DAILY_JOB2');



**Airflow / Sparkflows Nodes**
++++++++++++++++++++++++++++++++++

The pipeline uses a sequence of nodes to execute, monitor, and validate the stored procedure.

.. list-table:: 
   :widths: 10 20 20
   :header-rows: 1

   * - Node Name
     - Type
     - Description
   * - Run Snowflake Command
     - SnowflakeStoredProcedureOperator
     - Executes the stored procedure call and pushes the return JSON into XCom.
   * - Snowflake Sensor
     - SnowflakeSensor
     - Periodically queries SP_STATUS_TABLE to confirm job status becomes 'SUCCESS' within timeout.
   * - verify_the_response
     - BranchPythonOperator
     - Pulls the stored-procedure response from XCom and decides the workflow branch.
   * - success_task
     - DummyOperator or downstream step
     - Runs when stored procedure status = SUCCESS.
   * - failure_task
     - DummyOperator or alert step
     - Runs if stored procedure fails or status is missing.



**Branch Operator Logic**
++++++++++++++++++++++++++++
The following logic is used in the BranchPythonOperator to decide the workflow path based on the stored procedure’s JSON output.

.. code-block:: sql

    def branch_func(ti):
    import json
    sp_result = ti.xcom_pull(task_ids='run_snowflake_sp')
    print("Stored Procedure XCom Result:", sp_result)

    # Handle both list/dict XCom shapes
    if isinstance(sp_result, list) and len(sp_result) > 0:
        first_entry = sp_result[0]
        json_str = list(first_entry.values())[0]
        sp_dict = json.loads(json_str)
    elif isinstance(sp_result, dict):
        sp_dict = sp_result
    else:
        print("Unexpected XCom type:", type(sp_result))
        return "failure_task"

    print("Parsed Stored Procedure Result:", sp_dict)

    if sp_dict.get("status") == "SUCCESS":
        print("Job succeeded!")
        return "success_task"
    else:
        print("Job failed or status missing.")
        return "failure_task"


**Execution Flow**
++++++++++++++++++++++++
      
1. **Run Snowflake Command** → starts stored procedure; record set to RUNNING.
2. **Snowflake Sensor** → polls status table every poke_interval seconds until status = SUCCESS.
3. **verify_the_response** → reads the JSON output from XCom and evaluates status.
4. **Branches:**
      
    * SUCCESS → success_task
    * FAILED/MISSING → failure_task


   .. figure:: ../../../_assets/tutorials/pipeline/pipeline-snowflake-sp.png
      :alt: pipeline-tutorials
      :width: 70%



**Pipeline JSON File**
+++++++++++++++++++++++++

**File Name:** ``SnowflakeSP.json``













