URL Single Record JSON Reader
===============================
This node reads content of a JSON file present at the provided URL.

Below is a sample workflow which contains the URL Single Record JSON Reader processor in Fire Insights. It demonstrates the usage of URL Single Record JSON Reader node to read the content of a JSON file present at the provided URL.

 .. figure:: ../../../_assets/user-guide/read-write/read-structured/read-JSON-URL-WF.png
    :alt: readwrite_userguide
    :width: 50%
   

It does the following processing of data:

*	Reads the content of a JSON file present at the provided URL using URL Single Record JSON Reader node.
*	Prints the content of JSON file in a tabular format.


**URL Single Record JSON Reader node configuration**

The URL Single Record JSON Reader node is configured as below.

* ``URL``: Enter the URL address containing JSON file. 
* ``Refresh Schema``: Click on this button to list schema of the JSON file.
*	Output prints the content of JSON file in a tabular format.

 .. figure:: ../../../_assets/user-guide/read-write/read-structured/url_config.PNG
    :alt: readwrite_userguide
    :width: 70%
   
**URL Single Record JSON Reader node output**

Output of the URL Single Record JSON Reader node prints the content of JSON file in a tabular format.

 .. figure:: ../../../_assets/user-guide/read-write/read-structured/url_output.PNG
    :alt: readwrite_userguide
    :width: 70%       	    
