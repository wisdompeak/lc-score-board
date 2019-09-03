import time
import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np

start = datetime.date(2018,9,2)
today = datetime.date.today()

addPeople = collections.defaultdict(int)
losePeople = collections.defaultdict(int)
PeopleStatIn = []
PeopleStatOut = []

file = open("Members/Out.txt","r") 
data = file.readlines()
file.close()

for line in data:
  if len(line.split())!=3: continue
  
  readDate = line.split()[1]
  d = readDate.split("/")  
  date1 = datetime.date(int(d[2]),int(d[0]),int(d[1]))
  addPeople[date1]+=1
  
  readDate = line.split()[2]
  d = readDate.split("/")  
  date2 = datetime.date(int(d[2]),int(d[0]),int(d[1]))
  losePeople[date2]+=1
  
  PeopleStatOut.append((date2-date1).days)


file = open("Members/In.txt","r") 
data = file.readlines()
file.close()

for line in data:
  if len(line.split())!=2: continue
  readDate = line.split()[1]
  d = readDate.split("/")  
  date = datetime.date(int(d[2]),int(d[0]),int(d[1]))
  addPeople[date]+=1
  
  PeopleStatIn.append((today-date).days)


  
  
count = 0;
Days = []
Nums = []
upper = []
lower = []
for i in range(500):
  day = start + datetime.timedelta(days=i)
  if day>today: break;
  
  Days.append(day.strftime("%Y/%m/%d")[2:])
  
  if day in addPeople:
    count+=addPeople[day]    
    
  if day in losePeople:
    count-=losePeople[day]  
    
  upper.append(count+addPeople[day] if day in addPeople else count)  
  lower.append(count-losePeople[day] if day in losePeople else count)
  
  Nums.append(count)


for i in range(len(Days)):
    print(Days[i]," ",Nums[i])


plt.figure(21,figsize=(10,10))

plt.subplot(211)
plt.plot(Nums, label = 'member growth curve')
plt.fill_between(list(range(0,len(Days))), lower, upper, color = '#539caf', alpha = 0.5, label = 'same-day fluctuation')
plt.xticks( list(range(0, len(Days),14)), Days[:-1:14], rotation=20 ) 
plt.grid(linestyle='-.')
plt.title("Historical number of members growth curve (weekly updated) ")
plt.legend(loc = 'upper left')
# plt.xticks(fontsize=16, color="red", rotation=45)

plt.subplot(212)
maxDay = (today-start).days
n, bins, patches = plt.hist(x=PeopleStatOut, bins='auto', label = 'Quited', color='steelblue', alpha=0.7, rwidth=0.65)
plt.hist(x=PeopleStatIn, bins='auto', label = 'Current', color='#FF1B1B', alpha=0.6, rwidth=0.45)
plt.grid(axis='y', alpha=0.75)
plt.xticks( list(range(0,maxDay,25)), list(range(0,maxDay,25)))
plt.xlabel('Survival Days')
plt.ylabel('Number of People')
plt.title('Membership duration statistics')
plt.legend(loc = 'upper right')

plt.subplots_adjust(hspace=0.6)  


plt.show()

