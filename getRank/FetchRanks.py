import subprocess
import json
import argparse


# Get user's rank of contest.
# Can also get user's score and finish time if needed


def fetchRanking(contest, page):
    """
    # Get kwargs
    parser = argparse.ArgumentParser()
    parser.add_argument("contest", help="contest id")
    parser.add_argument("page", help="rank total page")
    kwargs = parser.parse_args()
    contest = int(kwargs.contest)
    page = int(kwargs.page)
    """

    url = f"https://leetcode.com/contest/api/ranking/weekly-contest-{contest}/?pagination=%d"

    # Read user ids
    fi = open('id.in', 'r')
    id_list = [line.strip() for line in fi.readlines()]
    id_list.remove("lee215")
    id_set = set(id_list)
    fi.close()

    display = []
    data = {}

    # curl rank
    start, end = 1, page
    group_rank = 1
    for p_i in range(start, end + 1):
        print("curl " + url % p_i)
        response = subprocess.check_output("curl " + url % p_i, shell=True)
        str_response = response.decode('utf-8')

        total_rank = json.loads(str_response)['total_rank']
        submissions = json.loads(str_response)['submissions']

        user_count = len(total_rank)
        for u_i in range(user_count):
            user = total_rank[u_i]
            submission = submissions[u_i]
            if user["username"] in id_set and user["username"] not in data:
                rank = user["rank"] if len(submission) != 0 else -1
                display.append([rank, user["username"], len(submission), group_rank])
                data[user["username"]] = [rank, len(submission), group_rank]
                group_rank += 1

        if len(display) == len(id_set):
            break

    # Output result

    print("\n******** search done ************\n")

    display.sort()

    for user_id in id_list:
        if user_id not in data:
            data[user_id] = [-1, 0]

    for item in display:
        print(item[0], item[1], item[2], item[3])

    print("\n******** display done ************\n")

    return data
