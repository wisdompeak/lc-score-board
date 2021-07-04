import subprocess
import json
import argparse

# Get user's rank of contest.
# Can also get user's score and finish time if needed

def fetchRanking(contest,page):

    """
    # Get kwargs
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", help="contest id")
    parser.add_argument("page", help="rank total page")
    kwargs = parser.parse_args()
    contest = int(kwargs.contest)
    page = int(kwargs.page)
    """
    
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%d/?pagination=%d"

    # Read user ids
    fi = open('id.in', 'r')
    id_list = [line.strip() for line in fi.readlines()]
    id_set = set(id_list)
    fi.close()

    display = []
    data = {}
    
    # curl rank
    start, end = 1, page
    for i in range(start, end + 1):
        print("curl " + url % (contest, i))
        success = 0
        while success == 0:
          response = subprocess.check_output("curl " + url % (contest, i), shell=True)                    
          str_response = response.decode('utf-8')
          try:            
            total_rank = json.loads(str_response)['total_rank']
            success = 1
          except Exception as e:
            print("retry page ", i, " due to ", str(e))           
        
        total_rank = json.loads(str_response)['total_rank']        
        submissions = json.loads(str_response)['submissions']        
        
        N = len(total_rank)        
        for i in range(N):
            line = total_rank[i]
            submission = submissions[i]
            if line["username"] in id_set:
                if len(submission) == 0: rank = -1
                else: rank = line["rank"]
                display.append([rank, line["username"], len(submission)])
                data[line["username"]] = [rank, len(submission)]               
                
        if len(display) == len(id_set): break

    # Output result
    
    print("\n******** search done ************\n")  
    
    display = sorted(display)
        
    for ID in id_list:
      if ID not in data:
        data[ID] = [-1, 0]
         
    for item in display:
      print(item[0],item[1],item[2])
      
    print("\n******** display done ************\n")  

    return data

