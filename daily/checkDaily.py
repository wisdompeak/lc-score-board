import datetime
import json
import math
import pandas
import requests
import time

uid = ''
token = ''
session = requests.Session()
url = 'https://leetcode.com/problems/two-sum/'


def prepareSession():
    cookies = session.get(url).cookies
    token = cookies.get('csrftoken')
    uid = cookies.get('__cfduid')
    uid = uid if uid else ''


def downloadSubmission(leetcodeId):
    sql = {'operationName': 'getRecentSubmissionList',
           'variables': {'username': leetcodeId, 'limit': 100 },
           'query': '''
                query getRecentSubmissionList($username: String!, $limit: Int!) {
                    recentSubmissionList(username: $username, limit: $limit) {
                      title
                      titleSlug
                      timestamp
                      statusDisplay
                      lang
                      __typename
                    }
                    languageList {
                      id
                      name
                      verboseName
                      __typename
                    }
                }           
           '''
           }

    data = json.dumps(sql).encode('utf8')
    headers = {'Content-Type': 'application/json',
               'Referer': url,
               'Cookie': '__cfduid=' + uid + ';' + 'csrftoken=' + token,
               'x-csrftoken': token
               }
    resp = session.post('https://leetcode.com/graphql', data=data, headers=headers, timeout=10)
    open('submissions/' + leetcodeId + '.json', 'w').write(resp.content.decode('utf-8'))


def checkSubmission(leetcodeId, problem):
    data = json.load(open('submissions/' + leetcodeId + '.json'))
    for submission in data['data']['recentSubmissionList']:
        if submission['statusDisplay'] == 'Accepted' and submission['titleSlug'] == problem:
            t = int(submission['timestamp'])
            now = int(time.time())
            if t > now - 3600 * 24 * 2:
                return True
    return False


def downloadProblem():
    url = "https://leetcode.com/api/problems/all/"
    resp = session.get(url, headers={}, timeout=10)
    open('problems.json', 'w').write(resp.content.decode('utf-8'))


def parseProblem():
    data = json.load(open('problems.json'))
    problems = {}
    for question in data['stat_status_pairs']:
        question_id = question['stat']['frontend_question_id']
        question_slug = question['stat']['question__title_slug']
        level = question['difficulty']['level']
        # if question['paid_only']:
        #     continue
        problems[question_id] = question_slug
    return problems


def downloadMember():
    url = 'https://github.com/wisdompeak/lc-score-board/blob/gh-pages/generateEXCEL/Data/Members/GroupRecord.xlsx?raw=true'
    resp = requests.get(url, allow_redirects=True)
    open('GroupRecord.xlsx', 'wb').write(resp.content)


def parseMember():
    members = {}
    # '../generateEXCEL/Data/Members/GroupRecord.xlsx'
    df = pandas.read_excel('GroupRecord.xlsx', sheet_name='Current', header=None, usecols=[0, 1])
    for i in range(df.shape[0]):
        wechatId = df.iat[i, 0]
        leetCodeId = df.iat[i, 1]
        members[wechatId] = leetCodeId
    return members


# TODO
def downloadTasks():
    print('https://docs.google.com/spreadsheets/d/1kBGyRsSdbGDu7DzjQcC-UkZjZERdrP8-_QyVGXHSrB8/edit#gid=0')


def parseTasks():
    tasks = {}
    df = pandas.read_excel('LeetCode打卡记录.xlsx', sheet_name='Problem List', header=None, usecols=[0, 2])
    for i in range(df.shape[0]):
        id = df.iat[i, 0]
        date = df.iat[i, 1]
        if (type(id) == int or type(id) == float) and not math.isnan(id):
            tasks[date] = int(id)
    return tasks


def main():
    prepareSession()
    # downloadProblem()
    problems = parseProblem()
    # downloadMember()
    members = parseMember()
    # downloadTasks()
    tasks = parseTasks()
    today = datetime.date.today()
    date = today - datetime.timedelta(days=2)
    date = pandas.Timestamp(date)
    problemId = tasks[date]
    problem = problems[problemId]
    for id in members:
        if id != 'Lucas':
            continue
        downloadSubmission(members[id])
        success = checkSubmission(members[id], problem)
        if not success:
            print(id, members[id])


if __name__ == "__main__":
    main()
