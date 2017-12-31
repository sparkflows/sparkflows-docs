
ElasticSearchLoad
^^^^^^ 

Stores the rows of the incoming DataFrame into Elastic Search

type

transform

nodeClass

fire.nodes.elasticsearch.NodeElasticSearchLoad

Fields

+-------------------+------------------------+----------------------------------+
| Name              | Title                  | Description                      |
+===================+========================+==================================+
| indexName         | Index Name             | Name of the Elastic Search Index |
+-------------------+------------------------+----------------------------------+
| elasticSearchHost | Elastic Search Host    | Name of the Elastic Search Host  |
+-------------------+------------------------+----------------------------------+
| elasticSearchPort | Elastic Search Port    | Port of Elastic Search           |
+-------------------+------------------------+----------------------------------+
| esIndexAutoCreate | es.index.auto.create   | ES Index Auto Create             |
+-------------------+------------------------+----------------------------------+
| esNodesWANOnly    | es.nodes.wan.only      | ES Nodes WAN Only                |
+-------------------+------------------------+----------------------------------+
| esNodesIngestOnly | es.nodes.ingest.only   | ES Nodes Ingest Only             |
+-------------------+------------------------+----------------------------------+
| esNodesDataOnly   | es.nodes.data.only     | ES Nodes Data Only               |
+-------------------+------------------------+----------------------------------+
| esNetHttpAuthUser | es.net.http.auth.user  | Username                         |
+-------------------+------------------------+----------------------------------+
| esNetHttpAuthPass | es.net.http.auth.pass  | Password                         |
+-------------------+------------------------+----------------------------------+
| esConfKeys        | Config Key/Value Pairs | More Config Values               |
+-------------------+------------------------+----------------------------------+
| esConfValues      | Config Key/Value Pairs | More Config Values               |
+-------------------+------------------------+----------------------------------+