Change Data Capture
===================

There are many times when we need to  Change Data Capture.

Below is one way to do CDC with Fire.

Overview
--------

We have streaming events coming in. The events can be updates to the existing records. In the final table, we need to publish only the latest record.

Design
------

We keep a staging table. This table would have all the records coming in. We do dedup at the end of the day and publish it to the final table. 

Let us say that we are getting real time events of orders. As we get these events we append it to the staging table. If there are updates to an order, say an order got cancelled, we will have multiple records for that order in the staging table.

There is a final published order table where there are no duplicates. It gets updated once a day.

We join the final order table with the staging table. In doing so we get multiple order entries. We take the one with the latest timestamp and drop the others. Then for a given order we have only one record in the final table. We rewrite the final orders table with the newly calculated records.

