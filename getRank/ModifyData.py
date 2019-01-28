import json
from pprint import pprint

with open('data.json', 'r') as f:
    json_str = json.load(f)
    data = json.loads(json_str)

for contest in range(118,120+1):
	data["user4286"][str(contest)]=[-2,0]

for contest in range(118,120+1):
	data["Brooky"][str(contest)]=[-2,0]
	
for contest in range(118,119+1):
	data["zihao"][str(contest)]=[-2,0]	
	
for contest in range(118,119+1):
	data["DorisGe"][str(contest)]=[-2,0]		
	
for contest in range(118,120+1):
	data["yexiaoxiao2102"][str(contest)]=[-2,0]		
   
pprint(data)    

json_str = json.dumps(data)

with open('data.json', 'w') as f:
    json.dump(json_str, f)
    
########################

contests = {}
contests["121"] = 3924
contests["120"] = 3876
contests["119"] = 3847
contests["118"] = 3587

json_str = json.dumps(contests)

with open('contests.json', 'w') as f:
    json.dump(json_str, f)
    
