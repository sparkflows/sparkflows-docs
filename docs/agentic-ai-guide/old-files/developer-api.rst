Developer & API
===============

Run any saved agent from your own systems over the Agent REST API - start a run,
poll its status, answer an approval, and read the result.

.. contents:: On this page
   :local:
   :depth: 1


Any agent saved in Sparkflows can be executed from outside the UI through the Agent REST API. All agent endpoints are served under the base path ``/api/v1/agents``.

Pass the Sparkflows access token on every call in the ``token`` header. The token is sent as-is, with no ``Bearer`` prefix.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Header
     - Value
   * - ``token``
     - The access token generated from **Profile & Settings > Generate Access Token**

::

    token: <sparkflows_access_token>

Execute the Agent
-----------------

Start a new agent run.

::

    POST /api/v1/agents/{agentId}/execute

The request body is optional. It is used to pass the runtime inputs the agent expects.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Field
     - Type
     - Description
   * - ``inputs``
     - object
     - Key/value inputs supplied to the agent run, for example the user message or workflow parameters. ``input`` is accepted as an alias.
   * - ``launchedType``
     - string
     - ``MANUAL`` (default) or ``SCHEDULE``. Records how the run was launched.

.. note::

   An agent always runs the graph it was saved with. A ``graph`` sent in the request body is ignored, so that an agent cannot be made to run something other than its saved definition. To change what the agent does, edit and save it in the agent editor.

An example request:

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'token: <sparkflows_access_token>' -d '{"inputs": {"question": "What is the refund policy for enterprise customers?", "customer_id": "C-10932"}}' 'http://hostname:8080/api/v1/agents/118/execute'

An example response:

::

    {
      "runId": "5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21",
      "jobId": "c7d1e3b0-2f45-4a6b-9d18-7e5c2a9f4b30",
      "thread_id": "c7d1e3b0-2f45-4a6b-9d18-7e5c2a9f4b30",
      "execution": {
        "id": 742,
        "agentId": 118,
        "projectId": 33,
        "name": "Customer Support Agent",
        "status": 0,
        "username": "admin",
        "fireJobId": "c7d1e3b0-2f45-4a6b-9d18-7e5c2a9f4b30",
        "runId": "5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21",
        "startTime": 1757059200000
      },
      "fireAgentResponse": {
        "run_id": "5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21",
        "status": "RUNNING"
      }
    }

The values to retain from this response are:

* ``runId`` - used to poll, resume and cancel the run.
* ``execution.id`` - the Sparkflows execution record, used to read the stored results.
* ``jobId`` / ``thread_id`` - the correlation ID for the run and its conversation thread.

The call is asynchronous. It returns as soon as the run has been accepted by the agent engine.

Poll the Run Status
-------------------

::

    GET /api/v1/agents/{agentId}/runs/{runId}/status

An example request:

::

    curl -X GET --header 'Accept: application/json' --header 'token: <sparkflows_access_token>' 'http://hostname:8080/api/v1/agents/118/runs/5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21/status'

An example response:

::

    {
      "run_id": "5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21",
      "status": "completed",
      "outputs": {
        "answer": "Enterprise customers may request a refund within 30 days."
      },
      "node_outputs": { },
      "execution_log": [ ],
      "elapsed_ms": 8420
    }

This endpoint reports the state in lower case. Compare it case-insensitively rather than against an exact string.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Status
     - Code
     - Meaning
   * - ``starting``
     - 4
     - The run has been created and submitted to the agent engine.
   * - ``running``
     - 0
     - The agent is executing.
   * - ``completed``
     - 2
     - The run finished successfully.
   * - ``failed``
     - 3
     - The run ended with an error.
   * - ``stopped``
     - 1
     - The run was cancelled.
   * - ``interrupted``
     - \-
     - The run is paused and waiting for a human decision or input.
   * - ``resuming``
     - 12
     - A resume request has been submitted for a paused run.

The **Code** column is the numeric ``status`` stored on the execution record, which is what the ``/api/v1/agent-executions`` endpoints return.

Resume a Paused Run (Human-in-the-Loop)
---------------------------------------

When the agent contains a Human Approval or Human Input node, the run pauses and reports an interrupted status. The run is continued by posting the decision or the requested input.

::

    POST /api/v1/agents/{agentId}/runs/{runId}/resume

An example approval request:

::

    curl -X POST --header 'Content-Type: application/json' --header 'token: <sparkflows_access_token>' -d '{"decision": "approved", "comments": "Verified against the CRM record"}' 'http://hostname:8080/api/v1/agents/118/runs/5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21/resume'

