Stanford Core NLP
------------------

Stanford CoreNLP provides a set of natural language analysis tools. It can give the base forms of words, their parts of speech, whether they are names of companies, people, etc., normalize dates, times, and numeric quantities, mark up the structure of sentences in terms of phrases and word dependencies, indicate which noun phrases refer to the same entities, indicate sentiment, extract particular or open-class relations between entity mentions, get quotes people said, etc.

Sparkflows leveraged Stanford NLP to provide the below NLP capabilities:

* Named Entity Recognizer: Stanford NLP's Named Entity Recognizer can identify and classify entities such as names of people, organizations, and locations in text.

* Part-Of-Speech Tagger (POS Tagger): The POS Tagger assigns grammatical categories (e.g., noun, verb) to words in sentences, aiding in syntactic analysis.

* TokensRegex: TokensRegex is a powerful tool for defining and extracting complex patterns from text using regular expressions.

* RegexNER: Stanford NLP's RegexNER allows you to perform named entity recognition based on regular expressions, providing flexibility in identifying custom entities.

* Word Segmenter: The Word Segmenter can split text into individual words or tokens, a fundamental step in NLP.

* Pattern-based Information Extraction and Diagnostics (SPIED): SPIED enables the extraction of structured information from unstructured text using predefined patterns.

* Tregex, Tsurgeon, and Semgrex: These tools provide advanced linguistic query and transformation capabilities for analyzing and manipulating parse trees and linguistic structures.

* Relation Extractor: Stanford NLP's Relation Extractor can discover relationships between entities in text, such as identifying who works for a particular organization.

* Coreference Resolution: Coreference Resolution helps determine which words or phrases in text refer to the same entity, improving text understanding and analysis.

More details of Stanford Core NLP can be found here : http://stanfordnlp.github.io/CoreNLP/
