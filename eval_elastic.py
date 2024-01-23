#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings

import warnings
warnings.filterwarnings("ignore")

client = Elasticsearch(hosts = "http://@localhost:9200")
question_number = "2-1"
# Nombre de modalités ou valeurs uniques du champ "Division Name"

query = {
{
  "size": 0,
  "aggs": {
    "unique_makes": {
      "cardinality": {
          "field": "Division Name.keyword"}}}}}

response = client.search(index="eval", body=query)

with open("/mnt/c/Users/Charline/Desktop/Codes/elasticsearch/eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)

with open("/mnt/c/Users/Charline/Desktop/Codes/elasticsearch/eval/{}.json".format("q_" + question_number + "_request"), "w") as f:
  json.dump(query, f, indent=2)