``decision`` accepts ``approved`` or ``rejected``. For convenience the API also normalizes the equivalent forms sent by integrations, such as ``{"approved": true}`` or ``{"approval_result": {"status": "approved", "comments": "..."}}``.

When the agent is waiting on a Human Input node instead of an approval, the reply is sent as text or values:

::

    -d '{"text": "Ship it to the billing address on file"}'

Cancel a Run
------------

::

    POST /api/v1/agents/{agentId}/runs/{runId}/cancel

An example request:

::

    curl -X POST --header 'Accept: application/json' --header 'token: <sparkflows_access_token>' 'http://hostname:8080/api/v1/agents/118/runs/5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21/cancel'

Read Executions and Results
---------------------------

The execution history and the stored outputs of a run are available through the agent execution APIs.

.. list-table::
   :header-rows: 1
   :widths: 55 45

   * - Endpoint
     - Description
   * - ``GET /api/v1/agent-executions?projectId={projectId}``
     - List agent executions for a project (server-side paginated).
   * - ``GET /api/v1/agent-executions/{id}``
     - Get one execution by its execution ID.
   * - ``GET /api/v1/agent-executions/agent/{agentId}``
     - List all executions of a given agent.
   * - ``GET /api/v1/agent-executions/fire-job/{fireJobId}``
     - Look up an execution by the ``jobId`` returned at launch.
   * - ``GET /api/v1/agent-execution-results/execution/{executionId}``
     - Get the stored results produced by an execution.

Passing Parameters Before a Run
-------------------------------

Agents that reference workflow parameters can have those parameters set before the run is started. This is the same mechanism used by analytic apps.

::

    curl -X POST --header 'Content-Type: application/json' --header 'token: <sparkflows_access_token>' -d '{"startDate": "2026-01-01", "region": "EMEA"}' 'http://hostname:8080/api/v1/agents/updateParameters/118'

Error Handling
--------------

The execute endpoint validates the request before it reaches the agent engine and returns a message that names the problem.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Condition
     - Response
   * - Agent ID does not exist
     - ``Agent not found with id: {agentId}``
   * - Agent has been moved to the trash
     - ``Agent '{name}' is in the trash. Restore it before running it.``
   * - Agent has no saved graph
     - ``Agent '{name}' has no content to run. Open it in the editor and save a graph first.``
   * - Caller lacks EXECUTE permission on the project
     - Access denied
   * - Missing, invalid or expired ``token`` header
     - ``401 Unauthorized``

Errors reported by the agent engine on resume are propagated with the engine's own message, so the cause stays visible to the caller.

Complete Example in Python
--------------------------

The example below triggers an agent, polls until the run completes, approves any human-approval step, and prints the outputs.

::

    #!/usr/bin/python

    import json
    import time

    import requests

    HOST = "http://hostname:8080"
    AGENT_ID = 118

    headers = {
        "token": "<sparkflows_access_token>",
        "Content-Type": "application/json",
    }

    # Step 1 - trigger the agent
    payload = {
        "inputs": {
            "question": "What is the refund policy for enterprise customers?",
            "customer_id": "C-10932",
        }
    }
    run = requests.post(
        "{}/api/v1/agents/{}/execute".format(HOST, AGENT_ID),
        headers=headers,
        data=json.dumps(payload),
        verify=False,
    ).json()

    run_id = run["runId"]
    execution_id = run["execution"]["id"]
    print("Started run {} (execution {})".format(run_id, execution_id))

    # Step 2 - poll until the run reaches a terminal state
    terminal = {"completed", "failed", "stopped"}
    while True:
        status = requests.get(
            "{}/api/v1/agents/{}/runs/{}/status".format(HOST, AGENT_ID, run_id),
            headers=headers,
            verify=False,
        ).json()

        state = str(status.get("status")).lower()
        print("status:", state)

        if state in terminal:
            break

        # Step 3 - approve, if the agent paused on a human approval node
        if state == "interrupted":
            requests.post(
                "{}/api/v1/agents/{}/runs/{}/resume".format(HOST, AGENT_ID, run_id),
                headers=headers,
                data=json.dumps({"decision": "approved"}),
                verify=False,
            )

        time.sleep(3)

    # Step 4 - read the outputs
    print(json.dumps(status.get("outputs"), indent=2))


Next: watch the runs
--------------------

Runs started over the API appear on **Agents → Executions** like any other, with
the same token and step detail - see :doc:`/agentic-ai-guide/monitor-govern`.
