from parser import LeetcodeParser
from parser import LeetcodeParser2
import requests
from requests.auth import HTTPBasicAuth 
from bs4 import BeautifulSoup
import os
import json
import time
import argparse
from collections import deque
from config import Config
from config import Config2

if __name__ == "__main__":
    users = [name.strip() for name in open("id.in")]
    # users = ["wisdompeak","arignote"]

    lc_parser = LeetcodeParser(users, Config)
    lc_parser.parse()    
    profiles = lc_parser.results
    print("LC done")

    lc_parser2 = LeetcodeParser2(users, Config2)
    lc_parser2.parse() 
    profiles2 = lc_parser2.results
    print("LCCN done")
  
    for user in users:        
        print(f"processing {user}...")
        if profiles2[user]["userContestRanking"]==None:
            continue
        if profiles2[user]["userContestRanking"]["ratingHistory"] == None:
            continue
        rating2 = float(profiles2[user]["userContestRanking"]["ratingHistory"][1:-2].split(", ")[-1])
        if profiles[user]["userContestRanking"]==None:
            profiles[user]["userContestRanking"] = {"rating": rating2}            
        elif profiles[user]["userContestRanking"]["rating"] < rating2:
            profiles[user]["userContestRanking"]["rating"] = rating2
        print(profiles[user]["userContestRanking"]["rating"])


    json_str = json.dumps(profiles)
    with open('lc_profile_data.json', 'w') as f:
        json.dump(json_str, f)



