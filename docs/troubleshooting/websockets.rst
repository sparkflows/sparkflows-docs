Websockets
============

In Fire Insights, the browser uses websockets for communications for some of the web pages of Fire Insights.
This document explains some of the common issues and corresponding resolutions related to Websockets:

Websocket Connection Error
------------------------------------------------------------

Problem
+++++

When clicking on ``Execute`` to execute a workflow, a dialog box appears that it could not connect to the Server.

In the developer tools, it displays ``Websocket connection failed``.

Solution
+++++

- Check if the Websocket ports are open within the VPC.
- Check if any Firewall / Security agent inside VPC / VM blocking the socket connection.
- Check if the browser version is supported. For example, this is a sockjs version details table. https://github.com/sockjs/sockjs-client#supported-transports-by-browser-html-served-from-http-or-https
- Ensure VPN / Antivirus not blocking Websocket connectivity
- Check if enough memory (min 16GB) allocated to Sparkflows


Websocket Debugging Steps
---------------

**Steps for debugging using the wscat command**

* Install Nodejs from the official website

* Install the tools wscat using the command

 - npm install -g wscat

* Capture the request headers being sent when you click on the Execute button

.. figure:: https://user-images.githubusercontent.com/88324072/216518054-a7f2572b-7211-4d3c-9afa-381c652df3d0.png
   :alt: Pipeline List
   :width: 60% 

* Use the header Cookie and Sec-WebSocket-Key

* Execute the following command

 - wscat -c wss://ecs.sparkflows.net/workflowexecute/415/kzv1urcw/websocket \
--header Sec-WebSocket-Key:0rma9fsOJoYnB69cOGo7VQ== \
--header Cookie:"XSRF-TOKEN=e2700ad3-756e-47c8-b2e4-5b79094ec30b; SESSION=ZTYxYWFjYjAtYjFjYy00MGY3LWJkZjUtYmY5MjM5NWQyMzY4"



