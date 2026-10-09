.. rst-class:: agentic-tutorial

Document Summarization Agent
============================

.. container:: tutorial-intro

   This example shows a single agent that reads three separate reports - sales,
   support and operations - and combines them into one cross-source summary.
   One Agent Node does the work, using three ``Read CSV`` tools.

.. container:: tutorial-start

   **What this example shows:** how one agent can pull from several data
   sources and return one consolidated answer. The result has a **Sales**, a
   **Support** and an **Operations** section, built from all three reports.

How the agent is built
----------------------

The agent is built on the **Agent Orchestration** canvas and is named
**02-Document-Summarization-Agent**. It has two nodes:

**Input → Agent Node**

The Input node feeds the Agent Node, and three ``Read CSV`` tools are attached
to the Agent Node. These are tools, not steps: the model decides when to call
each one.

.. figure:: ../../_assets/agentic-ai-guide/tutorials/document-summarization/canvas.png
   :alt: Canvas with an Input node wired to an Agent Node that has three Read CSV tools attached
   :width: 900px

   The Input node feeds the Agent Node. The three **Read CSV** chips under the
   Agent Node are its tools; the **3** badge shows how many are attached.

The request
-----------

The **Input** node passes the request to the agent as one parameter:

* **Key:** ``userQuery``
* **Value:** ``provide a summary for sales, support and operations``

The value can be changed each time the agent runs.

One tool per report
-------------------

Each ``Read CSV`` tool reads one report:

.. list-table:: Read CSV tools
   :header-rows: 1
   :widths: 22 42 36

   * - Tool
     - File
     - Description
   * - ``read_csv``
     - ``data/AgenticAI-Training/02_1_sales_report.csv``
     - ``Reads the August sales report``
   * - ``read_csv_2``
     - ``data/AgenticAI-Training/02_2_support_report.csv``
     - ``Reads the August support report``
   * - ``read_csv_3``
     - ``data/AgenticAI-Training/03_3_operations_update.csv``
     - ``Reads the operations update``

Each tool has a clear, distinct description. The model sees three tools of the
same type, so the description is the only way it can tell them apart. See
:doc:`/agentic-ai-guide/tools-integrations/tools-connectors`.

Model settings
--------------

The Agent Node's **LLM Configuration** tab uses these settings:

.. list-table:: LLM settings
   :header-rows: 1
   :widths: 40 60

   * - Setting
     - Value
   * - **Select Connection**
     - An LLM connection, here ``AZURE_FOUNDRY-4.1`` (GPT-4.1)
   * - **Temperature**
     - ``0``
   * - **Top P**
     - ``1.0``
   * - **Max Tokens**
     - ``500``
   * - **Timeout (seconds)**
     - ``180``
   * - **Max Tool Rounds**
     - ``8``
   * - **Output Format**
     - **text**

**Temperature 0** keeps the summary close to the source figures. **Max Tool
Rounds 8** leaves room for the three reads.

The instructions
----------------

The **Agent Instruction** tab tells the agent to read all three sources with
the ``Read CSV`` tools, summarize each one, then compare their key points:

.. code-block:: text

   You are a document summarization agent.
   Read all three sources with the Read CSV tools before writing anything:
   - the sales report
   - the support report
   - the operations update
   Summarize each one under its own heading: Sales, Support, Operations.
   Then compare their key points and finish with a short list of priorities.
   Verify every claim against the tool results. Do not invent figures.

Running the agent
-----------------

On the **Execute Agent** screen, **Agent Parameters** shows ``userQuery`` with
the request. Clicking **Execute** runs the agent.

.. figure:: ../../_assets/agentic-ai-guide/tutorials/document-summarization/execute.png
   :alt: Execute Agent screen with the userQuery parameter set to provide a summary for sales, support and operations
   :width: 900px

   The run starts with the ``userQuery`` value from the Input node.

The **Execution Timeline** shows each step as it completes. The Agent Node
makes one tool call per report:

.. figure:: ../../_assets/agentic-ai-guide/tutorials/document-summarization/timeline.png
   :alt: Execution timeline showing the Agent Node calling read_csv, read_csv_2 and read_csv_3 with their file paths
   :width: 680px

   ``read_csv``, ``read_csv_2`` and ``read_csv_3``, each with the file it read.

The result
----------

The Agent Node's output combines all three reports into one summary:

.. figure:: ../../_assets/agentic-ai-guide/tutorials/document-summarization/result.png
   :alt: Agent Node output with Sales, Support and Operations sections for August 2026
   :width: 680px

   **Sales** covers August revenue and order trends. **Support** covers ticket
   volume and resolution rates. **Operations** covers delivery performance and
   accessory restocking.

The summary closes with a short set of priorities drawn from all three
reports. Every figure in it comes from one of the three tool results.

Design notes
------------

* **One tool per source.** Each report has its own ``Read CSV`` tool, so the
  agent can read each one separately and the timeline shows which file each
  fact came from.
* **Distinct descriptions.** Without them, the agent may read only one or two
  of the reports.
* **Grounded output.** Temperature ``0`` and the instruction *Verify every
  claim against the tool results* keep the summary to the figures in the
  reports.
* **Output length.** **Max Tokens** ``500`` suits three short reports. Longer
  reports need a higher limit, or the summary stops mid-sentence.
