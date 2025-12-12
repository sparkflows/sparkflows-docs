Python Packages
====

How can I use spacy package in a Pyspark node?
----
1. You must **load the model** object (e.g., nlp = spacy.load(...)) before you start iterating over your rows.

  * **Standard Method:** Use the model name: spacy.load("en_core_web_sm").
  * **Custom Path:** If using a local directory(for restricted environments), point directly to the folder: spacy.load("/path/to/model/directory").
  * **Best Practice:** Initialize nlp inside your preprocessing function or immediately before the transformation loop within myFn. This ensures the model is loaded in the active memory context where the data processing actually happens.

2. You can **enable/disable**  specific **spaCy** components (NER, Parser). If you only need lemmatization and tokenization, disable the parser and named entity recognizer (NER). This significantly speeds up the nlp() call.
                                              
**Example:** ``nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])``

Example Usage
++++
Below is an example usage in a PySpark Custom Node:
                                                
.. code-block:: python

    import spacy
    from pyspark.sql import SparkSession
    
    def myfn(spark: SparkSession, workflowContext, id, inDF, cust_dict):
        
        # 1. Load the NLP model (path for the model should be pointing to the corpus)    
             nlp = spacy.load("/home/sparkflows/en_core_web_sm/..."])
    
        # 2.Select the column and convert it to pandas dataframe
            pdf = inDF.select("complaint").toPandas()
    
        # 3. Define preprocessing: Lowercase -> Tokenize -> Filter Stops/Punct -> Lemmatize
             def clean_text(text):
             doc = nlp(str(text).lower())
             return " ".join([t.lemma_ for t in doc if not t.is_stop and not t.is_punct])
    
        # 4. Apply transformation and return
             pdf["clean_text"] = pdf["complaint"].apply(clean_text)
             outDF = spark.createDataFrame(pdf)
             return outDF



















                                              
