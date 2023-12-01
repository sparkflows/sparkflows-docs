WebSockets
============

In Fire Insights, the browser uses WebSockets for communications for some of the web pages of Fire Insights.
This document explains some of the common issues and corresponding resolutions related to WebSockets:

1. WebSocket Connection Error
----------------------

**Problem**
+++++

When clicking on **Execute** to execute a workflow, a dialog box appears that it could not connect to the Server.

In the developer tools, it displays **Websocket connection failed**.

**Solution**
+++++

- Check if the Websocket ports are open within the VPC.
- Check if any Firewall / Security agent inside VPC / VM blocking the socket connection.
- Check if the browser version is supported. For example, this is a `sockjs version details table. <https://github.com/sockjs/sockjs-client#supported-transports-by-browser-html-served-from-http-or-https>`_
- Ensure VPN / Antivirus not blocking Websocket connectivity.
- Check if enough memory (min 16GB) allocated to Sparkflows.
- Check if the websocket connection is not dropped either by a firewall, proxy or others.

**The web socket connectivity can be tested using wscat command via the below steps:**

#. Install Node.js via the `npm` package manager as outlined here: `Node.js and npm Installation Guide <https://docs.npmjs.com/downloading-and-installing-node-js-and-npm>`_

#. Install the tools wscat using the command::

   npm install -g wscat

#. Capture the request headers being sent when you click on the Execute button of the Pipeline or Workflow.

   .. figure:: https://user-images.githubusercontent.com/88324072/216518054-a7f2572b-7211-4d3c-9afa-381c652df3d0.png
      :alt: Pipeline List
      :width: 60% 

#. Extract the header **Cookie** and **Sec-WebSocket-Key** and replace them in the below **wscat** command and run it from the command line::

   wscat -c wss://ecs.sparkflows.net/workflowexecute/415/kzv1urcw/websocket --header Sec-WebSocket-Key:0rma9fsOJoYnB69cOGo7VQ== --header Cookie:"XSRF-TOKEN=e2700ad3-756e-47c8-b2e4-5b79094ec30b; SESSION=ZTYxYWFjYjAtYjFjYy00MGY3LWJkZjUtYmY5MjM5NWQyMzY4"

#. If the WebSocket connection is allowed to go through, you will get back a **Connected** message and it will get connected. Now, one can execute WebSocket command.

   If the WebSocket is blocked, you will see an **Error** message.

#. Also, if you are using SSL with certificate, you would need to provide those details in the **wscat** command. These can be passed in as arguments to the **wscat** command. The supported arguments can be seen in the `wscat package documentation. <https://www.npmjs.com/package/wscat>`_ A representative example can be seen below::

    wscat --key server.key.pem --cert server.pem -c wss://127.0.0.1:8080

#. If you are using a self signed certificate, please pass the **--no-check** as seen below to ignore the unauthorized certificate::

    wscat --no-check --key server.key.pem --cert server.pem -c wss://127.0.0.1:8080

