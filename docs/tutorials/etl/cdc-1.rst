Change Data Capture
===================

There are many times when we need to do Change Data Capture.

Below is one way to do CDC with Fire.

Overview
--------

There is a staging table. This table would have duplicates. We do dedup at the end of the day and publish it to the final table.

There is a trade off between read and writes.

We are getting real time events, say orders. As we get these events we append it to the staging table. If there are updates to an order, say an order got cancelled, now we have to dedup this order record.

We join the order table with the staging table. In doing so we get multiple order entries. We take the one with the latest timestamp and drop the others. Then for a given order we have only one record in the final table.
