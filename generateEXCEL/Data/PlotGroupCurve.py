import time
import datetime
import collections
import matplotlib.pyplot as plt


start = datetime.date(2018,9,2)
today = datetime.date.today()

file = open("GroupCurve/addPeople.txt","r") 
data = file.readlines()
file.close()

addPeople = collections.defaultdict(int)
for line in data:
  d = line.split("/")
  if len(d)!=3: continue
  date = datetime.date(int(d[2]),int(d[0]),int(d[1]))
  addPeople[date]+=1


file = open("GroupCurve/losePeople.txt","r") 
data = file.readlines()
file.close()
losePeople = collections.defaultdict(int)
for line in data:
  d = line.split("/")
  if len(d)!=3: continue
  date = datetime.date(int(d[2]),int(d[0]),int(d[1]))
  losePeople[date]+=1
  
count = 0;
Days = []
Nums = []
upper = []
lower = []
for i in range(500):
  day = start + datetime.timedelta(days=i)
  if day>today: break;
  
  Days.append(day.strftime("%Y/%m/%d"))
  
  if day in addPeople:
    count+=addPeople[day]    
    
  if day in losePeople:
    count-=losePeople[day]  
    
  upper.append(count+addPeople[day] if day in addPeople else count)  
  lower.append(count-losePeople[day] if day in losePeople else count)
  
  Nums.append(count)


for i in range(len(Days)):
    print(Days[i]," ",Nums[i])

    

plt.plot(Nums, label = 'member growth curve')
plt.fill_between(list(range(0,len(Days))), lower, upper, color = '#539caf', alpha = 0.5, label = 'same day fluctuation')
plt.xticks( list(range(0, len(Days),14)), Days[:-1:14], rotation=20 )
plt.grid(linestyle='-.')
plt.title("Historical number of members growth curve (weekly updated) ")
plt.legend(loc = 'upper left')
plt.show()
# plt.xticks(fontsize=16, color="red", rotation=45)



