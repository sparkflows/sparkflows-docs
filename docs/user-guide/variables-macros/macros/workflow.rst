Macros in Workflows
==================

Macros that Sparkflows supports
++++++++++++++++++++++++++++++

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Macro
     - Description
   * - ``${fire.ds}``
     - 
   * - ``${fire.ds_nodash}``
     -
   * - ``${fire.ts}``
     -
   * - ``${fire.wf.name}``
     - 
   * - ``${fire.wf.id}``
     -
   * - ``${fire.wfe.id}``
     - 
   * - ``${fire.wfe.username}``
     -
   * - ``${fire.pl.name}``
     -
   * - ``${fire.pl.id}``
     -
   * - ``${fire.ple.id}``
     - 
   * - ``${fire.ple.username}``
     -
   * - ``${fire.macros.ds_add(ds, days)}``
     -
   * - ``${fire.macros.ds_format(ds, input_format, output_format)}``
     -
   * - ``${fire.macros.random()}``
     -
   * - ``${fire.macros.ds_format(ds, days, input_format, output_format)}``
     -
   * - ``${fire.macros.ts_add(ts, days)}``
     -
   * - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 
   * - ``${fire.macros.ts_format(ts, input_format, output_format)}``
     - 



Macros related to Date
+++++++++++++++++++++++++

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1

   * - Current Date
     - Operation
     - Input
     - Output
   * - 2024-11-19
     - ``${fire.macros.ds_add(ds, days)}``
     - 1
     - 2024-11-20
   * - 2024-11-19	
     - ``${fire.macros.ds_add(ds, days)}``
     - -1
     - 2024-11-18
   * - 2024-11-19	
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, d,DD-mm-YYYY,0
     - 2024-11-19
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, m,DD-mm-YYYY,0
     - 2024-11-19
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, y,DD-mm-YYYY,0
     - 2024-11-19
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, d,DD-mm-YYYY,-1
     - 18-11-2024
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, m,DD-mm-YYYY,-1
     - 19-10-2024
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, y,DD-mm-YYYY,-1
     - 19-11-2023
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, d,DD-mmm-YYYY,-1
     - 18-NOV-2024
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, m,DD-mmm-YYYY,-1
     - 19-OCT-2024
   * - 2024-11-19
     - ``${fire.macros.ds_format(ds,days, input_format, output_format)}``
     - 2024-11-19, y,DD-mmm-YYYY,-1
     - 19-NOV-2023

Macros related to Timestamp
+++++++++++++++++++++++++++++

.. list-table:: 
   :widths: 25 25 25 25
   :header-rows: 1

   * - Current Timestamp
     - Operation
     - Input
     - Output
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, d,YYYY-mm-DD HH-MM-SS,0
     - 2024-11-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, m,YYYY-mm-DD HH-MM-SS,0
     - 2024-11-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, y,YYYY-mm-DD HH-MM-SS,0
     - 2024-11-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, h,YYYY-mm-DD HH-MM-SS,0
     - 2024-11-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, m,YYYY-mm-DD HH-MM-SS,0
     - 2024-11-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, d,YYYY-mm-DD HH-MM-SS,-1
     - 2024-11-18 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, m,YYYY-mm-DD HH-MM-SS,-1
     - 2024-10-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, y,YYYY-mm-DD HH-MM-SS,-1
     - 2023-11-19 14:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, h,YYYY-mm-DD HH-MM-SS,-1
     - 2024-11-19 13:19:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, mi,YYYY-mm-DD HH-MM-SS,-1
     - 2024-11-19 14:18:44
   * - 2024-11-19 14:19:44
     - ``${fire.macros.ts_format(ts, days, input_format, output_format)}``
     - 2024-11-19 14:19:44, s,YYYY-mm-DD HH-MM-SS,-1
     - 2024-11-19 14:19:43
    
 
