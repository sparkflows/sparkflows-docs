Developer & API
===============

Sparkflows is designed to support visual development while still allowing developers to extend the platform when a use case requires custom logic or integration. APIs, code processors, and custom components can complement visual workflows rather than replacing them.

Developers can use programmatic interfaces to trigger workflows, integrate deployed agents with external applications, build custom processors or tools, and add Python, SQL, or JavaScript logic where supported.

Developer documentation should clearly separate stable public APIs from internal implementation details and provide authentication, request/response, error handling, and working examples for supported extension points.

Steps to Extend Sparkflows
--------------------------

Extend Sparkflows using APIs, code, and custom components by working through the following steps.

Step 1: Identify the Extension Requirement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify the integration, custom logic, or development requirement that cannot be addressed through the visual workflow alone.

Step 2: Select the Extension Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose the appropriate API, code processor, custom processor, custom tool, or other supported extension point.

Step 3: Configure API Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the authentication required for applications calling Sparkflows APIs.

Step 4: Invoke Agents & Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use supported APIs to invoke deployed agents and workflows programmatically where exposed.

Step 5: Add Custom Code
~~~~~~~~~~~~~~~~~~~~~~~

Extend workflows with Python, SQL, or JavaScript where supported.

Step 6: Build Custom Processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create reusable organization-specific processors for custom workflow logic.

Step 7: Create Custom Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create agent tools for proprietary systems and capabilities.

Step 8: Integrate External APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect third-party and internal services through supported interfaces.

Step 9: Configure Webhooks & Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Integrate workflows with events where supported.

Step 10: Define Request & Response Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use supported API payload structures and handle request and response data appropriately.

Step 11: Handle Errors
~~~~~~~~~~~~~~~~~~~~~

Implement appropriate handling for API and runtime errors.

Step 12: Test & Troubleshoot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate the extension with minimal requests or workflows and diagnose API, code, and extension issues.

Next Step
---------

Once the required APIs, code, or custom components have been tested, integrate them into the broader agent or workflow and continue to Evaluate to validate the resulting behavior.

Triggering an Agent from the REST API
-------------------------------------

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
~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~

::

    GET /api/v1/agents/{agentId}/runs/{runId}/status

An example request:

::

    curl -X GET --header 'Accept: application/json' --header 'token: <sparkflows_access_token>' 'http://hostname:8080/api/v1/agents/118/runs/5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21/status'

An example response:

::

    {
      "run_id": "5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21",
      "status": "COMPLETED",
      "outputs": {
        "answer": "Enterprise customers may request a refund within 30 days."
      },
      "node_outputs": { },
      "execution_log": [ ],
      "elapsed_ms": 8420
    }

The execution status recorded in Sparkflows uses the following codes.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Code
     - Status
     - Meaning
   * - 4
     - STARTING
     - The run has been created and submitted to the agent engine.
   * - 0
     - RUNNING
     - The agent is executing.
   * - 2
     - COMPLETED
     - The run finished successfully.
   * - 3
     - FAILED
     - The run ended with an error.
   * - 1
     - STOPPED
     - The run was cancelled.
   * - \-
     - INTERRUPTED
     - The run is paused and waiting for a human decision or input.
   * - 12
     - RESUMING
     - A resume request has been submitted for a paused run.

Resume a Paused Run (Human-in-the-Loop)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~

::

    POST /api/v1/agents/{agentId}/runs/{runId}/cancel

An example request:

::

    curl -X POST --header 'Accept: application/json' --header 'token: <sparkflows_access_token>' 'http://hostname:8080/api/v1/agents/118/runs/5f2a9c1e-88b4-42d7-9c33-6a1b0d4f7e21/cancel'

Read Executions and Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agents that reference workflow parameters can have those parameters set before the run is started. This is the same mechanism used by analytic apps.

::

    curl -X POST --header 'Content-Type: application/json' --header 'token: <sparkflows_access_token>' -d '{"startDate": "2026-01-01", "region": "EMEA"}' 'http://hostname:8080/api/v1/agents/updateParameters/118'

Error Handling
~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    terminal = {"COMPLETED", "FAILED", "STOPPED"}
    while True:
        status = requests.get(
            "{}/api/v1/agents/{}/runs/{}/status".format(HOST, AGENT_ID, run_id),
            headers=headers,
            verify=False,
        ).json()

        state = status.get("status")
        print("status:", state)

        if state in terminal:
            break

        # Step 3 - approve, if the agent paused on a human approval node
        if state == "INTERRUPTED":
            requests.post(
                "{}/api/v1/agents/{}/runs/{}/resume".format(HOST, AGENT_ID, run_id),
                headers=headers,
                data=json.dumps({"decision": "approved"}),
                verify=False,
            )

        time.sleep(3)

    # Step 4 - read the outputs
    print(json.dumps(status.get("outputs"), indent=2))


Next Step
---------

Once the required APIs, code, or custom components have been tested, integrate them into the broader agent or workflow and continue to Evaluate to validate the resulting behavior.
