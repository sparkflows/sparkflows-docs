Python-integration
==================

In this page it Explain How to setup python 3 & virtual environment.

Install Python 3
-----------------

Steps involved in installing Python-3.6 on Centso7, Do this from Root user.
  - cat /etc/os-release
  - curl -O https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
  - tar xf Python-3.6.4.tgz
  - cd Python-3.6.4
  - yum install gcc
  - ./configure
  - make
  - make install
  - yum install libffi-devel
  - export PATH=$PATH:/usr/local/bin/python3.6
  
Install pip/wheel
-----------------

Steps involved in Installing package
  - yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  - yum install python-pip
  - yum install python-wheel
  
Install and configure virtualenv to point to python 3.6
-------------------------------------------------------

Steps involved in Installing and configuring virtualenv to point to python 3.6
  - sudo pip install virtualenv
  - virtualenv -p /usr/local/bin/python3.6 ~/venv
  - venv/bin/activate
  - python --version
  
Install Pandas and scikit-learn in Virtual environment
------------------------------------------------------

Steps involved in Installing Pandas and scikit-learn in Virtual environment
  - source venv/bin/activate
  - pip install pandas
  - pip install scikit-learn  
  
Install pyspark and other packages
-----------------------------------

Steps involved in installing pyspark & other packages.
  - pip install tornado
  - pip install requests
  - pip install pyspark==2.1.2
  - pip install pyspark[sql]
    
  
