import json
import os
import argparse
from FetchRanks import fetchRanking
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("contest", help="contest id")
kwargs = parser.parse_args()
contest = int(kwargs.contest)
pageNum = 400

results = fetchRanking(contest,pageNum)

if os.path.isfile("data.json"):
    with open('data.json', 'r') as f:
    	json_str = json.load(f)
    	data = json.loads(json_str)
else:
    data = {}
		
for key in results:  
  if key not in data:
    data[key] = {}
    data[key][str(contest)] = results[key]
  else:
    data[key][str(contest)] = results[key]
   
# pprint(data)    

json_str = json.dumps(data)

with open('data.json', 'w') as f:
    json.dump(json_str, f)


