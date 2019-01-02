Dedup
=========== 

This node is used for problems like entity resolution or data matching. Entity resolution or Data matching is the problem of finding and linking different mentions of the same entity in a single data source or across multiple data sources.

Input
--------------
It takes in a DataFrame as input

Output
--------------
Dataframe with confidence score field and other selected scores for entities

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeDedup

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - confidenceScore
        - Confidence Score
        - Confidence Score
      * - lhsCols
        - LHS Variables
        - LHS columns for matching
      * - rhsCols
        - RHS Variables
        - RHS columns for matching
      * - matchingAlgorithms
        - Algorithm to use
        - Algorithm to use for matching
      * - matchingWeights
        - Weights
        - Weights for matches
      * - outputCols
        - Output Column
        - Output Column


Details
======


Levenstein
+++++++++++++++

The Levenshtein distance between two strings is defined as the minimum number of edits needed to transform one string into the other, with the allowable edit operations being insertion, deletion, or substitution of a single character.

How many char you change to make two strings equal.


JaroWinker
+++++++++++++++

Jaro–Winkler distance for two strings is, the more similar the strings are. The Jaro–Winkler distance metric is designed and best suited for short strings such as person names. The score is normalized such that 0 equates to no similarity and 1 is an exact match.

Good for short words, typos and nikename.

 Fullmatch
+++++++++++++++

Fullmatch distance for two strings is, how two strings are match exactly. The score is assigned such that 1 is for exact match and 0 is for not match.


Jaccard
+++++++++++++++

The Jaccard similarity measures similarity between finite sample sets, and is defined as the cardinality of the intersection of sets divided by the cardinality of the union of the sample sets. Suppose you want to find jaccard similarity between two sets A and B it is the ration of cardinality of A ∩ B and A ∪ B.

Sparkflows provide default 3-gram Jaccard similarity measures.


Longest common subsequences(LCS): LCS distance between strings s1 and s2, computed as |s1| +|s2| - 2 * |LCSfunction(s1, s2)| and distance is normalized between 0 and 1.

LCSfunction returns the length of Longest Common Subsequence (LCS) between strings s1 and s2.



Notional distance
+++++++++++++++

Notional distance between two numbers X and Y, computed as  abs(X - Y) / abs(x) + abs(Y).

Date Difference
+++++++++++++++

Date Difference gives number of days between two dates(yyyy-MM-dd).


