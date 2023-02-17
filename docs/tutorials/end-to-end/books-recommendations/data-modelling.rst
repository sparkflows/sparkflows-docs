Books Recommendations ML Model
=============================

This tutorial will cover how to model data related to book sales. The data has been taken from Kaggle courtesy of the BookCrossing project. 

Recommending Books Based on Popularity
-------------------------
The below workflow: 

* Groups the Ratings by ISBN.
* Calculates the weighting rating for each book.
* Sorts the books by their weighted rating.
* Prints out a top 20 list of the best books to recommend.


   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/books_popularity.PNG
      :alt: books-recommendations
      :width: 70%
   

Grouping Ratings by ISBN
-----------------------------------

We use the ``Group By`` processor to group the data based on values from a single column. This processor also allows us to calculate aggregate statistics for other columns that we select. In this case we are using ``Group By`` to calculate the average and count of Book_Ratings to be used later when we calculate the weighted ratings for each book.  

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Group_By_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Processor Output
^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Group_By_Output.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Calculating Weighted Ratings
-----------------------

We use the ``Math Expression`` processor to create a new column based on a user-provided math expression. In this case we are applying a weighting formula to adjust our ratings. When making recommendations based on ratings, if we were to use the average ratings for each books, the books that have been rated very highly, but by very few users would have a natural advantage. This formula takes into account not only the average ratings, but also the number of ratings relative to other books. This formula is a simplified version of the formula that IMDB uses to rank movies based on user-generated ratings. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Math_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Processor Output
^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Math_Output.PNG
      :alt: titanic-data-cleaning
      :width: 75%


Sorting Books by Weighted Ratings
------------------------

We use the ``Sort By`` processor to sort the data based on the numeric values in the selected column. In this case we are sorting the data based on the previously calculated weighted rating to rank the books. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Sort_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Printing the Top 20 Books to Recommend
----------------------

We use the ``Print N Rows`` processor to display a certain number of rows from the data. In this case we are displaying the top 20 books to be recommended. We can also see in the output how the weighted ratings compare to the average ratings(column R). We can also see how without using the weighted ratings instead of average ratings, it would impossible to seperate the top few books.  

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Print_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Processor Output
^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRP_Print_Output.PNG
      :alt: titanic-data-cleaning
      :width: 75%




Recommending Books Based on ALS
-------------------------
The below workflow: 

* Indexes the string column ISBN.
* Splits the data into training and testing datasets.
* Builds an ALS model using SparkML.
* Filters the rows to remove NaN values.
* Graphs the predicted values.
* Calculates the RMSE of the ALS model.


   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/books_als.PNG
      :alt: books-recommendations
      :width: 75%
   
   
   
Indexing the String ISBN Column
------------------------

We use the ``String Indexer`` processor to index / convert a string column to a numeric column. This allows us to use string columns in models that require only numeric values. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_String_Indexer_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Splitting the Data
------------------------

We use the ``Split`` processor to split the data into training and testing datasets for validating models. The ``Split`` processor allows us to choose the proportion of data to be put into each dataset. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_Split_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Building an ALS Model
------------------------

We use the ``ALS`` processor to build and ALS (Alternating Least Squares) model using SparkML. An ALS model attempts to predict what a particular user would rate a particular book based on their past reviews of other books. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_ALS_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Filtering Out NaN Values
------------------------

We use the ``Row Filter`` processor to filter rows based on a conditional statement set by the user. In this case we are filtering out all rows that contain the value "NaN" in the predictions column. Some models may create NaN values under specific circumstances so the ``Row Filter`` processor can be used to clean the data after modelling. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_Row_Filter_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Graphing the Predicted Values
----------------------

We use the ``Graph Values`` processor to graph the selected columns. In this case we are grpahing a selection of the predicted ratings. The ``Graph Values`` processor also allows us to graph multiple columns on the Y-axis. We are also graphing the actual ratings to compare with the predicted ratings and get an idea of how accurate our model is. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_Graph_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Processor Output
^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_Graph_Output.PNG
      :alt: titanic-data-cleaning
      :width: 75%
   
   
Calculating the RMSE
----------------------

We use the ``Regression Evaluator`` processor to calculate various model metrics. In this case we are calculating RMSE to quantify the performance of our model. 

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_Evaluator_Config.PNG
      :alt: titanic-data-cleaning
      :width: 75%

   
Processor Output
^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/data-engineering/books-recommendations/BRA_Evaluator_Output.PNG
      :alt: titanic-data-cleaning
      :width: 75%
