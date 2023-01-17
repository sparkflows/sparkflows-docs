HTTPS : Import Self-Signed Certificates
================================

Fire Insights comes with a self-signed certificate. It is contained in "conf/keystore.jks".

When you try to use self-signed certificate, the browser will complain as it has not been issued by a Certificate Authority.

You can import self-signed certificate into the browser inside ``Trusted Root Certification Authorities`` to suppress the warning message.

Below are the steps to import self-signed certificate into your browser:

Export the certificate to your machine
--------------------------------------------

- Got to ``URL`` for the ``HTTPS`` port.
   - https://privateip:8443/login

.. figure:: ../../../_assets/configuration/Url_https.PNG
   :alt: certificate
   :width: 60%
   
- Click on ``Not secure`` option.
 
.. figure:: ../../../_assets/configuration/Notsecure.PNG
   :alt: certificate
   :width: 60%
   
- Click on ``Certificate``.

.. figure:: ../../../_assets/configuration/certificate.PNG
   :alt: certificate
   :width: 60%
   
   

- View ``Certificate``.

.. figure:: ../../_assets/configuration/viewcertificate.PNG
   :alt: certificate
   :width: 60%

- Click on ``Details`` option to see detailed information of certificate.

.. figure:: ../../_assets/configuration/Certificatedetails.PNG
   :alt: certificate
   :width: 60%

- Click on ``copy to  file`` option to copy certificate to ``local machine``.

.. figure:: ../../_assets/configuration/Copyfile.PNG
   :alt: certificate
   :width: 60%

- Select below option and press ``Next``.

.. figure:: ../../_assets/configuration/Exportfile.PNG
   :alt: certificate
   :width: 60%
   
- Select the ``Name & file location`` of certificate.

.. figure:: ../../_assets/configuration/filelocation.PNG
   :alt: certificate
   :width: 60%

- On updation of details a ``Success msg`` will be displayed on the screen.

.. figure:: ../../_assets/configuration/exportcertificate.PNG
   :alt: certificate
   :width: 60%

Next, you need to add the exported certificate to the browser.

   
Add Certificate to the Browser
--------------------------
 
- Use Google chrome
   
- Open ``Google Chrome`` and follow the steps below:
   - Settings -> Advanced -> Privacy and Security-> Manage Certificates 
   

.. figure:: ../../_assets/configuration/managecertificate.PNG
   :alt: certificate
   :width: 60%

- Click on the ``Manage Certificates`` icon.

.. figure:: ../../_assets/configuration/Managebrowsecert.PNG
   :alt: certificate
   :width: 60%

- Click on ``Import``.

.. figure:: ../../_assets/configuration/import.PNG
   :alt: certificate
   :width: 60%

- Select ``certificate from local system``, then select ``Trusted Root Certification Authorities`` option and click on ``yes`` to save it.

.. figure:: ../../_assets/configuration/Trustedroot.PNG
   :alt: certificate
   :width: 60%
   

.. figure:: ../../_assets/configuration/Savingcertificate.PNG
   :alt: certificate
   :width: 60%

.. figure:: ../../_assets/configuration/successmsg.PNG
   :alt: certificate
   :width: 60%

- Once the above process is completed, close the ``browser`` and start again and try to login with above ``URL``. It should work without any warnings.

.. figure:: ../../_assets/configuration/sparkflow_loginpage.png
   :alt: certificate
   :width: 60%
   


* URL for further assistance: https://peacocksoftware.com/blog/make-chrome-auto-accept-your-self-signed-certificate 

