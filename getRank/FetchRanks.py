import subprocess
import json
import argparse
import time

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
    
    # url = "https://leetcode.com/contest/api/ranking/weekly-contest-%d/?pagination=%d"
    url = "https://leetcode.cn/contest/api/ranking/weekly-contest-%d/?pagination=%d&region=global_v2"

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiNDQ4NzE1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NzQ4YzM3N2VjODY5NzRhYzZjMzdjYzMzMDBmOGQyZTllZGRlMDI2ZTQwYzY4NzAwMmI3MWQwZmJhM2EwZmY4IiwiaWQiOjQ0ODcxNSwiZW1haWwiOiJndWFuLmh1aWZlbmdAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ3aXNkb21wZWFrIiwidXNlcl9zbHVnIjoid2lzZG9tcGVhayIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNuL2FsaXl1bi1sYy11cGxvYWQvdXNlcnMvd2lzZG9tcGVhay9hdmF0YXJfMTU4NzQzMjQ5NC5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiZGV2aWNlX2lkIjoiZTk5N2UyMDIwMzdiZWU2ZWQwNWEzNjU4OTJkYzA4NjQiLCJpcCI6Ijk4LjIwNy4xNzYuMTQyIiwiX3RpbWVzdGFtcCI6MTczMjAwOTEyMS4zMzMxODgsImV4cGlyZWRfdGltZV8iOjE3MzQ1NDg0MDAsInZlcnNpb25fa2V5XyI6MH0.3xSvLz6ccXUYCMkgMpp7UGGz4UvnAkKJAAOQCWqy-Vs",
        "Referer": "https://leetcode.cn/contest/weekly-contest-424/ranking/2/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "baggage": "sentry-environment=production,sentry-release=41b65882,sentry-transaction=%2Fcontest%2F%5BcontestSlug%5D%2Franking%2F%5B%5B...page%5D%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=5b86bc385d7045bab19b11e9551d359e,sentry-sample_rate=0.03",
        "content-type": "application/json",
        # "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sentry-trace": "5b86bc385d7045bab19b11e9551d359e-85af6c2694216cf1-0",
        "x-csrftoken": "6QEHJqRqxTeDfRt7EwNrhnmRe8WRUaEshLMvO3zKCRtvHCUidH4TeD5GRpwMxZ8F",
    }

    
    header_template = ' -H "%s: %s" '
    header_str = ""
    for i, (k, v) in enumerate(headers.items()):
       header_str = header_str + " " + header_template % (k,v)

    # Read user ids
    fi = open('id.in', 'r')
    id_list = [line.strip() for line in fi.readlines()]
    id_set = set(id_list)
    fi.close()

    display = []
    data = {}
    
    # curl rank
    start, end = 1, page
    total_player = 0

    for i in range(start, end + 1):
        # print("curl " + url % (contest, i))
        print("curl " + header_str + " " + url % (contest, i))
        success = 0
        while success == 0:
          response = subprocess.check_output("curl " + header_str + " " + url % (contest, i), shell=True)                    
          str_response = response.decode('utf-8')

          try:            
            total_rank = json.loads(str_response)['total_rank']
            success = 1
          except Exception as e:
            print("retry page ", i, " due to ", str(e))        
        
        total_rank = json.loads(str_response)['total_rank']        
        submissions = json.loads(str_response)['submissions']        
        
        N = len(total_rank)        
        should_stop = False
        for i in range(N):
            line = total_rank[i]
            submission = submissions[i]

            if len(submission) == 0: 
               should_stop = True
               break
            
            # if line["data_region"]!='CN' and (line["username"] not in id_set):
            #    continue

            total_player += 1

            # print(line)
            # print(submission)

            if line["username"] in id_set:
                if len(submission) == 0: rank = -1
                else: rank = total_player # line["rank"]
                if line["username"] not in data or len(submission)!=0:
                  display.append([rank, line["username"], len(submission)])
                  data[line["username"]] = [rank, len(submission)]                     
                
        if should_stop: break
        

    # Output result
    
    print("\n******** search done ************\n")  

    print("Total players:", total_player)
    
    display = sorted(display)
        
    for ID in id_list:
      if ID not in data:
        data[ID] = [-1, 0]
         
    for item in display:
      print(item[0],item[1],item[2])
      
    print("\n******** display done ************\n")  

    return data

