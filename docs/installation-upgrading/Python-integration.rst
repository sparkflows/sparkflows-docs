Python-integration
==================

In this page it Explain How to setup python 3 & virtual environment.

Install Python 3
-----------------

Steps involved in installing Python-3.6 on Centso7
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
