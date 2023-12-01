HTTPS
=============

Fire Insights can be configured with HTTPS. By default, it comes up with self signed certificate. User gets the option to configure customized certificate (CA).

This document explains some of the common issues and corresponding resolutions related to certificates.

1. Certificate is not Trusted
-----

**Problem**
+++++

When the user uses a self-signed certificate in the browser, it complains that the certificate is not trusted.

**Solution**
+++++

- Check if certificate configured is certified by CA.
- You can trust the local certificate, so that error will disappear.

2. Not Able to Access on HTTPS
------------

**Problem**
+++++

When user tries to access on **https** in browser, it shows a page not found error.

**Solution**
+++++

- Check if **https** port **443** is open and accessible.
- Make sure to validate **application.properties** file and see if what would be expected port which is configured for **https**.
