HTTPS
=============

Fire Insights can be Configured with HTTPS, by default it come up with self signed certificate, User can configured customized certificate (CA).

Certificate is not Trusted
-----

Problem
+++++

When the user use self signed certificate, on Browser it complains that Certificate is not Trusted.

Solution
+++++

- Check if certificate configured is certified by CA
- You can trust the local certificate, so that error will disappear.

Not Able to Access on HTTPS
------------

Problem
+++++

When user Try to access on ``https` in Browser, its not complaining page not found.

Solution
+++++

- Check if `https` port ``443`` is open and accessible.
- Make sure to validate ``application.properties`` file and see if what would be expected port which is configured for ``https``
