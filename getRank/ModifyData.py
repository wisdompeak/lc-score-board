import json
from pprint import pprint

with open('data.json', 'r') as f:
    json_str = json.load(f)
    data = json.loads(json_str)
'''
for contest in range(118,119+1):
	data["zihao"][str(contest)]=[-2,0]	
	data["DorisGe"][str(contest)]=[-2,0]		
	
for contest in range(118,120+1):
	data["user4286"][str(contest)]=[-2,0]
	data["Brooky"][str(contest)]=[-2,0]
	data["yexiaoxiao2102"][str(contest)]=[-2,0]		
	
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
	data["liuguanhualouie"][str(contest)]=[-2,0]
	data["SummerYang19"][str(contest)]=[-2,0]
	data["whyer"][str(contest)]=[-2,0]
	data["user6745"][str(contest)]=[-2,0]
	data["zhengfu23"][str(contest)]=[-2,0]
	data["abyebye"][str(contest)]=[-2,0]
	data["sijin"][str(contest)]=[-2,0]
	data["Zifengmolan"][str(contest)]=[-2,0]
	data["phoenixpan"][str(contest)]=[-2,0]
	data["WhateverYouSay"][str(contest)]=[-2,0]
	data["nagato1208"][str(contest)]=[-2,0]
	data["weiyang95"][str(contest)]=[-2,0]
	data["Bingyy"][str(contest)]=[-2,0]
	data["wolf940509"][str(contest)]=[-2,0]
	data["thu_winfield"][str(contest)]=[-2,0]
	data["gyf6434"][str(contest)]=[-2,0]
	data["suzyzhang"][str(contest)]=[-2,0]
data["qz267"]['128']=[2441,2]
data["Arco"]['127']=[653,4]
data["Arco"]['128']=[78,4]
data["nagato1208"]['127']=[392,4]
data["nagato1208"]['128']=[445,3]
data["weiyang95"]['128']=[809,3]
data["thu_winfield"]['128']=[2257,2]
data["suzyzhang"]['127']=[283,4]
data["suzyzhang"]['128']=[102,4]

data["gzh47"]['127']=[-2,0]
data["gzh47"]['128']=[-2,0]


for contest in range(118,129+1):
	data["ellaliu"][str(contest)]=[-2,0]
	data["leetcodeyu1990"][str(contest)]=[-2,0]
	data["wanyoyo"][str(contest)]=[-2,0]
	data["xguo-Will"][str(contest)]=[-2,0]
	data["ZhengkaiWei"][str(contest)]=[-2,0]
	data["richarddia"][str(contest)]=[-2,0]
	data["cc189"][str(contest)]=[-2,0]
	data["FrankZC"][str(contest)]=[-2,0]
data["Bingyy"]['129']=[-1,0]
data["wanyoyo"]['128']=[417,3]
data["wanyoyo"]['129']=[942,2]
data["xguo-Will"]['128']=[593,3]
data["xguo-Will"]['129']=[529,3]
data["liuguanhualouie"]['129']=[-1,0]
data["liuguanhualouie"]['130']=[-1,0]

for contest in range(118,130+1):
    data["ShangqiYang"][str(contest)]=[-2,0]
    data["clchenliang"][str(contest)]=[-2,0]
    data["Rui_Huang"][str(contest)]=[-2,0]
    data["fu_blue_turkey"][str(contest)]=[-2,0]


for contest in range(118,131+1):
    data["xuyequan"][str(contest)]=[-2,0]
    data["qw123"][str(contest)]=[-2,0]                
for contest in range(128,131+1):    
    data["LittleBaldHead"][str(contest)]=[-2,0] # rejoin


for contest in range(118,132+1):    
    data["mooncaketree"][str(contest)]=[-2,0]
    data["Charlesna"][str(contest)]=[-2,0]
    data["WongBaba"][str(contest)]=[-2,0]
    data["wangzemeng111222"][str(contest)]=[-2,0]
    data["charleszhou327"][str(contest)]=[-2,0]
data["Charlesna"]['131']=[953,4]	
data["shuizhouwang"]['131']=[-2,0]  # rejoin

data["MaggieZhao95"]['133']=[2200,1]	# modify, misuse of account
data["nagato1208"]['129']=[84,4]    # chagne name from OnadaHiro
data["nagato1208"]['130']=[287,4]
data["nagato1208"]['131']=[137,4]
data["nagato1208"]['132']=[555,4]
data["nagato1208"]['133']=[274,4]


for contest in range(118,133+1):  
    data["waitnote"][str(contest)]=[-2,0]
    data["tankztc"][str(contest)]=[-2,0]
    data["mzcj"][str(contest)]=[-2,0]
    data["wxy9018"][str(contest)]=[-2,0]
    data["Cique"][str(contest)]=[-2,0]
    data["FYQiang"][str(contest)]=[-2,0]
    data["bradhuang1999"][str(contest)]=[-2,0]
    data["fighting_for_flag"][str(contest)]=[-2,0]


for contest in range(132,133+1):    
    data["xianglaniunan"][str(contest)]=[-2,0] # rejoin


for contest in range(118,134+1):  
    data["hxin"][str(contest)]=[-2,0]
    data["ddxig"][str(contest)]=[-2,0]
    data["Cicindela"][str(contest)]=[-2,0]
    data["uwelena"][str(contest)]=[-2,0]
    data["dickbomb"][str(contest)]=[-2,0]

for contest in range(123,135+1):  
    data["sissishiny"][str(contest)]=[-2,0]
    data["jpju"][str(contest)]=[-2,0]
    data["kuangwenyi"][str(contest)]=[-2,0]
    data["Hines"][str(contest)]=[-2,0]
    data["baihuajun"][str(contest)]=[-2,0]
    data["yuchenliulyc"][str(contest)]=[-2,0]
    data["winniex0412"][str(contest)]=[-2,0]
    data["aruba1"][str(contest)]=[-2,0]
    

for contest in range(133,135+1):  
	data["bifeitang"][str(contest)]=[-2,0]		# rejoin
data["bifeitang"]['136']=[697,2]	

for contest in range(118,136+1):  
	data["qianchanger"][str(contest)]=[-2,0]
	data["Jc_Qu"][str(contest)]=[-2,0]
	data["Henry_Jiang"][str(contest)]=[-2,0]

data["Rui_Huang"]['136']=[-2,0]		# rejoin

data["ansonluo"]['118']=[1799,1]			
data["ansonluo"]['119']=[556,3]			
data["ansonluo"]['120']=[1622,2]			
data["ansonluo"]['121']=[769,2]
data["ansonluo"]['122']=[-1,0]
data["ansonluo"]['123']=[1353,1]
data["ansonluo"]['124']=[1133,2]
data["ansonluo"]['125']=[1778,2]
data["ansonluo"]['126']=[596,3]
data["ansonluo"]['127']=[1928,3]
data["ansonluo"]['128']=[858,3]
data["ansonluo"]['129']=[924,2]
data["ansonluo"]['130']=[2574,1]
data["ansonluo"]['131']=[-1,0]
data["ansonluo"]['132']=[-1,0]
data["ansonluo"]['133']=[1697,2]
data["ansonluo"]['134']=[1848,1]
data["ansonluo"]['135']=[1193,2]
data["ansonluo"]['136']=[-1,0]

for contest in range(118,137+1):  
    data["zzy1996"][str(contest)]=[-2,0]
    data["thumbpixels"][str(contest)]=[-2,0]
    
for contest in range(125,137+1):  
    data["Duuuuu"][str(contest)]=[-2,0] # rejoin

### before 139
    
for contest in range(118,138+1): 
	data["adayxiang"][str(contest)]=[-2,0]
	data["KatieeeeWang"][str(contest)]=[-2,0]
	data["tift"][str(contest)]=[-2,0]
	data["VectorX"][str(contest)]=[-2,0]
data["VectorX"]['137']=[154,4]	
data["VectorX"]['138']=[158,4]	

### before 140

for contest in range(118,139+1): 
	data["ixinqi"][str(contest)]=[-2,0]
	data["KyleFu"][str(contest)]=[-2,0]
	data["jasonzzzz"][str(contest)]=[-2,0]
	data["clue2gt"][str(contest)]=[-2,0]
	data["sabakunoarashi"][str(contest)]=[-2,0]
	data["liujiashun66"][str(contest)]=[-2,0]
	data["cyn3966"][str(contest)]=[-2,0]
	data["lumic"][str(contest)]=[-2,0]
	data["LZ1994"][str(contest)]=[-2,0]
	data["yuw119"][str(contest)]=[-2,0]
	data["praenubilus"][str(contest)]=[-2,0]
	data["fang2018"][str(contest)]=[-2,0]	
	data["hui1202"][str(contest)]=[-2,0]
	data["liuleo"][str(contest)]=[-2,0]
		
data["IrisGuo"]['118']=[112,4]
data["IrisGuo"]['119']=[164,4]
data["IrisGuo"]['120']=[154,4]
data["IrisGuo"]['121']=[637,3]
data["IrisGuo"]['122']=[142,4]
data["IrisGuo"]['123']=[161,3]
data["IrisGuo"]['124']=[418,3]
data["IrisGuo"]['125']=[269,4]
data["IrisGuo"]['126']=[20,4]
data["IrisGuo"]['127']=[758,4]		
data["IrisGuo"]['128']=[613,3] 
data["IrisGuo"]['129']=[-1,0]
data["IrisGuo"]['130']=[-1,0]
for contest in range(131,139+1): 	 # rejoin
    data["IrisGuo"][str(contest)]=[-2,0]

data["1373757850"]['127']=[2017,2]
data["1373757850"]['128']=[2522,2]
data["1373757850"]['129']=[304,4]
data["1373757850"]['130']=[1644,2]
data["1373757850"]['131']=[1353,3]
data["1373757850"]['132']=[3003,1]
data["1373757850"]['133']=[-1,0]
data["1373757850"]['134']=[1679,1]
data["1373757850"]['135']=[2114,1]
for contest in range(136,139+1): 	 # rejoin
	data["1373757850"][str(contest)]=[-2,0]
		
for contest in range(124,139+1):  
    data["ZhuYamei"][str(contest)]=[-2,0] # rejoin
    data["zpzpzzp2020"][str(contest)]=[-2,0] # rejoin
    		
for contest in range(136,139+1):  
    data["1373757850"][str(contest)]=[-2,0] # rejoin

data["yuw119"]['138']=[232,4]	    
data["yuw119"]['139']=[624,2]


for contest in range(118,132+1): 
   data["stayfoolish2"][str(contest)]=[-2,0]		# change name from dfy8054
data["stayfoolish2"]['133']=[747,3]   
data["stayfoolish2"]['134']=[404,3]
data["stayfoolish2"]['135']=[1176,2]
data["stayfoolish2"]['136']=[1632,1]
data["stayfoolish2"]['137']=[501,3]
data["stayfoolish2"]['138']=[956,3]
data["stayfoolish2"]['139']=[948,2]


### before 141

for contest in range(118,140+1): 
	data["yedi"][str(contest)]=[-2,0]
	data["sequenzf"][str(contest)]=[-2,0]
	data["shuchenc"][str(contest)]=[-2,0]
	data["ljr1226"][str(contest)]=[-2,0]
	data["luorinz"][str(contest)]=[-2,0]
	data["deepda2k"][str(contest)]=[-2,0]
	data["ShoutingLyu"][str(contest)]=[-2,0]
	data["Mengqian"][str(contest)]=[-2,0]
	data["zhifanhui"][str(contest)]=[-2,0]
	data["alex_woods"][str(contest)]=[-2,0]
	data["weidong6686"][str(contest)]=[-2,0]
	data["lanxi619"][str(contest)]=[-2,0]
	data["tocque"][str(contest)]=[-2,0]
	data["davidluoyes"][str(contest)]=[-2,0]
	
### before 142	
for contest in range(118,141+1): 
	data["Lawrence_M"][str(contest)]=[-2,0]
	data["zgcmx2011"][str(contest)]=[-2,0]
	data["shuoyan"][str(contest)]=[-2,0]
	
### before 143		
for contest in range(118,142+1): 
	data["qingqi_lei"][str(contest)]=[-2,0]
	data["timFan"][str(contest)]=[-2,0]
	data["wangru1994305"][str(contest)]=[-2,0]
for contest in range(132,142+1):  
    data["JackTheBest"][str(contest)]=[-2,0] # rejoin    
    
### before 144		
for contest in range(118,143+1): 
	data["tesla_pp"][str(contest)]=[-2,0]
	data["mangoman"][str(contest)]=[-2,0]
	data["litian220"][str(contest)]=[-2,0]
	data["yunfanyi"][str(contest)]=[-2,0]
	data["superflb"][str(contest)]=[-2,0]
	data["coder001"][str(contest)]=[-2,0]
	data["wenting95"][str(contest)]=[-2,0]  
for contest in range(135,143+1):  
    data["yueb95"][str(contest)]=[-2,0] # rejoin 

### before 145	
for contest in range(118,144+1): 
	data["xhou0540"][str(contest)]=[-2,0]
	data["Dawnren123"][str(contest)]=[-2,0]
	data["song30"][str(contest)]=[-2,0]
	data["zac44"][str(contest)]=[-2,0]
	
### before 146
for contest in range(118,145+1): 
	data["sifangyou"][str(contest)]=[-2,0]
	data["mrtong_liu"][str(contest)]=[-2,0]
	data["Sakamono"][str(contest)]=[-2,0]
	data["miracleyanyu"][str(contest)]=[-2,0]
	data["myc9799"][str(contest)]=[-2,0]
for contest in range(144,145+1):  
    data["zpzpzzp2020"][str(contest)]=[-2,0] # rejoin 	


### before 147
for contest in range(118,146+1): 
	data["Wenhuaa"][str(contest)]=[-2,0]
	data["crumbbb"][str(contest)]=[-2,0]
	data["Sakamono"][str(contest)]=[-2,0]
	data["zerotrac2"][str(contest)]=[-2,0]
	data["ChenDanni"][str(contest)]=[-2,0]
	
### before 148
for contest in range(118,147+1): 
	data["KMAGYOYO"][str(contest)]=[-2,0]
	data["clu9"][str(contest)]=[-2,0]
	data["nanjers"][str(contest)]=[-2,0]
	data["Jessi_zxy"][str(contest)]=[-2,0]
	data["zhu_irse"][str(contest)]=[-2,0]
	
### before 149
for contest in range(118,148+1): 
	data["tommyjiang"][str(contest)]=[-2,0]
	data["redbeanlyx"][str(contest)]=[-2,0]
	data["liuchanglouisa"][str(contest)]=[-2,0]
	data["exquisitetaste"][str(contest)]=[-2,0]
	data["wangzi6147"][str(contest)]=[-2,0]		
	data["XiaojingHu"][str(contest)]=[-2,0]		
	
### before 150
for contest in range(118,149+1): 
	data["ZhiWei_Shi"][str(contest)]=[-2,0]
	data["l90095z"][str(contest)]=[-2,0]
	data["latioshuang"][str(contest)]=[-2,0]
	data["Erwin_Ke"][str(contest)]=[-2,0]
	data["gingerale"][str(contest)]=[-2,0]		
	data["LijianChen"][str(contest)]=[-2,0]	
for contest in range(143,149+1):  
    data["thu_winfield"][str(contest)]=[-2,0] # rejoin 	


### before 151
for contest in range(118,150+1): 
	data["sunxiaohua"][str(contest)]=[-2,0]
	data["lucas0316"][str(contest)]=[-2,0]


### before 152
for contest in range(118,151+1): 
	data["UltraShieldRog"][str(contest)]=[-2,0]
	data["qiuyu_93"][str(contest)]=[-2,0]
	data["ping999"][str(contest)]=[-2,0]
	data["fengw7"][str(contest)]=[-2,0]
	data["Captain_Mushroom"][str(contest)]=[-2,0]
	data["Marlon2102win"][str(contest)]=[-2,0]
	data["zhengkai2001"][str(contest)]=[-2,0]
	data["OTTFF"][str(contest)]=[-2,0]						
	data["Journey_Long"][str(contest)]=[-2,0]					
	data["TinyExplorer"][str(contest)]=[-2,0]	


### before 153
for contest in range(118,152+1): 
	data["angel30818"][str(contest)]=[-2,0]
	data["XiaoWanLINJU"][str(contest)]=[-2,0]
	data["sequenzf"][str(contest)]=[-2,0]
	data["coutPKprintf"][str(contest)]=[-2,0]
	data["jwang89225"][str(contest)]=[-2,0]
	data["onionpork"][str(contest)]=[-2,0]
	data["hhjkkl"][str(contest)]=[-2,0]
	data["JIEeee"][str(contest)]=[-2,0]
	data["BingleLove"][str(contest)]=[-2,0]

### before 154
for contest in range(118,153+1): 
	data["wenyou"][str(contest)]=[-2,0]
	data["albertzhang86"][str(contest)]=[-2,0]
	data["ZaozaoNan"][str(contest)]=[-2,0]
	data["Olala_michelle"][str(contest)]=[-2,0]
	data["jason_wong1"][str(contest)]=[-2,0]
	data["Elsie_jiayou"][str(contest)]=[-2,0]
	data["machaohcun"][str(contest)]=[-2,0]
	data["ywxkxcy"][str(contest)]=[-2,0]
	
### before 155
for contest in range(118,154+1): 	
	data["disinuo"][str(contest)]=[-2,0]	
	data["JansonLu"][str(contest)]=[-2,0]
	data["wAgChen"][str(contest)]=[-2,0]
	data["zlpmichelle"][str(contest)]=[-2,0]
data["disinuo"]["153"]=[1925,2]
data["disinuo"]["154"]=[947,3]
		    

### before 156
for contest in range(118,155+1): 	
	data["zlpmichelle"][str(contest)]=[-2,0]	
	data["jpju"][str(contest)]=[-2,0]
	data["Vendettathee"][str(contest)]=[-2,0]
	data["wendy_sun"][str(contest)]=[-2,0]
for contest in range(138,155+1):  
    data["dickbomb"][str(contest)]=[-2,0] # rejoin 		

### before 157
for contest in range(118,156+1): 	
	data["iwfahalfbloodunicorn"][str(contest)]=[-2,0]	
	data["qingdu_river"][str(contest)]=[-2,0]
	data["WendiLiu"][str(contest)]=[-2,0]
	data["fan_zh"][str(contest)]=[-2,0]
	data["SUPERJOSY"][str(contest)]=[-2,0]
	data["dennanisny"][str(contest)]=[-2,0]
	
### before 158
for contest in range(118,157+1): 	
	data["annaluciaa"][str(contest)]=[-2,0]	
	data["yaochou1995"][str(contest)]=[-2,0]
	data["nicole_Song"][str(contest)]=[-2,0]
	data["fengzhixiao"][str(contest)]=[-2,0]
	
### before 159
for contest in range(118,158+1): 	
	data["tichen47"][str(contest)]=[-2,0]	
	data["WarriorZ"][str(contest)]=[-2,0]
	data["JamesCool"][str(contest)]=[-2,0]
	data["Rayleigh0328"][str(contest)]=[-2,0]	
for contest in range(134,158+1):  
    data["KyleFu"][str(contest)]=[-2,0] # rejoin 	
for contest in range(143,158+1):  
    data["zhifanhui"][str(contest)]=[-2,0] # rejoin 	
data["SUPERJOSY"]["159"] = [3852, 1]

### before 160
for contest in range(118,159+1): 	
	data["Rayleigh0328"][str(contest)]=[-2,0]	
	data["chuw"][str(contest)]=[-2,0]
	data["FlagIsMine"][str(contest)]=[-2,0]
	data["RedWolf"][str(contest)]=[-2,0]
	data["endlesscheng"][str(contest)]=[-2,0]	

### before 161
for contest in range(118,160+1): 	
	data["xxz-leetcode"][str(contest)]=[-2,0]	
	data["hongrubb"][str(contest)]=[-2,0]
for contest in range(156,160+1):  
    data["leoknuth"][str(contest)]=[-2,0] # rejoin 
    
    
### before 162
for contest in range(145,161+1):  
    data["cc189"][str(contest)]=[-2,0] # rejoin 
    
### before 163
for contest in range(118,162+1):  
    data["YuhanWu"][str(contest)]=[-2,0]    
    data["zmz666"][str(contest)]=[-2,0]
    data["wdyfy317138"][str(contest)]=[-2,0]
    data["WKelvinson"][str(contest)]=[-2,0]
    data["YutingLiu"][str(contest)]=[-2,0]
    data["blackp1nk"][str(contest)]=[-2,0]
for contest in range(138,162+1):  
    data["got7amy"][str(contest)]=[-2,0] # rejoin 
for contest in range(146,162+1):  
    data["user760"][str(contest)]=[-2,0] # rejoin 
data["OneDirection"]["163"]=[1457,2]  # manual record

### before 164
for contest in range(118,163+1): 
	data["greeneyes"][str(contest)]=[-2,0]    

### before 165
for contest in range(118,164+1): 
	data["concussion"][str(contest)]=[-2,0]   
for contest in range(157,164+1):  
    data["sequenzf"][str(contest)]=[-2,0] # rejoin 	

### before 166
for contest in range(118,165+1): 
	data["hongchenjack"][str(contest)]=[-2,0]  
	data["Yiyue15"][str(contest)]=[-2,0]  
	data["anhpp"][str(contest)]=[-2,0]   

### before 167
for contest in range(118,166+1): 
	data["LambertTao"][str(contest)]=[-2,0]  
	data["xcao65"][str(contest)]=[-2,0] 
for contest in range(161,166+1):  
    data["iwfahalfbloodunicorn"][str(contest)]=[-2,0] # rejoin 	
for contest in range(163,166+1):  
    data["dickbomb"][str(contest)]=[-2,0] # rejoin 	

### before 168    			
for contest in range(118,167+1): 
	data["shangxy"][str(contest)]=[-2,0] 
	data["yanyafeng"][str(contest)]=[-2,0] 
	data["hialvin"][str(contest)]=[-2,0] 
	data["Shirley-lan"][str(contest)]=[-2,0] 
for contest in range(124,167+1):  
    data["Lisanaaa"][str(contest)]=[-2,0] # rejoin 	

### before 169
for contest in range(118,168+1): 
	data["christine_christine"][str(contest)]=[-2,0] 
	data["xinchao0509"][str(contest)]=[-2,0] 
	data["insomniacat"][str(contest)]=[-2,0] 
	data["lilllllllll"][str(contest)]=[-2,0] 
	data["chongtan111200"][str(contest)]=[-2,0] 
	
### before 170
for contest in range(118,169+1): 
	data["luozj14"][str(contest)]=[-2,0] 
	data["overloading"][str(contest)]=[-2,0] 
	data["huanglanzhiguan"][str(contest)]=[-2,0] 
	data["0000alex1111"][str(contest)]=[-2,0] 
	data["lihao199408"][str(contest)]=[-2,0]
	data["LuckyHoungLeee"][str(contest)]=[-2,0]
for contest in range(167,169+1):  
    data["fengw7"][str(contest)]=[-2,0] # rejoin 	
for contest in range(153,169+1):  
    data["venico19"][str(contest)]=[-2,0] # rejoin 	
	
### before 171
for contest in range(118,170+1): 
	data["bugattiforsamsam"][str(contest)]=[-2,0] 
	data["susususueeeeeee"][str(contest)]=[-2,0] 
	data["Achilles_M"][str(contest)]=[-2,0] 
	data["cindywmiao"][str(contest)]=[-2,0] 
	data["PHISSTOOD"][str(contest)]=[-2,0]
	data["lostleaf"][str(contest)]=[-2,0]
	data["emmm_"][str(contest)]=[-2,0]
	data["chenhaomaiji"][str(contest)]=[-2,0]
	data["KurosuHa"][str(contest)]=[-2,0]
	data["Blue_Epoch"][str(contest)]=[-2,0]
	data["yuhengc2"][str(contest)]=[-2,0]
	data["miguelmac"][str(contest)]=[-2,0]
for contest in range(167,170+1):  
    data["zpzpzzp2020"][str(contest)]=[-2,0] # rejoin 	
for contest in range(164,170+1):  
    data["zhengfu23"][str(contest)]=[-2,0] # rejoin     
for contest in range(166,170+1):  
    data["sunxiaohua"][str(contest)]=[-2,0] # rejoin    		
for contest in range(142,170+1):  
    data["ZhuYamei"][str(contest)]=[-2,0] # rejoin  	

### before 172
for contest in range(118,171+1): 
	data["kealyn"][str(contest)]=[-2,0] 
	data["lichunzhu"][str(contest)]=[-2,0] 
	data["bbbblues"][str(contest)]=[-2,0] 
	data["G_lory"][str(contest)]=[-2,0] 
	data["Isomorphic"][str(contest)]=[-2,0] 
	data["infmount"][str(contest)]=[-2,0] 
	data["zzhong511"][str(contest)]=[-2,0] 
	data["freemanzhang"][str(contest)]=[-2,0] 
	data["Neo_Chen"][str(contest)]=[-2,0] 	
	data["user7194i"][str(contest)]=[-2,0]
	data["lzl124631x"][str(contest)]=[-2,0] 
for contest in range(169,171+1):  		
	data["dickbomb"][str(contest)]=[-2,0] # rejoin 
for contest in range(161,171+1):  		
	data["tichen47"][str(contest)]=[-2,0] # rejoin 
for contest in range(169,171+1):  		
	data["sequenzf"][str(contest)]=[-2,0] # rejoin 			
	
	
### before 173
for contest in range(118,172+1): 
	data["lzl124631x"][str(contest)]=[-2,0] 
	data["sunhui"][str(contest)]=[-2,0] 
	data["harttle"][str(contest)]=[-2,0] 
	data["Jony_Cho"][str(contest)]=[-2,0] 
	data["CrhnbP"][str(contest)]=[-2,0] 
	data["JerryHaMa"][str(contest)]=[-2,0] 

### before 174
for contest in range(118,173+1): 
	data["notfxt"][str(contest)]=[-2,0] 
	data["Kerathy"][str(contest)]=[-2,0] 
	data["wangchuqiao93"][str(contest)]=[-2,0] 
	data["Jony_Cho"][str(contest)]=[-2,0] 
	data["obihai"][str(contest)]=[-2,0] 
for contest in range(170,173+1):  		
	data["ShangqiYang"][str(contest)]=[-2,0] # rejoin 
for contest in range(134,173+1):  		
	data["Kaiyu-Wang"][str(contest)]=[-2,0] # rejoin 	


### before 175
for contest in range(118,174+1): 
	data["laikwunsing"][str(contest)]=[-2,0] 
	data["biss"][str(contest)]=[-2,0] 
	data["ZihaoXue1995"][str(contest)]=[-2,0] 
	data["Zoe_Du"][str(contest)]=[-2,0] 
	data["VanCN"][str(contest)]=[-2,0]
	data["aChris"][str(contest)]=[-2,0]
	data["BlinkBamboo"][str(contest)]=[-2,0]
	data["YanJF"][str(contest)]=[-2,0]
	data["2valor"][str(contest)]=[-2,0] 
for contest in range(167,174+1):  		
	data["Dawnren123"][str(contest)]=[-2,0] # rejoin 
for contest in range(174,174+1):  		
	data["machaohcun"][str(contest)]=[-2,0] # rejoin 

data["Zoe_Du"]['175']=[5682,1]
data["LuckyHoungLeee"]['175']=[5045,2] 


### before 176
for contest in range(118,175+1): 
	data["oOoO0oOoO0oOo"][str(contest)]=[-2,0]
	data["thewisp"][str(contest)]=[-2,0]
	data["FighterNan"][str(contest)]=[-2,0]
	data["allen980123"][str(contest)]=[-2,0]
	data["BestQian"][str(contest)]=[-2,0]
	data["yanrucheng"][str(contest)]=[-2,0] 
	data["gabyXuan"][str(contest)]=[-2,0]
	data["kid1412z"][str(contest)]=[-2,0]
	data["aruhanliu2"][str(contest)]=[-2,0]
	data["user7687"][str(contest)]=[-2,0]
	data["Juny1He"][str(contest)]=[-2,0]
	data["lozy219"][str(contest)]=[-2,0]
for contest in range(174,175+1):  		
	data["aruba1"][str(contest)]=[-2,0] # rejoin 

### before 177
for contest in range(118,176+1): 
	data["Imma007"][str(contest)]=[-2,0]
	data["YI-DING"][str(contest)]=[-2,0]
	data["Ethan_M"][str(contest)]=[-2,0]
	data["alycia"][str(contest)]=[-2,0]
	data["ChelsieZ"][str(contest)]=[-2,0]
for contest in range(168,176+1):  		
	data["ChenDanni"][str(contest)]=[-2,0] # rejoin 

### before 178
for contest in range(118,177+1): 
	data["renjunyao"][str(contest)]=[-2,0]
	data["VivianVVang"][str(contest)]=[-2,0]
	data["Coup_De_Grace"][str(contest)]=[-2,0]
	data["tt198866"][str(contest)]=[-2,0]
	data["halolong"][str(contest)]=[-2,0]
	data["jxu349"][str(contest)]=[-2,0]
for contest in range(175,177+1):  		
	data["greeneyes"][str(contest)]=[-2,0] # rejoin 
for contest in range(133,177+1):  		
	data["supersam331"][str(contest)]=[-2,0] # rejoin 

### before 179
for contest in range(118,178+1): 
	data["Allllll"][str(contest)]=[-2,0]

### before 180
for contest in range(118,179+1): 
	data["ziyezhu92"][str(contest)]=[-2,0]
	data["jerryxyj289"][str(contest)]=[-2,0]
	data["nliu_l"][str(contest)]=[-2,0]
	data["meiyiyan"][str(contest)]=[-2,0]
for contest in range(176,179+1):  		
	data["Yiyue15"][str(contest)]=[-2,0] # rejoin 

### before 181
for contest in range(118,180+1): 
	data["hptcyhj"][str(contest)]=[-2,0]
	data["hw2020"][str(contest)]=[-2,0]
	data["YuchenYang1997"][str(contest)]=[-2,0]
	data["ShidaLei"][str(contest)]=[-2,0]
	data["Yao_Yin"][str(contest)]=[-2,0]
	data["zyw_code"][str(contest)]=[-2,0]
	data["deadstorm"][str(contest)]=[-2,0]
	data["chenjianxu97"][str(contest)]=[-2,0]
	data["michelle_sima"][str(contest)]=[-2,0]
	data["CE_RE_WAyitiaolong"][str(contest)]=[-2,0]
for contest in range(180,180+1):  		
	data["Kerathy"][str(contest)]=[-2,0] # rejoin 	
for contest in range(177,180+1):  		
	data["Charles000"][str(contest)]=[-2,0] # rejoin 		

### before 182
for contest in range(118,181+1): 
	data["wang2019"][str(contest)]=[-2,0]	
	data["YoungForest"][str(contest)]=[-2,0]	
	data["kylelovealgo"][str(contest)]=[-2,0]	
	data["lishichengyan"][str(contest)]=[-2,0]	
	data["ruanys"][str(contest)]=[-2,0]	
	data["scarlett_jl"][str(contest)]=[-2,0]	
	data["klutzCoder"][str(contest)]=[-2,0]	
	data["Xingdong_Cao"][str(contest)]=[-2,0]	
	data["Malik-Jia"][str(contest)]=[-2,0]	
	data["besieger"][str(contest)]=[-2,0]	

### before 183
for contest in range(118,182+1): 
	data["jwang89225"][str(contest)]=[-2,0]	
	data["coding_meowmeow"][str(contest)]=[-2,0]	
	data["fanzhh"][str(contest)]=[-2,0]	
	data["ddwysg1"][str(contest)]=[-2,0]	
	data["larui529"][str(contest)]=[-2,0]	
	data["zhongqusc"][str(contest)]=[-2,0]	
	data["dalaobi"][str(contest)]=[-2,0]	
	data["homily707"][str(contest)]=[-2,0]	
	data["Xiuyang"][str(contest)]=[-2,0]	
for contest in range(181,182+1):  		
	data["WKelvinson"][str(contest)]=[-2,0] # rejoin 	
for contest in range(166,182+1):  		
	data["TOYAMA_NAO"][str(contest)]=[-2,0] # rejoin 
for contest in range(153,182+1):  		
	data["liuleo"][str(contest)]=[-2,0] # rejoin 		

### before 184
for contest in range(118,183+1): 
	data["Lawliet890"][str(contest)]=[-2,0]	
	data["zyzz1234"][str(contest)]=[-2,0]	
	data["hssrut"][str(contest)]=[-2,0]	
	data["alanlzl"][str(contest)]=[-2,0]	
	data["axiu777"][str(contest)]=[-2,0]	
for contest in range(178,183+1):  		
	data["KurosuHa"][str(contest)]=[-2,0] # rejoin 		


### before 185
for contest in range(118,184+1): 
	data["pku_erutan"][str(contest)]=[-2,0]	
	data["skierlin"][str(contest)]=[-2,0]	
	data["codingmushroom"][str(contest)]=[-2,0]	
	data["keepswimming"][str(contest)]=[-2,0]	
	data["sxd32550"][str(contest)]=[-2,0]	
data["jasonzzzz"]["185"]=[2133,3]		# rename
data["zpzpzzp2020"]["185"]=[2705,3]		# rename

### before 186
for contest in range(118,185+1): 
	data["Hangzhi"][str(contest)]=[-2,0]	
	data["derekW"][str(contest)]=[-2,0]	
	data["Jtx_"][str(contest)]=[-2,0]	
	data["lwh14710"][str(contest)]=[-2,0]	
	data["LyannaGoGoGo"][str(contest)]=[-2,0]	

### before 187
for contest in range(118,186+1): 
	data["leileimiao"][str(contest)]=[-2,0]	
	data["pjequilibrium"][str(contest)]=[-2,0]	
	data["izhongyuting"][str(contest)]=[-2,0]	
	data["swift9"][str(contest)]=[-2,0]	
for contest in range(185,186+1):  		
	data["zerotrac2"][str(contest)]=[-2,0] # rejoin 	


### before 188
data["Chrisify"]=data["aChris"]
data.pop("aChris")
data["ddoudle"]=data["Xingdong_Cao"]
data.pop("Xingdong_Cao")
data["lance_skier"]=data["skierlin"]
data.pop("skierlin")
for contest in range(118,187+1): 
	data["wenjun_gael"][str(contest)]=[-2,0]	
	data["edisonnie"][str(contest)]=[-2,0]	
	data["xywang0520"][str(contest)]=[-2,0]	
	data["arignote"][str(contest)]=[-2,0]	
for contest in range(184,187+1):  		
	data["sequenzf"][str(contest)]=[-2,0] # rejoin 

## before 189
for contest in range(118,188+1): 
	data["Googlehsieh"][str(contest)]=[-2,0]	
for contest in range(162,188+1):  		
	data["JamesCool"][str(contest)]=[-2,0] # rejoin 
for contest in range(169,188+1):  		
	data["MaggieZhao95"][str(contest)]=[-2,0] # rejoin 
for contest in range(172,188+1):  		
	data["Mengqian"][str(contest)]=[-2,0] # rejoin 

## before 190
for contest in range(118,189+1): 
	data["cindy199707"][str(contest)]=[-2,0]	
	data["haimingz112"][str(contest)]=[-2,0]
	data["457368837"][str(contest)]=[-2,0]
	data["zzh372024750"][str(contest)]=[-2,0]
for contest in range(181,189+1):  		
	data["dickbomb"][str(contest)]=[-2,0] # rejoin 
for contest in range(183,189+1):  		
	data["BestQian"][str(contest)]=[-2,0] # rejoin 

## before 191
for contest in range(118,190+1): 
	data["cyn3966"][str(contest)]=[-2,0]	
	data["htkzmo"][str(contest)]=[-2,0]
	data["Luna_Zhang26"][str(contest)]=[-2,0]
for contest in range(187,190+1):  		
	data["zhu_irse"][str(contest)]=[-2,0] # rejoin 
for contest in range(170,190+1):  		
	data["Journey_Long"][str(contest)]=[-2,0] # rejoin 

## before 192
for contest in range(118,191+1): 
	data["zebox"][str(contest)]=[-2,0]	
	data["huangyuyang"][str(contest)]=[-2,0]
	data["wangyxwyx"][str(contest)]=[-2,0]
	data["davidguuuo"][str(contest)]=[-2,0]

## before 193
for contest in range(174,192+1):  		
	data["user760"][str(contest)]=[-2,0] # rejoin 

## before 195
for contest in range(118,194+1):  		
	data["chaoqin-li"][str(contest)]=[-2,0] 
	data["Khan_2020"][str(contest)]=[-2,0]
for contest in range(183,194+1):  
	data["Neo_Chen"][str(contest)]=[-2,0]	# rejoin 	
for contest in range(188,194+1):  
	data["YanJF"][str(contest)]=[-2,0]	# rejoin 	
for contest in range(187,194+1):  
	data["Duuuuu"][str(contest)]=[-2,0]	# rejoin 
for contest in range(135,194+1):  
	data["huyouhyw"][str(contest)]=[-2,0]	# rejoin 

## before 196
for contest in range(118,195+1):  		
	data["YaoyaoChang"][str(contest)]=[-2,0] 
	data["nanotrt2333"][str(contest)]=[-2,0]

## before 197
for contest in range(118,196+1):  		
	data["alsvia"][str(contest)]=[-2,0] 
	data["jamesfan1101"][str(contest)]=[-2,0]
	data["lbyxiafei"][str(contest)]=[-2,0]
	data["darkaimagic"][str(contest)]=[-2,0]

## before 198
for contest in range(118,197+1):  		
	data["LeetCoding_Master"][str(contest)]=[-2,0] 
	data["shuijian7"][str(contest)]=[-2,0]
	data["tiandaliu"][str(contest)]=[-2,0]
	data["crystalmiumiu"][str(contest)]=[-2,0]
	data["Silver_Blade"][str(contest)]=[-2,0]
	data["yinjun"][str(contest)]=[-2,0]
	data["lisy14"][str(contest)]=[-2,0]
for contest in range(186,197+1):  		
	data["kylelovealgo"][str(contest)]=[-2,0] # rejoin 	

## before 199
for contest in range(118,198+1):  	
	data["wcy23"][str(contest)]=[-2,0]
for contest in range(185,198+1):  		
	data["fengw7"][str(contest)]=[-2,0] # rejoin 	
for contest in range(193,198+1):  		
	data["yiyue15"][str(contest)]=[-2,0] # rejoin 		

## before 201
for contest in range(118,200+1):  	
	data["buffa"][str(contest)]=[-2,0]
	data["shenshun"][str(contest)]=[-2,0]
	data["X_Chen6"][str(contest)]=[-2,0]

for contest in range(194,200+1):  		
	data["FightEveryDay"][str(contest)]=[-2,0] # rejoin 

## before 202
for contest in range(118,201+1):  	
	data["ilovejunghyun"][str(contest)]=[-2,0]
	data["JDEP"][str(contest)]=[-2,0]
	data["mayintong"][str(contest)]=[-2,0]
for contest in range(199,201+1):  		
	data["laikwunsing"][str(contest)]=[-2,0] # rejoin 	

## before 203
for contest in range(118,202+1):  	
	data["youjiahan"][str(contest)]=[-2,0]
for contest in range(186,202+1):  	
	data["WKelvinson"][str(contest)]=[-2,0] # rejoin
for contest in range(193,202+1):  	
	data["chenhaomaiji"][str(contest)]=[-2,0] # rejoin	

## before 204
for contest in range(195,203+1):  	
	data["zebox"][str(contest)]=[-2,0]  # rejoin
for contest in range(193,203+1):  	
	data["wenyou"][str(contest)]=[-2,0] # rejoin
for contest in range(188,203+1):  	
	data["Charles000"][str(contest)]=[-2,0] # rejoin	
for contest in range(194,203+1):  	
	data["wang2019"][str(contest)]=[-2,0] # rejoin	

## before 205
for contest in range(118,204+1):  	
	data["NuozhouXu"][str(contest)]=[-2,0]
	data["ShizukaYee"][str(contest)]=[-2,0]
	data["ScottCC"][str(contest)]=[-2,0]
	data["Castling"][str(contest)]=[-2,0]
	data["OliverGates"][str(contest)]=[-2,0]
	data["am0320"][str(contest)]=[-2,0]

## before 206
for contest in range(118,205+1):  	
	data["tigermlt"][str(contest)]=[-2,0]
	data["pku-zbt"][str(contest)]=[-2,0]

## before 207
for contest in range(118,206+1):  	
	data["monaziyi"][str(contest)]=[-2,0]
	data["yi-zhi-xiao-ruo-ji"][str(contest)]=[-2,0]
	data["wwwap"][str(contest)]=[-2,0]
	data["bill04128682"][str(contest)]=[-2,0]
	data["yangshaoqian111"][str(contest)]=[-2,0]
	data["qwerjkl112"][str(contest)]=[-2,0]
	data["lichenz"][str(contest)]=[-2,0]
	data["homily707"][str(contest)]=[-2,0]
	data["mcuallen"][str(contest)]=[-2,0]
	data["lichenz"][str(contest)]=[-2,0]
for contest in range(164,206+1):  	
	data["nanjers"][str(contest)]=[-2,0] # rejoin	
for contest in range(205,206+1):  	
	data["jamesfan1101"][str(contest)]=[-2,0] # rejoin	
for contest in range(183,206+1):  	
	data["please_AC"][str(contest)]=[-2,0] # rejoin		

## before 208
for contest in range(118,207+1):  	
	data["zhangsz1998"][str(contest)]=[-2,0]
	data["xiapengchng"][str(contest)]=[-2,0]
	data["Arsenal-591"][str(contest)]=[-2,0]
data["Arsenal-591"]["208"]=[492,4]
data["yi-zhi-xiao-ruo-ji"]["208"]=[780,4]

## before 209
for contest in range(118,208+1):  	
	data["FreshBing"][str(contest)]=[-2,0]
for contest in range(179,208+1):  	
	data["BlinkBamboo"][str(contest)]=[-2,0] # rejoin	

## before 210
for contest in range(118,209+1):  	
	data["li-jinze"][str(contest)]=[-2,0]
	data["woshilxd912"][str(contest)]=[-2,0]

## before 211
for contest in range(118,210+1):  	
	data["mengmoya"][str(contest)]=[-2,0]
	data["hanzhoutang"][str(contest)]=[-2,0]
	data["keepPace"][str(contest)]=[-2,0]
	data["lynnnaive16"][str(contest)]=[-2,0]
	data["zgtmy"][str(contest)]=[-2,0]
	data["forresty"][str(contest)]=[-2,0]
	data["lilydenris"][str(contest)]=[-2,0]
for contest in range(207,210+1):  	
	data["huangyuyang"][str(contest)]=[-2,0] # rejoin		

## before 212
for contest in range(118,211+1):  	
	data["vRussell"][str(contest)]=[-2,0]
	data["wenyu3"][str(contest)]=[-2,0]

## before 213
for contest in range(118,212+1):  	
	data["Courtmouse"][str(contest)]=[-2,0]
	data["ruofeisan"][str(contest)]=[-2,0]
	data["YangXiYi"][str(contest)]=[-2,0]
	data["ChenQuanWei7"][str(contest)]=[-2,0]
for contest in range(209,212+1):  	
	data["tigermlt"][str(contest)]=[-2,0] # rejoin	

## before 214
for contest in range(118,213+1):  	
	data["tsunamixiao"][str(contest)]=[-2,0]
	data["hongleyou"][str(contest)]=[-2,0]
	data["skd233"][str(contest)]=[-2,0]

## before 215
for contest in range(118,214+1):  	
	data["EdmizJay"][str(contest)]=[-2,0]

## before 216
for contest in range(118,215+1):  	
	data["maoyp"][str(contest)]=[-2,0]
	data["yinghuahu"][str(contest)]=[-2,0]
	data["lighteningzhang"][str(contest)]=[-2,0]
for contest in range(206,215+1):  	
	data["chenjianxu97"][str(contest)]=[-2,0] # rejoin	

## before 217
for contest in range(118,216+1):  	
	data["wxhelloworld"][str(contest)]=[-2,0]

## before 218
for contest in range(118,217+1):  	
	data["Byleth"][str(contest)]=[-2,0]
	

## before 219
for contest in range(118,218+1):  	
	data["ryoyukiyangy"][str(contest)]=[-2,0]	
	data["rqren2018"][str(contest)]=[-2,0]
for contest in range(215,218+1):  	
	data["BlinkBamboo"][str(contest)]=[-2,0] # rejoin

## before 220
for contest in range(118,219+1):  	
	data["jiutiany1127"][str(contest)]=[-2,0]
for contest in range(202,219+1):  	
	data["0000alex1111"][str(contest)]=[-2,0] # rejoin

## before 222
for contest in range(118,219+1):  	
	data["fuchengshun"][str(contest)]=[-2,0]
	data["wan-catherine"][str(contest)]=[-2,0]
	data["xyzzzzzzzz"][str(contest)]=[-2,0]
	data["rayms"][str(contest)]=[-2,0]
	data["klutzCoder"][str(contest)]=[-2,0]
	data["z1m"][str(contest)]=[-2,0]
	data["window0105"][str(contest)]=[-2,0]
	data["hc167"][str(contest)]=[-2,0]

## before 223
for contest in range(118,222+1):  	
	data["jja725"][str(contest)]=[-2,0]
	data["stevenhuang42195"][str(contest)]=[-2,0]
	data["changyu_jiang"][str(contest)]=[-2,0]
	data["FunBam"][str(contest)]=[-2,0]
	data["ddddyliu"][str(contest)]=[-2,0]
	data["apoi2333"][str(contest)]=[-2,0]
	data["zk299"][str(contest)]=[-2,0]
	data["chrisdzxu"][str(contest)]=[-2,0]
	data["33sharewithu"][str(contest)]=[-2,0]
	data["ShizukaYee"][str(contest)]=[-2,0]
	data["wqql"][str(contest)]=[-2,0]
	data["Alkyl"][str(contest)]=[-2,0]
	data["ruifeng"][str(contest)]=[-2,0]
for contest in range(221,222+1):  	
	data["wenyou"][str(contest)]=[-2,0] # rejoin
for contest in range(217,222+1):  	
	data["jamesfan1101"][str(contest)]=[-2,0] # rejoin
data["tangere"]['223']=[929,3]

## before 224
for contest in range(118,223+1):  	
	data["axjin"][str(contest)]=[-2,0]
	data["yuanlu0210"][str(contest)]=[-2,0]
	data["nickee1942"][str(contest)]=[-2,0]
	data["home_z"][str(contest)]=[-2,0]
data["tangere"]['223']=[929,3]	

## before 225
for contest in range(118,224+1):  	
	data["blackspinner"][str(contest)]=[-2,0]
	data["REED_W"][str(contest)]=[-2,0]
	data["zwang96"][str(contest)]=[-2,0]
	data["sam_lee_"][str(contest)]=[-2,0]
	data["YukiWang"][str(contest)]=[-2,0]
	data["Zhang957"][str(contest)]=[-2,0]
	data["conanjinming"][str(contest)]=[-2,0]
for contest in range(211,224+1):  	
	data["zebox"][str(contest)]=[-2,0] # rejoin
for contest in range(192,224+1):  	
	data["dickbomb"][str(contest)]=[-2,0] # rejoin

## before 226
for contest in range(118,225+1):  	
	data["slurpyFart"][str(contest)]=[-2,0]
	data["Kamikakushi"][str(contest)]=[-2,0]

## before 227
for contest in range(118,226+1):  	
	data["zqsgopyyq"][str(contest)]=[-2,0]

## before 228
for contest in range(118,227+1):  	
	data["y-square"][str(contest)]=[-2,0]
for contest in range(218,227+1):  	
	data["tigermlt"][str(contest)]=[-2,0] # rejoin

## before 229
for contest in range(118,228+1):  	
	data["inucla"][str(contest)]=[-2,0]
	data["ruizhang199509"][str(contest)]=[-2,0]
	data["SDE2018_Carson_Yingying"][str(contest)]=[-2,0]
	data["weeeed"][str(contest)]=[-2,0]
	data["Lunaaaa"][str(contest)]=[-2,0]
	data["puuuuuuuuuuuuu"][str(contest)]=[-2,0]

## before 230
for contest in range(118,229+1):  	
	data["zhenguowcs"][str(contest)]=[-2,0]

## before 231
for contest in range(118,230+1):  	
	data["jja725"][str(contest)]=[-2,0]
	data["bc2615"][str(contest)]=[-2,0]
	data["delphih"][str(contest)]=[-2,0]
for contest in range(221,230+1):  	
	data["htkzmo"][str(contest)]=[-2,0]
for contest in range(208,230+1):  	
	data["wanyoyo"][str(contest)]=[-2,0]	

## before 232
for contest in range(118,231+1): 
	data["deepli"][str(contest)]=[-2,0]
	data["quantuminfo"][str(contest)]=[-2,0]	

## before 233
for contest in range(118,232+1): 
	data["ZhemingX"][str(contest)]=[-2,0]
	data["kstxdy"][str(contest)]=[-2,0]	
	data["sugaruncle1996"][str(contest)]=[-2,0]	
	data["Zoey-ZOU"][str(contest)]=[-2,0]	
	data["songx544"][str(contest)]=[-2,0]	
	data["AmeliaHe98"][str(contest)]=[-2,0]	
	data["yufeng0827"][str(contest)]=[-2,0]	
for contest in range(188,232+1):  	
	data["yuhengc2"][str(contest)]=[-2,0] # rejoin

## before 234
for contest in range(118,233+1): 
	data["ViribusUnitis"][str(contest)]=[-2,0]

## before 235
for contest in range(118,234+1): 
	data["caoboxiao"][str(contest)]=[-2,0]

## before 236
for contest in range(118,235+1): 
	data["TimSYQQX"][str(contest)]=[-2,0]
	data["playfair"][str(contest)]=[-2,0]
for contest in range(190,235+1):  	
	data["KurosuHa"][str(contest)]=[-2,0] # rejoin

## before 237
for contest in range(118,236+1): 
	data["RomainTian"][str(contest)]=[-2,0]
	data["MaskRay"][str(contest)]=[-2,0]
	data["efgonzalez"][str(contest)]=[-2,0]

## before 238
for contest in range(118,237+1): 
	data["nyu_ldf"][str(contest)]=[-2,0]
	data["guyang123"][str(contest)]=[-2,0]
	data["youyou331"][str(contest)]=[-2,0]
	data["SaveThePlanet"][str(contest)]=[-2,0]
	data["luyifan1996"][str(contest)]=[-2,0]
	data["corn2597"][str(contest)]=[-2,0]
	data["hellocici"][str(contest)]=[-2,0]
	data["han3000"][str(contest)]=[-2,0]
	data["guanhao2"][str(contest)]=[-2,0]
for contest in range(228,237+1):  	
	data["WKelvinson"][str(contest)]=[-2,0] # rejoin

## before 239
for contest in range(118,238+1): 
	data["jianghd1996"][str(contest)]=[-2,0]
	data["kesihai"][str(contest)]=[-2,0]
	data["HarrisonShen"][str(contest)]=[-2,0]
	data["bxiao_ca"][str(contest)]=[-2,0]
for contest in range(128,238+1): 
	data["banrenmasanxing"][str(contest)]=[-2,0] # rejoin

## before 240
for contest in range(118,239+1): 
	data["direction"][str(contest)]=[-2,0]
	data["upupming"][str(contest)]=[-2,0]
	data["ryanwong0127"][str(contest)]=[-2,0]
	data["Saiyan_fdy"][str(contest)]=[-2,0]
	data["zxiaoqi1"][str(contest)]=[-2,0]
	data["remfzh"][str(contest)]=[-2,0]
	data["zrts"][str(contest)]=[-2,0]
	data["cozlind"][str(contest)]=[-2,0]
	data["HIT_TOM"][str(contest)]=[-2,0]
	data["NaoJoeMiao"][str(contest)]=[-2,0]
for contest in range(206,239+1): 
	data["LeetCodeSuperman"][str(contest)]=[-2,0] # rejoin
for contest in range(235,239+1): 
	data["insomniacat"][str(contest)]=[-2,0] # rejoin	


## before 241
for contest in range(118,240+1): 
	data["goodstudyqaq"][str(contest)]=[-2,0]
	data["MSY16"][str(contest)]=[-2,0]
	data["bush11"][str(contest)]=[-2,0]
	data["zmxsdu"][str(contest)]=[-2,0]
	data["zzzxxAkir"][str(contest)]=[-2,0]
	data["zhichuan"][str(contest)]=[-2,0]

## before 242
for contest in range(118,241+1): 
	data["Tyrande"][str(contest)]=[-2,0]
	data["ashzzyj"][str(contest)]=[-2,0]
	data["migeater"][str(contest)]=[-2,0]
	data["perry304"][str(contest)]=[-2,0]
	data["universer2009"][str(contest)]=[-2,0]
	data["thinkiny"][str(contest)]=[-2,0]
	data["erds44"][str(contest)]=[-2,0]
	data["WeijieChen0_0"][str(contest)]=[-2,0]
for contest in range(211,241+1): 
	data["Castling"][str(contest)]=[-2,0] # rejoin	
for contest in range(217,241+1): 
	data["lichenz"][str(contest)]=[-2,0] # rejoin	

## before 243
for contest in range(118,242+1): 
	data["tainule"][str(contest)]=[-2,0]
	data["lightmiao"][str(contest)]=[-2,0]
	data["daybreaker678"][str(contest)]=[-2,0]
	data["silvertint10"][str(contest)]=[-2,0]
	data["maobing"][str(contest)]=[-2,0]

## before 244
for contest in range(118,243+1): 
	data["senliu_ac"][str(contest)]=[-2,0]
	data["jozdortraz"][str(contest)]=[-2,0]
	data["marfemale"][str(contest)]=[-2,0]
	data["Ghostk1590"][str(contest)]=[-2,0]
	data["ningziwen"][str(contest)]=[-2,0]
	data["skqliao"][str(contest)]=[-2,0]
for contest in range(230,243+1): 
	data["aChris"][str(contest)]=[-2,0] # rejoin	
for contest in range(241,243+1): 
	data["bill04128682"][str(contest)]=[-2,0] # rejoin		

## before 245
for contest in range(118,244+1): 
	data["ZeRoLJ42"][str(contest)]=[-2,0]
	data["cguo"][str(contest)]=[-2,0]
	data["lianxin_cn"][str(contest)]=[-2,0]
	data["faang2022"][str(contest)]=[-2,0]
for contest in range(167,244+1): 
	data["jzcheng"][str(contest)]=[-2,0] # rejoin	
for contest in range(226,244+1): 
	data["dickbomb"][str(contest)]=[-2,0] # rejoin	

## before 246
for contest in range(118,245+1): 
	data["lih627"][str(contest)]=[-2,0]
	data["shyhaimao"][str(contest)]=[-2,0]
	data["flagamy"][str(contest)]=[-2,0]
	data["meowbawang"][str(contest)]=[-2,0]
	data["weiliang515"][str(contest)]=[-2,0]
	data["Jack_Ma1024"][str(contest)]=[-2,0]
	data["jingwenxxx"][str(contest)]=[-2,0]	
for contest in range(197,245+1): 
	data["wangyxwyx"][str(contest)]=[-2,0] # rejoin	
data["han3000"]["246"]=[637,3]

## before 247
for contest in range(118,246+1): 
	data["LeetCodeForce"][str(contest)]=[-2,0]
	data["huangfq07"][str(contest)]=[-2,0]
	data["Evolut1on"][str(contest)]=[-2,0]
	data["ggggle"][str(contest)]=[-2,0]
	data["hakunamatete"][str(contest)]=[-2,0]
	data["leetcodelibo"][str(contest)]=[-2,0]

## before 248
for contest in range(118,247+1): 
	data["ryanzhang29"][str(contest)]=[-2,0]
	data["zhouxiongjia"][str(contest)]=[-2,0]
	data["SupervisorMayHap"][str(contest)]=[-2,0]

## before 249
for contest in range(118,248+1): 
	data["fangdanzai"][str(contest)]=[-2,0]
	data["M954"][str(contest)]=[-2,0]
for contest in range(246,248+1): 
	data["yuhengc2"][str(contest)]=[-2,0] # rejoin	
for contest in range(141,248+1): 
	data["wyzhang421"][str(contest)]=[-2,0] # rejoin	
for contest in range(195,248+1): 
	data["Yao_Yin"][str(contest)]=[-2,0] # rejoin		

## before 250
for contest in range(118,249+1): 
	data["27rabbitlt"][str(contest)]=[-2,0]
	data["YUFENGWANG"][str(contest)]=[-2,0]
	data["sssssummer"][str(contest)]=[-2,0]

## before 251
for contest in range(118,250+1): 
	data["vanstar123456"][str(contest)]=[-2,0]
	data["whtttth"][str(contest)]=[-2,0]
	data["sirgarfield"][str(contest)]=[-2,0]
	data["yllclover"][str(contest)]=[-2,0]
	data["danielxuforever"][str(contest)]=[-2,0]
	data["bttsv"][str(contest)]=[-2,0]
for contest in range(140,250+1): 
	data["jmzhang18"][str(contest)]=[-2,0] # rejoin	
for contest in range(229,250+1): 
	data["james_fan1101"][str(contest)]=[-2,0] # rejoin	

## before 252
for contest in range(188,251+1): 
	data["liulaoye135"][str(contest)]=[-2,0] # rejoin	

## before 253
for contest in range(118,252+1): 
	data["daojingLeetcode"][str(contest)]=[-2,0]
	data["TRDample"][str(contest)]=[-2,0]
for contest in range(245,252+1): 
	data["MSY16"][str(contest)]=[-2,0] # rejoin	
for contest in range(247,252+1): 
	data["ScottCC"][str(contest)]=[-2,0] # rejoin	
for contest in range(148,252+1): 
	data["KyleAC"][str(contest)]=[-2,0] # rejoin

## before 254
for contest in range(118,253+1): 
	data["LeeShengkai"][str(contest)]=[-2,0]
	data["zzgreen"][str(contest)]=[-2,0]
	data["CharlieZyl"][str(contest)]=[-2,0]
	data["bit3tbb"][str(contest)]=[-2,0]

## before 255
for contest in range(118,254+1): 
	data["xzy19951213"][str(contest)]=[-2,0]
	data["zyg3328"][str(contest)]=[-2,0]
	data["chenzhaojie1997"][str(contest)]=[-2,0]
	data["zjrenivan"][str(contest)]=[-2,0]
	data["Zheng_Four_Oranges"][str(contest)]=[-2,0]
	data["fang_w"][str(contest)]=[-2,0]	
for contest in range(222,254+1): 
	data["yiyue15"][str(contest)]=[-2,0] # rejoin

data["chenzhaojie1997"]["255"]=[2057,2]
data["xzy19951213"]["255"]=[-1,0]
data["zjrenivan"]["255"]=[-1,0]
data["fang_w"]["255"]=[1450,2]
data["Zheng_Four_Oranges"]["255"]=[130,3]	

## before 256
for contest in range(118,255+1): 	
	data["oaixuroab"][str(contest)]=[-2,0]
	data["SteveSunTech"][str(contest)]=[-2,0]	
for contest in range(195,255+1): 
	data["hialvin"][str(contest)]=[-2,0] # rejoin

## before 257
for contest in range(118,256+1): 	
	data["shogunpang"][str(contest)]=[-2,0]
	data["tzsysu"][str(contest)]=[-2,0]	
for contest in range(204,256+1): 
	data["fengw7"][str(contest)]=[-2,0] # rejoin

## before 258
for contest in range(118,257+1): 	
	data["hit_kong"][str(contest)]=[-2,0]
	data["coryking"][str(contest)]=[-2,0]	
	data["wfnuser"][str(contest)]=[-2,0]	
	data["WRWRW"][str(contest)]=[-2,0]	
	data["forever_moon"][str(contest)]=[-2,0]	
	data["linjiale"][str(contest)]=[-2,0]	
for contest in range(219,257+1): 
	data["larui529"][str(contest)]=[-2,0] # rejoin

## before 259
for contest in range(118,258+1): 	
	data["GreatL"][str(contest)]=[-2,0]
	data["nirodha"][str(contest)]=[-2,0]
	data["Juwentus"][str(contest)]=[-2,0]
	data["Hhhoyuu"][str(contest)]=[-2,0]
	data["Biteyou"][str(contest)]=[-2,0]
	data["rookie_my"][str(contest)]=[-2,0]
	data["goldAdventure"][str(contest)]=[-2,0]
	data["XYqqq777"][str(contest)]=[-2,0]
	data["fsyun"][str(contest)]=[-2,0]

## before 260
for contest in range(118,259+1): 	
	data["jiekun"][str(contest)]=[-2,0]
	data["ray_mzy"][str(contest)]=[-2,0]
	data["alicila"][str(contest)]=[-2,0]
	data["jiaxuqin"][str(contest)]=[-2,0]
	data["cyzh"][str(contest)]=[-2,0]

for contest in range(199,259+1):
	data["BestQian"][str(contest)]=[-2,0] # rejoin
for contest in range(199,259+1):
	data["zhu_irse"][str(contest)]=[-2,0] # rejoin	
for contest in range(243,259+1):
	data["9caiji"][str(contest)]=[-2,0] # rejoin	

## before 261
for contest in range(118,260+1): 	
	data["jam64"][str(contest)]=[-2,0]
	data["super468"][str(contest)]=[-2,0]
	data["bourbonwhiskey"][str(contest)]=[-2,0]
	data["fireee"][str(contest)]=[-2,0]
	data["ayanamiaaa"][str(contest)]=[-2,0]
for contest in range(211,260+1):
	data["leileimiao"][str(contest)]=[-2,0] # rejoin

## before 262
for contest in range(118,261+1): 	
	data["v-ger"][str(contest)]=[-2,0]
	data["immajm"][str(contest)]=[-2,0]
	data["mercerchen"][str(contest)]=[-2,0]
	data["chiro_11"][str(contest)]=[-2,0]
	data["PurplePearl"][str(contest)]=[-2,0]
	data["zys01310131"][str(contest)]=[-2,0]
	data["weijiag"][str(contest)]=[-2,0]
	data["hjx2016"][str(contest)]=[-2,0]
	data["Oyyko"][str(contest)]=[-2,0]
	data["roccopass"][str(contest)]=[-2,0]
for contest in range(249,261+1):
	data["bxiao_ca"][str(contest)]=[-2,0] # rejoin
for contest in range(260,261+1):
	data["hongrubb"][str(contest)]=[-2,0] # rejoin

## before 263
for contest in range(118,262+1): 	
	data["elvistqchen"][str(contest)]=[-2,0]
	data["seekQ"][str(contest)]=[-2,0]
	data["Mikayla333"][str(contest)]=[-2,0]
	data["haruhiui"][str(contest)]=[-2,0]
	data["digmouse"][str(contest)]=[-2,0]
	data["Rainyforest"][str(contest)]=[-2,0]
	data["nijiademianbao"][str(contest)]=[-2,0]
## before 264
for contest in range(118,263+1): 	
	data["shiyaow"][str(contest)]=[-2,0]
	data["hkhzzz"][str(contest)]=[-2,0]
	data["Sato_Ken"][str(contest)]=[-2,0]
	data["FreeYourMind"][str(contest)]=[-2,0]
	data["answerer"][str(contest)]=[-2,0]	
for contest in range(263,263+1):
	data["LeeShengkai"][str(contest)]=[-2,0] # rejoin
for contest in range(263,263+1):
	data["lianxin_cn"][str(contest)]=[-2,0] # rejoin

## before 265
for contest in range(118,264+1): 	
	data["Jamesleons"][str(contest)]=[-2,0]
	data["REDSREDS"][str(contest)]=[-2,0]
	data["zeningc"][str(contest)]=[-2,0]
	data["Hogwartsss"][str(contest)]=[-2,0]
	data["scau_grated"][str(contest)]=[-2,0]

## before 266
for contest in range(118,265+1): 	
	data["jiechen067"][str(contest)]=[-2,0]
	data["Monsooooon"][str(contest)]=[-2,0]
	data["fatyuan"][str(contest)]=[-2,0]
	data["mtx2d"][str(contest)]=[-2,0]

## before 267
for contest in range(118,266+1): 	
	data["flyoceans"][str(contest)]=[-2,0]
	data["michelle_taco"][str(contest)]=[-2,0]
	data["irisbber"][str(contest)]=[-2,0]
	data["kuan525"][str(contest)]=[-2,0]
	data["kuailema9089"][str(contest)]=[-2,0]

## before 268
for contest in range(118,267+1): 	
	data["_Hy3"][str(contest)]=[-2,0]
	data["grcd"][str(contest)]=[-2,0]
	data["zhongdizhu"][str(contest)]=[-2,0]
	data["bl2621"][str(contest)]=[-2,0]
for contest in range(265,267+1):
	data["PurplePearl"][str(contest)]=[-2,0] # rejoin

## before 269
for contest in range(118,268+1): 	
	data["wqricardo"][str(contest)]=[-2,0]
	data["Leetcode_Pro"][str(contest)]=[-2,0]
	data["zz659749"][str(contest)]=[-2,0]
	data["ceaxyz"][str(contest)]=[-2,0]
	data["KimTaeyeon"][str(contest)]=[-2,0]
for contest in range(205,268+1):
	data["Kaiyu-Wang"][str(contest)]=[-2,0] # rejoin
for contest in range(250,268+1):
	data["migeater"][str(contest)]=[-2,0] # rejoin


## before 270
for contest in range(118,269+1): 	
	data["rika321"][str(contest)]=[-2,0]
	data["AC_Mikoto"][str(contest)]=[-2,0]
	data["megurine"][str(contest)]=[-2,0]
	data["X_ray"][str(contest)]=[-2,0]
	data["chiakimio"][str(contest)]=[-2,0]
	data["wytlc"][str(contest)]=[-2,0]


## before 271
for contest in range(118,270+1): 	
	data["txu33"][str(contest)]=[-2,0]
	data["Time-limit-exceed"][str(contest)]=[-2,0]
	data["izackwu"][str(contest)]=[-2,0]
for contest in range(263,270+1):
	data["dickbomb"][str(contest)]=[-2,0] # rejoin	

## before 272
for contest in range(118,271+1): 	
	data["awayzjj"][str(contest)]=[-2,0]
	data["visionary_sg"][str(contest)]=[-2,0]
	data["Zhuoran_Liu"][str(contest)]=[-2,0]
for contest in range(232,271+1):
	data["rqren2018"][str(contest)]=[-2,0] # rejoin	

## before 273
for contest in range(118,272+1): 	
	data["ocavue"][str(contest)]=[-2,0]
	data["asherascout"][str(contest)]=[-2,0]
	data["OnMyOwn"][str(contest)]=[-2,0]
	data["N2510"][str(contest)]=[-2,0]	
for contest in range(269,272+1):
	data["rookie0080"][str(contest)]=[-2,0]
for contest in range(241,272+1):	
	data["SaveThePlanet"][str(contest)]=[-2,0] # rejoin	

## before 274
for contest in range(118,273+1): 	
	data["wy907645377"][str(contest)]=[-2,0]
	data["sjyang_"][str(contest)]=[-2,0]
	data["iofu728"][str(contest)]=[-2,0]
	data["curiosity-10"][str(contest)]=[-2,0]
for contest in range(265,273+1):
	data["wfnuser"][str(contest)]=[-2,0]
for contest in range(272,273+1):	
	data["jingwenxxx"][str(contest)]=[-2,0] # rejoin	


## before 275
for contest in range(118,274+1): 	
	data["wakme"][str(contest)]=[-2,0]
	data["axlsdtkl"][str(contest)]=[-2,0]
	data["Rogn"][str(contest)]=[-2,0]
	data["Haoyuw"][str(contest)]=[-2,0]
	data["jushuai_lfx"][str(contest)]=[-2,0]
	data["wen_chin"][str(contest)]=[-2,0]
	data["Terry95"][str(contest)]=[-2,0]
	data["stevensnake"][str(contest)]=[-2,0]
	data["mfk443838746"][str(contest)]=[-2,0]
	data["981377660LMT"][str(contest)]=[-2,0]
	data["ainoyume"][str(contest)]=[-2,0]
for contest in range(272,274+1):
	data["aChris"][str(contest)]=[-2,0]
for contest in range(237,274+1):
	data["klutzCoder"][str(contest)]=[-2,0]
for contest in range(267,274+1):
	data["liulaoye135"][str(contest)]=[-2,0]	

## before 276
for contest in range(118,275+1): 	
	data["blzhu"][str(contest)]=[-2,0]
	data["QinhaoChang"][str(contest)]=[-2,0]
	data["KYan20010323"][str(contest)]=[-2,0]
	data["Attttrx"][str(contest)]=[-2,0]
	data["miahall"][str(contest)]=[-2,0]
	data["yeahhuai"][str(contest)]=[-2,0]
for contest in range(260,275+1):
	data["WKelvinson"][str(contest)]=[-2,0]	
for contest in range(266,275+1):
	data["jamesfan1101"][str(contest)]=[-2,0]	

## before 277
for contest in range(118,276+1): 	
	data["zjbztianya"][str(contest)]=[-2,0]
	data["aguang-xyz"][str(contest)]=[-2,0]
	data["Haoyangerrr-MoMo"][str(contest)]=[-2,0]
	data["lu-chen-chen"][str(contest)]=[-2,0]
	data["yu-niang-niang"][str(contest)]=[-2,0]
	data["yypu"][str(contest)]=[-2,0]
	data["alastian"][str(contest)]=[-2,0]
for contest in range(246,276+1):
	data["KurosuHa"][str(contest)]=[-2,0]	
for contest in range(135,276+1):
	data["davidqing1991"][str(contest)]=[-2,0]	
data["jamesfan1101"]["277"]=[442,4]		
'''

