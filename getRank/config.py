class Config:
    SHORT_INTERVAL = 1
    MID_INTERVAL = 10
    LONG_INTERVAL = 60

    GRAPHQL_ATTEMPTS = 3

    MAINPAGE_HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }

    GRAPHQL_HEADERS = {
        "accept": "*/*",
        "accept-encoding": "gzip",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://leetcode.com",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }

    # $limit seems useless
    GRAPHQL_JSON = {
        "operationName": "getContentRankingData",
        "variables": {
            "username": "PLACEHOLDER",
        },
        "query": "query getContentRankingData($username: String!) { userContestRanking(username: $username) { attendedContestsCount    rating    globalRanking }  userContestRankingHistory(username: $username) {contest { title}   rating   ranking  }}"

    }

class Config2:
    SHORT_INTERVAL = 1
    MID_INTERVAL = 10
    LONG_INTERVAL = 60

    GRAPHQL_ATTEMPTS = 1

    MAINPAGE_HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }

    GRAPHQL_HEADERS = {
        "accept": "*/*",
        "accept-encoding": "gzip",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://leetcode-cn.com",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    }

    # $limit seems useless
    GRAPHQL_JSON = {
        "operationName": "userContest",
        "variables": {
            "userSlug": "PLACEHOLDER",
        },
        "query": "query userContest($userSlug: String!) {userContestRanking(userSlug: $userSlug) {currentRatingRanking    ratingHistory    levelHistory    contestRankingHistoryV2    contestHistory    __typename  }  globalRatingRanking(userSlug: $userSlug)  userContestScore(userSlug: $userSlug)  contestUnratedContests}"
    }
    
