SQL Examples in Fire
----------------------

Fire provides a SQL processer in which SQL can be written.


Example 1
=========

select bedrooms, avg(lotsize) as avg_lotsize from fire_temp_table group by bedrooms

