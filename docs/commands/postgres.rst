PostgreSQL
==========

PostgreSQL Database Server
---------------------------

https://www.postgresqltutorial.com/postgresql-python/connect/

pip install psycopg2

python setup.py build
sudo python setup.py install

conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

