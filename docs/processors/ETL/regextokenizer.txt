
RegexTokenizer
^^^^^^ 

This node creates a new DataFrame by the process of taking text (such as a sentence) and breaking it into individual terms (usually words) based on regular express

type

transform

nodeClass

fire.nodes.etl.NodeRegexTokenizer

Fields

+-----------+------------------+--------------------------------------------+
|    Name   |      Title       |                Description                 |
+-----------+------------------+--------------------------------------------+
|  inputCol |      Column      |        input column for tokenizing         |
| outputCol | Tokenized Column |    New output column after tokenization    |
|  pattern  |     Pattern      | The regex pattern used to match delimiters |
|    gaps   |       Gaps       | Indicates whether the regex splits on gaps |
+-----------+------------------+--------------------------------------------+