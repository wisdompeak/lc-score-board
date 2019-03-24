import json
from pprint import pprint

with open('data.json', 'r') as f:
    json_str = json.load(f)
    data = json.loads(json_str)
	
for contest in range(118,119+1):
	data["zihao"][str(contest)]=[-2,0]	
	data["DorisGe"][str(contest)]=[-2,0]		
	
for contest in range(118,120+1):
	data["user4286"][str(contest)]=[-2,0]
	data["Brooky"][str(contest)]=[-2,0]
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

for contest in range(118,122+1):
	data["user760"][str(contest)]=[-2,0]	
data["user760"]['122']=[352,4]

for contest in range(118,123+1):
	data["banrenmasanxing"][str(contest)]=[-2,0]	
	data["hgzry812"][str(contest)]=[-2,0]	
	data["Yizhao_Han"][str(contest)]=[-2,0]		
	
for contest in range(118,124+1):
	data["zhounaiding"][str(contest)]=[-2,0]				
	data["fish444556"][str(contest)]=[-2,0]				
data["zhounaiding"]['123']=[1800,1]
data["zhounaiding"]['124']=[321,4]
data["fish444556"]['123']=[2215,1]
data["fish444556"]['124']=[1896,2]

for contest in range(118,125+1):
	data["huyouhyw"][str(contest)]=[-2,0]				
	data["JackTheBest"][str(contest)]=[-2,0]
	data["MaggieZhao95"][str(contest)]=[-2,0]
	data["huange"][str(contest)]=[-2,0]
	data["crossbowman"][str(contest)]=[-2,0]
	data["Mengqian"][str(contest)]=[-2,0]
	data["please_AC"][str(contest)]=[-2,0]
	data["venico19"][str(contest)]=[-2,0]
	data["please_AC"]['124']=[742,3]	
data["huyouhyw"]['125']=[2068,2]		
data["please_AC"]['125']=[336,4]		
data["venico19"]['124']=[637,3]	
data["venico19"]['125']=[229,4]		

for contest in range(118,126+1):
	data["Golden_Fish"][str(contest)]=[-2,0]
	data["jiancheng2"][str(contest)]=[-2,0]
	data["Uneed"][str(contest)]=[-2,0]
	data["Dengxj"][str(contest)]=[-2,0]	
	data["vonxq"][str(contest)]=[-2,0]	
	data["1373757850"][str(contest)]=[-2,0]
	data["FrankYao"][str(contest)]=[-2,0]	
	data["cookiecookie"][str(contest)]=[-2,0]		
data["jiancheng2"]['125']=[514,4]	
data["jiancheng2"]['126']=[819,3]		
data["Dengxj"]['126']=[498,3]	
data["vonxq"]['126']=[1131,3]	
	
for contest in range(118,127+1):
	data["sukeyzhou"][str(contest)]=[-2,0]
	data["shuizhouwang"][str(contest)]=[-2,0]	
	data["wangyxwyx"][str(contest)]=[-2,0]
	data["zexingfa"][str(contest)]=[-2,0]						
	

for contest in range(118,128+1):
	data["qz267"][str(contest)]=[-2,0]
	data["Shanshan_Zhang"][str(contest)]=[-2,0]
	data["Arco"][str(contest)]=[-2,0]
	data["user504"][str(contest)]=[-2,0]
	data["Kaiyu-Wang"][str(contest)]=[-2,0]
	data["LindaLyu"][str(contest)]=[-2,0]
	data["liuguanhuaLouie"][str(contest)]=[-2,0]
	data["SummerYang19"][str(contest)]=[-2,0]
	data["whyer"][str(contest)]=[-2,0]
	data["user6745"][str(contest)]=[-2,0]
	data["zhengfu23"][str(contest)]=[-2,0]
	data["abyebye"][str(contest)]=[-2,0]
	data["sijin"][str(contest)]=[-2,0]
	data["Zifengmolan"][str(contest)]=[-2,0]
	data["phoenixpan"][str(contest)]=[-2,0]
	data["WhateverYouSay"][str(contest)]=[-2,0]
	data["OnodaHiro"][str(contest)]=[-2,0]
	data["weiyang95"][str(contest)]=[-2,0]
	data["bingyy"][str(contest)]=[-2,0]
	data["wolf940509"][str(contest)]=[-2,0]
	data["thu_winfield"][str(contest)]=[-2,0]
	data["gyf6434"][str(contest)]=[-2,0]
	data["suzyzhang"][str(contest)]=[-2,0]
data["qz267"]['128']=[2441,2]
data["Arco"]['127']=[653,4]
data["Arco"]['128']=[78,4]
data["OnodaHiro"]['127']=[392,4]
data["OnodaHiro"]['128']=[445,3]
data["thu_winfield"]['128']=[2257,2]
data["suzyzhang"]['127']=[283,4]
data["suzyzhang"]['128']=[102,4]

data["gzh47"]['127']=[-2,0]
data["gzh47"]['128']=[-2,0]


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
contests["126"] = 4564
contests["127"] = 4071
contests["128"] = 5164
contests["129"] = 4325

json_str = json.dumps(contests)

with open('contests.json', 'w') as f:
    json.dump(json_str, f)
    

