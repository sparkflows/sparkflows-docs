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

