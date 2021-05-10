SQL Examples in Fire
----------------------

Fire provides a SQL processer in which SQL can be written.


Example 1: Calculate average lotsize by number of bedrooms
=========

::

    select bedrooms, avg(lotsize) as avg_lotsize from fire_temp_table group by bedrooms

Example 2: Using Case statements to check the condition against the column value and return a result
==========

::

    select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW > 40 then 1.0 else 0.0 END as label from fire_temp_table

