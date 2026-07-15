Text Analysis
=============

Sparkflows ships a family of **Text Analysis** processors that turn free-text columns into structured signals — sentiment, emotion, summaries, categories, grammatical acceptability and inference — with a single low-code node. Most of them run **local Hugging Face models**, so they need **no API key** and no data leaves your environment. One node (**Text Analysis**) instead uses a configured LLM connection for richer, prompt-driven analysis.

Every node reads one text column and appends its result columns to the incoming DataFrame, so you can chain it after any reader or transform.

Processors
----------

.. list-table::
   :widths: 32 68
   :header-rows: 1

   * - Node
     - What it does
   * - Hugging Face Sentiment Analysis
     - Classifies each text value as **POSITIVE** / **NEGATIVE** with a confidence score. Default model ``distilbert-base-uncased-finetuned-sst-2-english``.
   * - Hugging Face Tone Analysis
     - Predicts the dominant **emotion / tone** (joy, anger, sadness, fear, surprise, …) with a confidence score.
   * - Hugging Face Summarization
     - Produces a short **abstractive summary** of each long text value.
   * - Hugging Face Custom-Category (Zero-Shot)
     - Labels each text value with the best-fitting label from **your own** ``category_list`` — no training needed (zero-shot).
   * - Hugging Face Grammatical Correctness
     - Judges whether each text value is **grammatically acceptable** (CoLA), with a confidence score.
   * - Hugging Face Natural Language Inference
     - Given a premise and hypothesis, labels the pair **entailment / contradiction / neutral**.
   * - Hugging Face Question NLI
     - Determines whether a document contains the answer to a question (**entailment / not-entailment**).
   * - Text Analysis
     - LLM-driven analysis (slang, intent, key phrases, and more) using a configured LLM connection.

Ready-to-run templates
----------------------

Import any of these from the **Gen AI** template category and run them as-is — each reads the bundled ``Product-Review.csv`` sample and prints the labelled output.

.. list-table::
   :widths: 38 62
   :header-rows: 1

   * - Template
     - Demonstrates
   * - Sentiment Analysis with Hugging Face
     - Positive/negative sentiment on the ``text`` column with a local model.
   * - Emotion & Tone Analysis with Hugging Face
     - Dominant emotion/tone per row.
   * - Text Summarization with Hugging Face
     - Short abstractive summaries of long text.
   * - Zero-Shot Text Classification with Hugging Face
     - Classifies text into your own categories (``product quality``, ``delivery experience``, …) with no training.
   * - Grammatical Correctness with Hugging Face
     - Flags grammatically unacceptable text.
   * - Natural Language Inference with Hugging Face
     - Entailment / contradiction / neutral labelling.

Configure a node
----------------

Each Hugging Face node has the same essentials:

* **Column to analyse** — the text column to read (for example, ``text``).
* **Pre-loaded model** — pick a bundled model, or enter any Hugging Face model id.
* **Custom model** *(optional)* — supply your own model name when the server has internet access to pull it.
* **Category list** *(zero-shot only)* — the candidate labels to classify into.

Worked example — Sentiment Analysis
-----------------------------------

The **Sentiment Analysis with Hugging Face** template reads product reviews and classifies the ``text`` column. Running it on the sample data produces:

.. code-block:: text

   rating=5   POSITIVE (1.00)   These gloves are the best I have bought...
   rating=1   NEGATIVE (1.00)   As shown in the photo it leaks and is very bad quality.
   rating=4   NEGATIVE (0.94)   May lose colour a lot quicker and it tears easy when wet.
   rating=5   POSITIVE (0.99)   I had to return the first box of Kimberly Clark...

The predicted sentiment tracks the star rating and even catches nuance — a four-star review that raises a quality complaint is flagged negative.

.. tip::

   The Hugging Face nodes download their model on first run and cache it locally. To run fully offline, set the **Pre-loaded model path** to a directory containing the downloaded model.
