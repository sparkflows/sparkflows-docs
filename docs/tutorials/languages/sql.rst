SQL Examples
----------------------

Fire Insights provides a SQL processer in which SQL can be written.

It does the below:

  * Receives an input DataFrame.
  * Creates a temporary table on top of the DataFrame.
  * Allows the user to write a SQL which would be executed on the temporary table.
  * The resulting DataFrame of running the SQL is passed on to the next node/processor.


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

Example 7: Using WITH CLAUSE in SQL Node
=========

::

   WITH dept_avg_salary AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM fire_temp_table
    GROUP BY department
   ),
   lastname_avg_salary AS (
    SELECT LAST_NAME, AVG(salary) AS avg_salary
    FROM fire_temp_table
    GROUP BY LAST_NAME
   )
   SELECT e.employee_id, e.first_name, e.last_name, e.department, d.avg_salary, f.avg_salary
   FROM fire_temp_table e
   JOIN dept_avg_salary d ON e.department = d.department
   JOIN lastname_avg_salary f ON e.LAST_NAME = f.LAST_NAME
   WHERE e.salary > d.avg_salary  

Example 8: Using WITH CLAUSE in Join Using SQL Node
=========

::

    WITH dept_avg_salary AS (
     SELECT department, AVG(salary) AS avg_salary
     FROM tempTable1
     GROUP BY department
    ),
    lastname_avg_salary AS (
     SELECT LAST_NAME, AVG(salary) AS avg_salary
     FROM tempTable1
     GROUP BY LAST_NAME
    ),
    employee_data AS (
     SELECT * FROM tempTable2
    )
    SELECT e.*, e.employee_id, e.first_name, e.last_name, e.department, d.avg_salary, f.avg_salary
    FROM tempTable1 e
    JOIN dept_avg_salary d ON e.department = d.department
    JOIN lastname_avg_salary f ON e.LAST_NAME = f.LAST_NAME
    JOIN employee_data g ON e.EMPLOYEE_ID = g.EMPLOYEE_ID
    WHERE e.salary > d.avg_salary
