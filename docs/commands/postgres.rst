PostgreSQL
==========

Install psycopg2 for connecting with PostgreSQL from python
---------------------------

https://www.postgresqltutorial.com/postgresql-python/connect/

pip install psycopg2

Connect to the PostgreSQL database using the psycopg2
----------

python setup.py build
sudo python setup.py install

conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Abcd1234")

The following is the list of the connection parameters:

* database: the name of the database that you want to connect.
* user: the username used to authenticate.
* password: password used to authenticate.
* host: database server address e.g., localhost or an IP address.
* port: the port number that defaults to 5432 if it is not provided.
