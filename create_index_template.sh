#!/bin/bash
curl -XPUT 'http://elasticsearch:9200/_template/data-template?pretty' -d '
{
  "template": "data-*",
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "data": {
      "properties": {
        "message": {
          "type": "text"
        },
        "status": {
          "type": "keyword"
        }
      }
    }
  }
}
'
