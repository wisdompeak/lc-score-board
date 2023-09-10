import json
from pprint import pprint
import xlrd
import json
import datetime
import collections
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import ticker
from matplotlib.ticker import NullFormatter, FixedLocator

with open('data.json', 'r') as f:
    json_str = json.load(f)
    contest_data = json.loads(json_str)

with open('contests.json', 'r') as f:
    json_str = json.load(f)
    contest_meta = json.loads(json_str)

lastContest = 362
firstContest = lastContest-51

'''**************************************'''
# AK of each contest
ak_by_contest = [0 for i in range(52)]
ak_by_pct = [0 for i in range(52)]
member_by_contest = [0 for i in range(52)]
for contest_id in range(firstContest, lastContest+1):
    for user in contest_data:
        if str(contest_id) not in contest_data[user]:
            continue		
        ac = contest_data[user][str(contest_id)][1]
        member_by_contest[contest_id - firstContest]+=1		
        if ac == 4:
            ak_by_contest[contest_id - firstContest]+=1
for contest_id in range(firstContest, lastContest+1):
	ak_by_pct[contest_id - firstContest] = ak_by_contest[contest_id - firstContest] / member_by_contest[contest_id - firstContest]
'''**************************************'''
# weekly contest normialized score distribution
row_list = []
players = [0 for _ in range(firstContest, lastContest+1)]
for user, v in contest_data.items():
    for contest_idx in range(firstContest,lastContest+1):
        if str(contest_idx) in contest_data[user] and contest_data[user][str(contest_idx)][0] > 0:
            # score = contest_data[user][str(contest_idx)][0]
			# score = (1 - contest_data[user][str(contest_idx)][0] / contest_meta[str(contest_idx)]) * 80 \
			#          + contest_data[user][str(contest_idx)][1] * 5
            score = contest_data[user][str(contest_idx)][0] / contest_meta[str(contest_idx)]			
            row_list.append((contest_idx, score))
            players[contest_idx-firstContest] += 1
df = pd.DataFrame(index=np.arange(0,len(row_list)), columns=('week', 'score'))
for i in range(0,len(row_list)):
    df.loc[i] = row_list[i]
df_counts = df.groupby(['score', 'week']).size().reset_index(name='counts')

fig, (ax, ax2) = plt.subplots(2, 1,figsize=(50,20), dpi= 80, \
    sharex=True, gridspec_kw={'height_ratios': [3, 2]})

sns.boxplot(x=df_counts.week, y=df_counts.score, whis=np.inf, ax=ax, boxprops={'fill': None})
sns.stripplot(x=df_counts.week, y=df_counts.score, ax=ax, dodge=True)
ax.set_title('Global Ranking (Top Percentage) of all group members over the most recent 52 games\n', fontsize=30)
ax.set_ylabel('Global Rank', fontsize=30)
ax.set_xlabel("Note: Each dot represents a data point. A smaller pct means a higher rank. The box indicates the 25%, 50%, 75% percentiles of members in each game. ", fontsize=30)
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
# ax.set_yscale("log")
# ax.yaxis.set_major_locator(FixedLocator([1, 200, 500, 1000, 2000, 3000, 4000, 5000, 10000]))
ax.yaxis.set_major_locator(FixedLocator([0.01, 0.1, 0.2, 0.3, 0.4, 0.5]))
ax.set_ylim([0.5, 0.01])


ax2.bar(list(range(0,52)), ak_by_contest, alpha=0.6)
ax2.set_xlabel('\nWeekly Contest # '+str(firstContest)+'=> '+str(lastContest), fontsize=30)
ax2.set_title('Number & Percentage of players who conquered all problems in a game', fontsize=30)
ax2.grid(linestyle='-.')
ax2.set_ylim([0, 200])
ax2.tick_params(axis='y', color = 'b', labelcolor = 'tab:blue')

ax3 = ax2.twinx()
ax3.plot(ak_by_pct, linewidth='5', color='r')
ax3.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
ax3.tick_params(axis='y', color = 'r', labelcolor = 'r')


for item in (ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(30)
for item in (ax2.get_xticklabels() + ax2.get_yticklabels()):
    item.set_fontsize(30)
for item in (ax3.get_xticklabels() + ax3.get_yticklabels()):
    item.set_fontsize(30)	

x_labels_arry = ['' for i in range(lastContest-firstContest+1)]
for i in range(0,len(x_labels_arry),5):
    x_labels_arry[i] = str(firstContest+i)    
ax.set_xticklabels(x_labels_arry)
plt.savefig('../Img/Rankings.png')