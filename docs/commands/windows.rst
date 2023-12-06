Windows Commands
===============
    
Generate Public Key
----------------

Windows 10 and 11::

    ssh-keygen

    Below steps need to be followed: 
    - Open Command Prompt using cmd command from windows start menu.
    - Enter ssh-keygen on the command prompt
    - It would suggest a default path where public key would be generated. It is recommended to leave it as it is otherwise enter a new path. It is also recommended if path mentioned is not empty then take a back-up before proceeding. 
    - It would ask for passphrase. It can be left blank. Press enter. 
    - It would ask to re-enter the passphrase. Press enter.
    - Two files would be generated in the path specified.
      * id_rsa
      * id_rsa.pub (This is the public key file)
