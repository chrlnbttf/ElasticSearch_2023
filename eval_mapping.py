#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings

import warnings
warnings.filterwarnings("ignore")

client = Elasticsearch(hosts = "http://@localhost:9200")

template = client.indices.get_mapping()

# Sauvegarde dans un fichier json
with open("/mnt/c/Users/Charline/Desktop/Codes/elasticsearch/eval/{}.json".format("index_template"), "w") as f:
  json.dump(dict(template), f, indent=2)