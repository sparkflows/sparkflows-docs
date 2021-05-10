SQL Examples in Fire
----------------------

Fire provides a SQL processer in which SQL can be written.


Example 1: Calculate Average lotsize by number of bedrooms
=========

::

    select bedrooms, avg(lotsize) as avg_lotsize from fire_temp_table group by bedrooms

Example 2: Using a CASE statement to check conditions against column value
==========

::

    select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW > 40 then 1.0 else 0.0 END as label from fire_temp_table

Example 3: Using another form of CASE statement
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
    
Example 4: Using CAST statement to change datatype 
==========

::

    select cast(to_date(ds) as STRING) as forecast_date, yhat as sales_pred_mean, yhat_lower as sales_pred_lower,
    yhat_upper as sales_pred_upper from fire_temp_table

Example 5: Using Date Functions
=========

::

    select current_date as date, current_timestamp as timestamp, to_date(current_timestamp) as converttodate, 
    date_add(current_date , 5) as addtodate, date_sub(current_date , 5) as subtractfromdate 
    from fire_temp_table
