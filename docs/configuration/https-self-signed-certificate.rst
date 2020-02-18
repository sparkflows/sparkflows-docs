HTTPS : Self-Signed Certificates
================================

Fire Insights comes with a self-signed certificate. It is contained in conf/keystore.jks.

When using the self-signed certificate, the Browser will complain as it has not been issued by a Certificate Authority.

This warning message can be supressed by importing the self-signed certificate into the Browser  inside  ``Trusted Root Certification Authorities``.

Below are the steps for it.

- Login to `URL` which is running on `HTTPS` port.
   - https://privateip:8443/login

.. figure:: ../_assets/configuration/Url_https.PNG
   :alt: certificate
   :align: center
   :width: 60%
   
- Click on ``Not secure`` option.
 
.. figure:: ../_assets/configuration/Notsecure.PNG
   :alt: certificate
   :align: center
   :width: 60%
   
- Click on ``Certificate``.

.. figure:: ../_assets/configuration/certificate.PNG
   :alt: certificate
   :align: center
   :width: 60%
   
   

- View ``Certificate``.

.. figure:: ../_assets/configuration/viewcertificate.PNG
   :alt: certificate
   :align: center
   :width: 60%

- Click on ``Details`` option.

.. figure:: ../_assets/configuration/certificatedetails.PNG
   :alt: certificate
   :align: center
   :width: 60%

- Click on ``copy to  file`` option.

.. figure:: ../_assets/configuration/copyfile.PNG
   :alt: certificate
   :align: center
   :width: 60%

- Select below option and press ``Next``.

.. figure:: ../_assets/configuration/exportfile.PNG
   :alt: certificate
   :align: center
   :width: 60%
   
- Select the ``Name & file location`` of certificate.

.. figure:: ../_assets/configuration/filelocation.PNG
   :alt: certificate
   :align: center
   :width: 60%

- After Upadating details ``Success msg`` will apear.

.. figure:: ../_assets/configuration/exportcertificate.PNG
   :alt: certificate
   :align: center
   :width: 60%

- Once the above steps Completed Successfully, Need to add certificate to Browser
   - Using Google chrome
   
- Go to below location after opening ``Googlechrome``.
   - Settings -> Advanced -> Privacy and Security-> Manage Certificates 
   

.. figure:: ../_assets/configuration/managecertificate.PNG
   :alt: certificate
   :align: center
   :width: 60%

- Click on ``Manage Certicate`` icon.

.. figure:: ../_assets/configuration/managebrowsecert.PNG
   :alt: certificate
   :align: center
   :width: 60%

- Click on ``import``.

.. figure:: ../_assets/configuration/import.PNG
   :alt: certificate
   :align: center
   :width: 60%


