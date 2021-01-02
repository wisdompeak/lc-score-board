import os
import argparse

mainArgumentsParser = argparse.ArgumentParser()
mainArgumentsParser.add_argument("endContest", help="EndContest id")
kwargs = mainArgumentsParser.parse_args()
endContest = int(kwargs.endContest)
        
os.system('python3 index.py ' + str(endContest))
os.system('python3 graduates.py ' + str(endContest))