## before 278
for contest in range(118,277+1): 	
	data["wangdh15"][str(contest)]=[-2,0]
	data["yuliiia7"][str(contest)]=[-2,0]
	data["ruizhewu"][str(contest)]=[-2,0]
for contest in range(274,277+1): 	
	data["hongrubb52"][str(contest)]=[-2,0]

# data["rookie0080"]=data["rookie_my"]
# data.pop("rookie_my")

# data["roy_1127"]=data["jiutiany1127"]
# data.pop("jiutiany1127")

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
contests["129"] = 4456
contests["130"] = 5226
contests["131"] = 4894
contests["132"] = 4765
contests["133"] = 3863
contests["134"] = 4136
contests["135"] = 3634
contests["136"] = 4109
contests["137"] = 4091
contests["138"] = 4143
contests["139"] = 3985
contests["140"] = 4046
contests["141"] = 4126
contests["142"] = 4504
contests["143"] = 4271
contests["144"] = 4358
contests["145"] = 4931
contests["146"] = 5074
contests["147"] = 4906
contests["148"] = 5319
contests["149"] = 5091
contests["150"] = 5338
contests["151"] = 5261
contests["152"] = 5331
contests["153"] = 6212
contests["154"] = 6062
contests["155"] = 6585
contests["156"] = 6764
contests["157"] = 6650
contests["158"] = 6640
contests["159"] = 6626
contests["160"] = 6126
contests["161"] = 6255
contests["162"] = 5997
contests["163"] = 5873
contests["164"] = 5907
contests["165"] = 5495
contests["166"] = 5585
contests["167"] = 5453
contests["168"] = 5525
contests["169"] = 5932
contests["170"] = 6833
contests["171"] = 7189
contests["172"] = 6604
contests["173"] = 6103
contests["174"] = 6997
contests["175"] = 7826
contests["176"] = 8105
contests["177"] = 9091
contests["178"] = 9210
contests["179"] = 9847
contests["180"] = 10047
contests["181"] = 10930
contests["182"] = 11694
contests["183"] = 12539
contests["184"] = 13661
contests["185"] = 14207
contests["186"] = 11684
contests["187"] = 12350
contests["188"] = 12714
contests["189"] = 13036
contests["190"] = 11873
contests["191"] = 13276
contests["192"] = 13805
contests["193"] = 13794
contests["194"] = 13808
contests["195"] = 11467
contests["196"] = 14301
contests["197"] = 13983
contests["198"] = 15151
contests["199"] = 14309
contests["200"] = 15382
contests["201"] = 15616
contests["202"] = 14373	
contests["203"] = 15080	
contests["204"] = 13949	
contests["205"] = 13171
contests["206"] = 13291
contests["207"] = 12923
contests["208"] = 11498
contests["209"] = 12138
contests["210"] = 11792
contests["211"] = 11960
contests["212"] = 10984
contests["213"] = 10630
contests["214"] = 9769
contests["215"] = 9683
contests["216"] = 9573
contests["217"] = 9462
contests["218"] = 9827
contests["219"] = 9290
contests["220"] = 9606
contests["221"] = 8838
contests["222"] = 9692
contests["223"] = 10671
contests["224"] = 11023
contests["225"] = 11282
contests["226"] = 11433
contests["227"] = 11076
contests["228"] = 9869
contests["229"] = 11173
contests["230"] = 11654
contests["231"] = 12900
contests["232"] = 12541
contests["233"] = 12037
contests["234"] = 12421
contests["235"] = 11443
contests["236"] = 12115
contests["237"] = 11446
contests["238"] = 11635
contests["239"] = 10870
contests["240"] = 11576
contests["241"] = 11572
contests["242"] = 12400
contests["243"] = 12835
contests["244"] = 14467
contests["245"] = 12724
contests["246"] = 13703
contests["247"] = 12636
contests["248"] = 13720
contests["249"] = 12832
contests["250"] = 13694
contests["251"] = 13663
contests["252"] = 14252
contests["253"] = 13587
contests["254"] = 13755
contests["255"] = 11837
contests["256"] = 12936
contests["257"] = 12540
contests["258"] = 12179
contests["259"] = 11277
contests["260"] = 11274
contests["261"] = 11751
contests["262"] = 13130
contests["263"] = 11795
contests["264"] = 12700
contests["265"] = 11093
contests["266"] = 11909
contests["267"] = 11024
contests["268"] = 11794
contests["269"] = 10907
contests["270"] = 12931
contests["271"] = 12806
contests["272"] = 15427
contests["273"] = 12203
contests["274"] = 14086
contests["275"] = 16126
# starting from this week, we only consider the participant who at least solved one problem
contests["276"] = 12418  
contests["277"] = 12867
contests["278"] = 13688

json_str = json.dumps(contests)

with open('contests.json', 'w') as f:
    json.dump(json_str, f)
    

