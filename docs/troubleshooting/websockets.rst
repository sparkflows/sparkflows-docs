Websockets
============

In Fire Insights, the browser uses websockets for communications for some of the web pages of Fire Insights.
This document explains some of the common issues and corresponding resolutions related to Websockets:

Websocket Connection Error
------------------------------------------------------------

- Check if the Websocket ports are open within the VPC.
- Check if any Firewall / Security agent inside VPC / VM blocking the socket connection.
- Check if the browser version is supported. For example, this is a sockjs version details table. https://github.com/sockjs/sockjs-client#supported-transports-by-browser-html-served-from-http-or-https
- Ensure VPN / Antivirus not blocking Websocket connectivity
- Check if enough memory (min 16GB) allocated to Sparkflows


Websocket connection failed
---------------

Problem
+++++

When clicking on ``Execute`` to execute a workflow, a dialog box appears that it could not connect to the Server.

In the developer tools, it displays ``Websocket connection failed``.

Solution
+++++

