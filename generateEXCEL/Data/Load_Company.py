def LoadCompany():
    file = open("Data/Members/Company.txt", "r") 
    Company = {}
    for line in file:
        info = line.split()
        if len(info)<2: continue
        Company[info[0]] = info[1]
    file.close()
    return Company
