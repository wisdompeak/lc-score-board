import json
import openpyxl
from openpyxl.styles import colors
from openpyxl.styles import Font, Color, PatternFill, Alignment


def convertToTitle(n):
  result = ''
  dist = ord('A') 
  while n > 0:
    y = (n-1) % 26
    n = (n-1) // 26
    s = chr(y+dist)
    result = ''.join((s, result))
  return result
        
startContest = 118
endContest = 121

# import data
with open('../getRank/data.json', 'r') as f:
   	json_str = json.load(f)
   	data = json.loads(json_str)
   	
with open('../getRank/contests.json', 'r') as f:
   	json_str = json.load(f)
   	contests = json.loads(json_str)     	
   	
# import person   	
fi = open('../getRank/id.in', 'r')
id_list = [line.strip() for line in fi.readlines()]
fi.close()   	

# compute scores

table = []
for personID in id_list:
  row = [personID] 
  for contestID in range(startContest,endContest+1):
    contestID = str(contestID)
    TotalPlayers = contests[contestID]
    if contestID not in data[personID]:
      row.append([-2,0,0])
    else:
      rank = data[personID][contestID][0]
      solved = data[personID][contestID][1]   
      if rank>0:   
      	score = round((1-rank/TotalPlayers)*80 + solved*5,1)
      else:
        score = 0
      row.append([rank,score,solved])
  
  pool = []
  for x in row[::-1][0:3]:
    if x[0]!=-2: pool.append(x[1])
  if len(pool)<=2: row.append(round(sum(pool)/len(pool),1))
  else: row.append(round((sum(pool)-min(pool))/2,1))
      
  table.append(row)
  
table = sorted(table, key = lambda x:x[-1], reverse = True)  

for row in table:
  print(row)
  
	
############################

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'LeetCode Score Book'
print(colors)
colorChoice = ['ffe6c2',colors.YELLOW,colors.GREEN,'19b457','ffb261']

sheet.column_dimensions['A'].width = 25.0
SIZE = 15

# output "contest" / "Participants"
sheet['A1'].value = 'Contest'
sheet['A1'].alignment = Alignment(horizontal='center')
sheet['A1'].font = Font(bold=True, size=SIZE)

sheet['A2'].value = 'Participants'
sheet['A2'].alignment = Alignment(horizontal='center')
sheet['A2'].font = Font(bold=True, size=SIZE)

# output contest ID / number of players
for k in range(endContest-startContest+1):
  row, column = 1, 1+1+k*2
  idx1 = convertToTitle(column)+str(row)
  idx2 = convertToTitle(column+1)+str(row)  
  sheet.merge_cells(idx1+':'+idx2)   
  sheet[idx1].value = startContest+k
  sheet[idx1].alignment = Alignment(horizontal='center') 
  sheet[idx1].font = Font(bold=True, size=SIZE)
  sheet[idx1].fill = PatternFill("solid", fgColor='D9D9D9')
  
  row, column = 2, 1+1+k*2
  idx1 = convertToTitle(column)+str(row)
  idx2 = convertToTitle(column+1)+str(row)  
  sheet.merge_cells(idx1+':'+idx2)   
  sheet[idx1].value = contests[str(startContest+k)]
  sheet[idx1].font = Font(size=SIZE)
  sheet[idx1].alignment = Alignment(horizontal='center') 
  sheet[idx1].fill = PatternFill("solid", fgColor='D9D9D9')


RowOffset = 4;

for i in range(len(id_list)):
  
  for j in range(len(table[i])):
  
    if j==0:    # output person ID
      row, column = RowOffset+i, 1+j
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][j]
      sheet[idx].alignment = Alignment(horizontal='center') 
      sheet[idx].font = Font(bold=True, size=SIZE)       
      sheet[idx].hyperlink = 'http://leetcode.com/'+table[i][j]
  
    elif j>0 and j<len(table[i])-1:     # output rank and score
    
      row, column = RowOffset+i, 1+1+(j-1)*2      
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][j][0]
      for k in range(1,5):
        if table[i][j][2]==k:  
          sheet[idx].fill = PatternFill("solid", fgColor=colorChoice[k-1])      
      sheet[idx].alignment = Alignment(horizontal='center') 
      sheet[idx].font = Font(size=SIZE)
      
      row, column = RowOffset+i, 1+1+(j-1)*2+1
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][j][1]
      sheet[idx].alignment = Alignment(horizontal='center') 
      sheet[idx].font = Font(size=SIZE)
    
    elif j==len(table[i])-1:            # output total score
      row, column = RowOffset+i, 1+1+(j-1)*2+1     
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][j]
      sheet[idx].fill = PatternFill("solid", fgColor=colorChoice[4])
      sheet[idx].alignment = Alignment(horizontal='center')
      sheet[idx].font = Font(size=SIZE)
      

row, column = RowOffset+len(id_list)+2, 1
idx = convertToTitle(column)+str(row) 
sheet[idx].value = '-2:     Not joined group yet'
sheet[idx].font = Font(size=15)

row, column = RowOffset+len(id_list)+3, 1
idx = convertToTitle(column)+str(row) 
sheet[idx].value = '-1:     Absent or zero score'
sheet[idx].font = Font(size=15)
      
wb.save('index.xlsx')    	

