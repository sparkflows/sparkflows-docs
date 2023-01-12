SQL Examples
----------------------

Fire Insights provides a SQL processer in which SQL can be written.

It does the below:

  * Receives an input dataframe.
  * Creates a temporary table on top of the dataframe.
  * Allows the user to write a SQL which would be executed on the temporary table.
  * The resulting dataframe of running the SQL is passed on to the next node/processor.


Example 1: Calculate Average Lotsize by Number of Bedrooms
=========

::

    select bedrooms, avg(lotsize) as avg_lotsize from fire_temp_table group by bedrooms

Example 2: Using CASE Statement to Check Conditions against Column Value
==========

::

    select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW > 40 then 1.0 else 0.0 END as label from fire_temp_table

Example 3: Using Another Form of CASE Statement
==========

::

    select customer_id, rValue, fValue , mValue,
    case when rValue <= 35 then 3.0 
         when rValue  > 35 and rValue <= 112 then 2.0
         else 1.0
         end as rScore,
    case when fValue >= 15 then 3.0
         when fValue >= 4 and fValue < 15 then 2.0
         else 1.0
         end as fScore,
    case when mValue >= 50000.0 then 3.0
         when mValue >= 25000.0 and mValue < 50000.0 then 2.0
         else 1.0
         end as mScore,
    mValue / fValue  as avg_amount from fire_temp_table
    
Example 4: Using CAST Statement to Convert Datatypes 
==========

::

     select cast(current_date as STRING) datetostring , cast ('2021' as int) stringtoint, cast('2021-01-01' as date) stringtodate 
     from fire_temp_table

Example 5: Using Date Functions
=========

::

    select current_date as date, current_timestamp as timestamp, date_add(current_date , 5) as addtodate, 
    date_sub(current_date , 5) as subtractfromdate from fire_temp_table
    
Example 6: Using CONCATENATE Function
=========

::

    select  concat_ws('-','firstname,lastname) as ClientName from fire_temp_table

