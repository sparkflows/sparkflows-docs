Books Recommendations
========

This tutorial will cover how to explore, clean, and model data related to book sales. The data has been taken from Kaggle courtesy of the BookCrossing project. 

The data for this project is split into 3 datasets. One dataset contains data related to the users, one dataset contains data related to the books, and the final dataset contains all of the user-generated ratings of the books. 

To more accurately represent how data analysis would be done in Sparkflows, different tasks have been split up into different workflows. This keeps the project more organized, allows for more expansion in the future, and will provide performance benefits during testing and execution. 


.. panels::
    :container: container-lg pb-3

    :doc:`/tutorials/end-to-end/books-recommendations/data-cleaning`

    This workflow does data cleaning on the Books Dataset.

    ---

    :doc:`/tutorials/end-to-end/books-recommendations/data-exploration`

    This workflow does data exploration on the Books Dataset.   

    ---

    :doc:`/tutorials/end-to-end/books-recommendations/data-modelling`

    This workflow builds ALS recommendations model on the Books Dataset.  
   
   
.. toctree::
   :hidden:

   data-cleaning.rst
   data-exploration.rst
   data-modelling.rst
   
