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
	
data["Ansonluo1"]['118']=[1799,1]			
data["Ansonluo1"]['119']=[556,3]			
data["Ansonluo1"]['120']=[1622,2]			
data["Ansonluo1"]['121']=[769,2]		

for contest in range(118,121+1):
	data["XRS"][str(contest)]=[-2,0]	
	
data["kaizer87"]['118']=[641,3]
data["kaizer87"]['119']=[-1,0]
data["kaizer87"]['120']=[-1,0]
data["kaizer87"]['121']=[-1,0]
data["kaizer87"]['122']=[-1,0]			

for contest in range(118,121+1):
	data["user760"][str(contest)]=[-2,0]	
data["user760"]['122']=[352,4]

for contest in range(118,123+1):
	data["banrenmasanxing"][str(contest)]=[-2,0]	
	
for contest in range(118,123+1):
	data["hgzry812"][str(contest)]=[-2,0]	

for contest in range(118,123+1):
	data["Yizhao_Han"][str(contest)]=[-2,0]		
	
for contest in range(118,122+1):
	data["zhounaiding"][str(contest)]=[-2,0]				
data["zhounaiding"]['123']=[1800,1]
data["zhounaiding"]['124']=[321,4]

for contest in range(118,122+1):
	data["fish444556"][str(contest)]=[-2,0]				
data["fish444556"]['123']=[2215,1]
data["fish444556"]['124']=[1896,2]

for contest in range(118,124+1):
	data["huyouhyw"][str(contest)]=[-2,0]				

pprint(data)    

json_str = json.dumps(data)

with open('data.json', 'w') as f:
    json.dump(json_str, f)
    
########################

contests = {}
contests["118"] = 3587
contests["119"] = 3847
contests["120"] = 3876
contests["121"] = 3924
contests["122"] = 3482
contests["123"] = 3468
contests["124"] = 4174
contests["125"] = 4288

json_str = json.dumps(contests)

with open('contests.json', 'w') as f:
    json.dump(json_str, f)
    
