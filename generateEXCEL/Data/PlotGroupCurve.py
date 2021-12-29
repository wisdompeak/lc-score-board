import time
import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np

from Read_Excel import read_excel
read_excel()


start = datetime.date(2018,9,2)
# start = datetime.date(2021,1,1)
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
  
  PeopleStatOut.append(min(365*2, (date2-date1).days))


file = open("Members/In.txt","r") 
data = file.readlines()
file.close()

for line in data:
  if len(line.split())!=2: continue
  readDate = line.split()[1]
  d = readDate.split("/")  
  date = datetime.date(int(d[2]),int(d[0]),int(d[1]))
  addPeople[date]+=1
  
  PeopleStatIn.append(min(365*2, (today-date).days))

 
count = 0
Days = []
Nums = []
upper = []
lower = []
for i in range(1500):
  day = start + datetime.timedelta(days=i)
  if day>today: break
  
  Days.append(day.strftime("%Y/%m/%d")[:])
  
  if day in addPeople:
    count+=addPeople[day]    
    
  if day in losePeople:
    count-=losePeople[day]  
    
  upper.append(count+addPeople[day] if day in addPeople else count)  
  lower.append(count-losePeople[day] if day in losePeople else count)
  
  Nums.append(count)



plt.figure(21,figsize=(40,16))

plt.subplot(211)
plt.plot(Nums, label = 'member growth curve')
plt.fill_between(list(range(0,len(Days))), lower, upper, color = '#539caf', alpha = 0.5, label = 'same-day fluctuation')
plt.xticks( list(range(0, len(Days),28)), Days[:-1:28], rotation=20, fontsize=14 ) 
plt.yticks(fontsize=14 ) 
plt.grid(linestyle='-.')
plt.title("Historical number of members growth curve (weekly updated) ", fontsize=25)
plt.legend(loc = 'upper left', fontsize=20)

plt.subplot(212)
maxDay = 365*2
n, bins, patches = plt.hist(x=PeopleStatOut, bins='auto', label = 'Quited', color='steelblue', alpha=0.7, rwidth=0.85)
plt.hist(x=PeopleStatIn, bins='auto', label = 'Current', color='#FF1B1B', alpha=0.6, rwidth=0.45)
plt.grid(axis='y', alpha=0.75)

tick1 = [x for x in range(0,maxDay+1,30)]
tick2 = [str(x) for x in range(0,maxDay+1,30)]
tick2[-1] = " >2Yr"
plt.xticks(tick1, tick2, fontsize=14)
plt.yticks(fontsize=14 ) 

plt.xlabel('Survival Days', fontsize=25)
plt.ylabel('Number of People', fontsize=25)
plt.title('Membership duration statistics', fontsize=25)
plt.legend(loc = 'upper right', fontsize=16)

plt.subplots_adjust(hspace=0.6)  


# plt.show()

plt.savefig('../../Img/curve.png')