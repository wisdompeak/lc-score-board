import time
import datetime

def CalculateMembership():
    
    Membership = {}
    
    file = open("Data/Members/Out.txt", "r") 
    for line in file:
        info = line.split()
        if len(info)<3: continue
        name = info[0]
        d1 = info[1].split("/")
        date1 = datetime.date(int(d1[2]),int(d1[0]),int(d1[1]))
        d2 = info[2].split("/")
        date2 = datetime.date(int(d2[2]),int(d2[0]),int(d2[1]))
        Membership[name] = (date2-date1).days
    file.close()
    
    
    today = datetime.date.today()
    file = open("Data/Members/In.txt", "r") 
    for line in file:
        info = line.split()
        if len(info)<2: continue
        name = info[0]
        d = info[1].split("/")
        date = datetime.date(int(d[2]),int(d[0]),int(d[1]))
        Membership[name] = (today-date).days
    file.close()
    
    return Membership
    
