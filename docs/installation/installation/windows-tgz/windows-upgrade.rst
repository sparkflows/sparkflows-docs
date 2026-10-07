Upgrade
=======

Upgrade Sparkflows on Windows to a new release. The new release is installed in a new folder next to the current one, so you can go back to the current release if something goes wrong.

All commands on this page are run in a **Command Prompt**.

Before You Upgrade
------------------

#. **Check the current version.** In the current installation folder, run the command below. ``releaseVersion`` is the installed Sparkflows version::

       cd %USERPROFILE%\fire-3.X.Y_spark_3.5.2
       type conf\version.txt

#. **Check the upgrade path.** Read the :doc:`/release-notes/index` for the versions between your current version and the new one, for any upgrade notes.

#. **Write down the current installation folder**, for example ``C:\Users\<user>\fire-3.X.Y_spark_3.5.2``. You need it to copy your settings, and to roll back.


Step 1 : Stop Sparkflows
------------------------

#. In the current installation folder, stop all Sparkflows processes::

       .\run-fire-agent.bat stop
       .\run-fire-polars.bat stop
       .\run-fire.bat stop
       .\run-fire-server.bat stop

#. Check that nothing is still listening on the Sparkflows ports. The command should print nothing::

       netstat -ano | findstr ":8080 :8081 :8089 :8200" | findstr LISTENING


Step 2 : Back Up
----------------

Make a dated backup of the database and the configuration. In the commands below, replace ``YYYY-MM-DD`` with today's date, for example ``2026-01-31``.

#. Create the backup folder::

       mkdir %USERPROFILE%\sparkflows-backup-YYYY-MM-DD

#. Back up the H2 database. The files are in your user folder::

       copy %USERPROFILE%\firedb.* %USERPROFILE%\sparkflows-backup-YYYY-MM-DD\

   If you use MySQL or PostgreSQL, back up that database with your usual database backup tools instead.

#. Back up the configuration of the current installation::

       xcopy /E /I %USERPROFILE%\fire-3.X.Y_spark_3.5.2\conf %USERPROFILE%\sparkflows-backup-YYYY-MM-DD\conf

#. Check that the backup folder contains ``firedb.mv.db`` (for H2) and the ``conf`` folder::

       dir %USERPROFILE%\sparkflows-backup-YYYY-MM-DD


Step 3 : Install the New Release
--------------------------------

#. Download the new Sparkflows TGZ file from https://www.sparkflows.io/download.

#. Extract it into your user folder, next to the current installation. Replace ``3.A.B`` with the new version::

       cd %USERPROFILE%
       tar -xzf fire-3.A.B_spark_3.5.2.tgz

   This creates a new installation folder, for example ``%USERPROFILE%\fire-3.A.B_spark_3.5.2``. Leave the current installation folder as it is.

#. Apply your settings to the new release. Compare each file below in the old and new installation's ``conf`` folders, and make your changes again in the new one. Do not copy the whole ``conf`` folder over: a new release can add or change settings.

   .. list-table::
      :widths: 35 65
      :header-rows: 1

      * - File in ``conf``
        - Settings to carry over
      * - ``db.properties``
        - The database connection, if you use MySQL or PostgreSQL.
      * - ``application.properties``
        - Ports (``http.port``, ``https.port``), and any engine or other settings you changed.
      * - ``keystore.properties`` and ``keystore.jks``
        - Your HTTPS certificate and its password, if you set up HTTPS. Copy your ``keystore.jks`` file as it is.
      * - ``sso.saml.properties``, ``ping.sso.saml.properties``, ``ldap.properties``
        - Single sign-on (SAML) and LDAP authentication settings, if you use them.
      * - ``aes-key.txt``
        - Copy this file from the old installation as it is.


Step 4 : Update the Database
----------------------------

In the new installation folder, update the database tables for the new release::

    cd %USERPROFILE%\fire-3.A.B_spark_3.5.2
    .\create-h2-db.bat

With MySQL or PostgreSQL, run ``.\create-mysql-db.bat`` or ``.\create-postgres-db.bat`` instead.


Step 5 : Start the New Release
------------------------------

#. Start the web server and the helper process from the new installation folder::

       .\run-fire-server.bat start
       .\run-fire.bat start

   If the command does not return to the prompt, leave this window open while Sparkflows runs, and open a new Command Prompt in the installation folder for the next commands.

#. **Set up Agents and Polars.** The new installation folder does not contain ``engine-venv``, so create it, then start the engines:

   #. Create the Python environment::

          .\install-fire-python.bat

      The script prints ``Done.`` when it completes.

   #. Start the engines::

          .\run-fire-polars.bat start
          .\run-fire-agent.bat start

   #. Check that both engines are running. Each prints ``Running on port <port>``::

          .\run-fire-polars.bat status
          .\run-fire-agent.bat status

   See :doc:`windows-install` for the script options.


Step 6 : Verify the Upgrade
---------------------------

Check each item before you remove the old release:

#. http://localhost:8080 opens the Sparkflows login page, and you can log in with your existing user.
#. ``type conf\version.txt`` in the new installation folder shows the new ``releaseVersion``.
#. ``log\fireserver-error.log`` in the new installation folder has no new errors.
#. Your projects and workflows are listed.
#. A small workflow runs successfully.
#. Your connections, for example to databases or LLM providers, still connect.
#. If you use Agents or Polars, both engines show ``Running on port <port>``.

When everything works, you can delete the old installation folder. Keep the backup folder until you are sure you do not need to roll back.


Roll Back
---------

If the upgrade does not work, go back to the previous release:

#. Stop all processes in the **new** installation folder, as in `Step 1 : Stop Sparkflows`_.

#. Restore the database from the backup::

       copy /Y %USERPROFILE%\sparkflows-backup-YYYY-MM-DD\firedb.* %USERPROFILE%\

   With MySQL or PostgreSQL, restore the database from your database backup instead.

#. Start Sparkflows from the **old** installation folder::

       cd %USERPROFILE%\fire-3.X.Y_spark_3.5.2
       .\run-fire-server.bat start
       .\run-fire.bat start

   If the prompt does not come back after ``.\run-fire.bat start``, leave that window open, and use a new Command Prompt for the next steps.

#. Verify as in `Step 6 : Verify the Upgrade`_.
