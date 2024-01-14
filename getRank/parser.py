import re
import copy
import json
import time
import requests
# from config import Config

class LeetcodeParser:
    def __init__(self, users, Config):
        self.users = users
        self.Config = Config
        self.session = None
        # Have no idea what it is and whether it will change
        self.xpid = None
        self.results = {}

        # Connect
        self.reset()

    def reset(self):
        # Close previous connection
        if self.session:
            self.session.close()

        # Try to reconnect
        while True:
            # Wait for a moment
            time.sleep(self.Config.MID_INTERVAL)

            try:
                # Launch a new session
                self.session = requests.Session()
                self.session.headers.update()
                response = self.session.get(
                    url="http://leetcode.com/",
                    headers=self.Config.MAINPAGE_HEADERS,
                    timeout=(9.05, 5),
                )
            except requests.RequestException:
                # Close and retry through next loop
                self.session.close()
            else:
                # Get xpid
                # self.xpid = re.search(r"loader_config={xpid:\"(\S+?)\"", response.text).groups()[0]

                # Success and exit
                break

    def parse(self):       
        for user in self.users:
            referer = f"https://leetcode.com/{user}/"

            # json data for POST
            request_payload = copy.deepcopy(self.Config.GRAPHQL_JSON)
            request_payload["variables"]["username"] = user

            # extra headers for POST
            headers = copy.deepcopy(self.Config.GRAPHQL_HEADERS)
            headers["referer"] = referer
            headers["x-csrftoken"] = self.session.cookies.get("csrftoken")

            success = False

            while not success:
                response = None
                for _ in range(self.Config.GRAPHQL_ATTEMPTS):
                    try:
                        response = self.session.post(
                            url="https://leetcode.com/graphql",
                            headers=headers,
                            data=json.dumps(request_payload),
                            timeout=(9.05, 5),
                        )
                    except requests.RequestException:
                        response = None
                        time.sleep(self.Config.SHORT_INTERVAL)
                    else:
                        break

                if not response:
                    self.reset()                    
                    print(f"{user}\tnot found.")
                else:
                    success = True
                    result = json.loads(response.text)
                    self.results[user] = result["data"]
                    if "errors" in result:
                        print(f"{user}\tis invalid.")
                    else:
                        print(f"{user}\tis recorded.")

                        
class LeetcodeParser2:
    def __init__(self, users, Config):
        self.users = users
        self.Config = Config
        self.session = None
        # Have no idea what it is and whether it will change
        self.xpid = None
        self.results = {}

        # Connect
        self.reset()

    def reset(self):
        # Close previous connection
        if self.session:
            self.session.close()

        # Try to reconnect
        while True:
            # Wait for a moment
            time.sleep(self.Config.MID_INTERVAL)

            try:
                # Launch a new session
                self.session = requests.Session()
                self.session.headers.update()
                response = self.session.get(
                    url="https://leetcode-cn.com/",
                    headers=self.Config.MAINPAGE_HEADERS,
                    timeout=(9.05, 5),
                )
            except requests.RequestException:
                # Close and retry through next loop
                self.session.close()
            else:
                # Get xpid
                # self.xpid = re.search(r"loader_config={xpid:\"(\S+?)\"", response.text).groups()[0]

                # Success and exit
                break

    def parse(self):       
        for user in self.users:
            referer = f"https://leetcode.cn/u/{user}/"

            # json data for POST
            request_payload = copy.deepcopy(self.Config.GRAPHQL_JSON)
            request_payload["variables"]["userSlug"] = user

            # extra headers for POST
            headers = copy.deepcopy(self.Config.GRAPHQL_HEADERS)
            headers["referer"] = referer
            headers["x-csrftoken"] = self.session.cookies.get("csrftoken")

            success = False

            while not success:
                response = None
                for _ in range(self.Config.GRAPHQL_ATTEMPTS):
                    try:
                        response = self.session.post(
                            url="https://leetcode.cn/graphql",
                            headers=headers,
                            data=json.dumps(request_payload),
                            timeout=(9.05, 5),
                        )
                    except requests.RequestException:
                        response = None
                        time.sleep(self.Config.SHORT_INTERVAL)
                    else:
                        break

                if not response:
                    self.reset()                    
                    print(f"{user}\tnot found.")
                else:
                    success = True
                    result = json.loads(response.text)
                    self.results[user] = result["data"]                    
                    if "errors" in result:
                        print(f"{user}\tis invalid.")
                    else:
                        print(f"{user}\tis recorded.")