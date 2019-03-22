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
endContest = 128

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
  for contestID in range(endContest,startContest-1,-1):
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
   
  pool = [] # A pool for computing rolling score
  for x in row[1:4]:
    if x[0]!=-2: pool.append(x[1])
  if len(pool)<=2: 
    RollingScore = round(sum(pool)/len(pool),1)
  else: 
    RollingScore = round((sum(pool)-min(pool))/2,1)
        
  newRow = [row[0],RollingScore]   # Reorder into [ID,RollingScore,contestInfo]
  for x in row[1:]: newRow.append(x)
      
  table.append(newRow)  

table = sorted(table, key = lambda x:x[1], reverse = True)  

for row in table:
  print(row)
  
############################ Graduated or laidoff members

table2 = []
for personID in data:

  if personID in id_list: continue
  if personID=="Ansonluo": continue
  
  row = [personID] 
  for contestID in range(endContest,startContest-1,-1):
    contestID = str(contestID)
    TotalPlayers = contests[contestID]
    if contestID not in data[personID]:
      row.append([-3,0,0])
    else:
      rank = data[personID][contestID][0]
      solved = data[personID][contestID][1]   
      if rank>0:   
      	score = round((1-rank/TotalPlayers)*80 + solved*5,1)
      else:
        score = 0
      row.append([rank,score,solved])
   
  RollingScore = 0       
  newRow = [row[0],RollingScore]   # Reorder into [ID,RollingScore,contestInfo]
  for x in row[1:]: newRow.append(x)
      
  table2.append(newRow)  

table2 = sorted(table2, key = lambda x:x[0])  

print("**********************************************************")
for row in table2:
  print(row)

	
############################

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'LeetCode Score Book'
print(colors)
colorChoice = ['EAEAEA','ffe6c2',colors.YELLOW,colors.GREEN,'19b457','ffb261']

sheet.column_dimensions['B'].width = 25.0
sheet.column_dimensions['D'].width = 5.0
SIZE = 15

# output header "contest" 
sheet['B1'].value = 'Contest'
sheet['B1'].alignment = Alignment(horizontal='center')
sheet['B1'].font = Font(bold=True, size=SIZE)

# output header "contest" "Participants"
sheet['B2'].value = 'Participants'
sheet['B2'].alignment = Alignment(horizontal='center')
sheet['B2'].font = Font(bold=True, size=SIZE)

# output contest ID / number of players
for k in range(endContest-startContest+1):
  row, column = 1, 5+k*2
  idx1 = convertToTitle(column)+str(row)
  idx2 = convertToTitle(column+1)+str(row)  
  sheet.merge_cells(idx1+':'+idx2)   
  sheet[idx1].value = endContest-k 
  sheet[idx1].alignment = Alignment(horizontal='center',vertical='center')
  sheet[idx1].font = Font(bold=True, size=SIZE)
  sheet[idx1].fill = PatternFill("solid", fgColor='D9D9D9')
  
  row, column = 2, 5+k*2
  idx1 = convertToTitle(column)+str(row)
  idx2 = convertToTitle(column+1)+str(row)  
  sheet.merge_cells(idx1+':'+idx2)   
  sheet[idx1].value = contests[str(endContest-k)] 
  sheet[idx1].font = Font(size=SIZE)
  sheet[idx1].alignment = Alignment(horizontal='center',vertical='center')
  sheet[idx1].fill = PatternFill("solid", fgColor='D9D9D9')


RowOffset = 4;

for i in range(len(id_list)):

  # 1st column: Rank
  row, column = RowOffset+i, 1
  idx = convertToTitle(column)+str(row) 
  sheet[idx].value = i+1
  sheet[idx].alignment = Alignment(horizontal='center',vertical='center')
  sheet[idx].font = Font(bold=True, size=SIZE)       
  if (i%2==0):
        sheet[idx].fill = PatternFill("solid", fgColor='EAEAEA')      
  
  for j in range(len(table[i])):  # column index
     
    # 2nd Column: LC ID
    if j==0:   
      row, column = RowOffset+i, 2+j
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][j]
      sheet[idx].alignment = Alignment(horizontal='center',vertical='center')
      sheet[idx].font = Font(bold=True, size=SIZE)       
      sheet[idx].hyperlink = 'http://leetcode.com/'+table[i][j]
      if (i%2==0):
        sheet[idx].fill = PatternFill("solid", fgColor='EAEAEA')   
        
    # 3rd column :  avg score
    elif j==1:            
      row, column = RowOffset+i, 2+j
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][1]
      sheet[idx].fill = PatternFill("solid", fgColor=colorChoice[5])
      sheet[idx].alignment = Alignment(horizontal='center',vertical='center')
      sheet[idx].font = Font(size=SIZE)
      
    else:     # output rank and score                    
      row, column = RowOffset+i, 5+(j-2)*2      
      idx = convertToTitle(column)+str(row) 
      
      sheet[idx].value = table[i][j][0]
      for k in range(0,5):
        if k>0 and table[i][j][2]==k or k==0 and i%2==0:  
          sheet[idx].fill = PatternFill("solid", fgColor=colorChoice[k])      
      sheet[idx].alignment = Alignment(horizontal='center',vertical='center')
      sheet[idx].font = Font(size=SIZE)
      
      row, column = RowOffset+i, 5+(j-2)*2+1
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table[i][j][1]
      if (i%2==0):
        sheet[idx].fill = PatternFill("solid", fgColor='EAEAEA')      
      sheet[idx].alignment = Alignment(horizontal='center',vertical='center')
      sheet[idx].font = Font(size=SIZE)
      
      if (table[i][0]=="SeymourLee" or table[i][0]=="IrisGuo") and j==len(table[i])-1:
        row, column = RowOffset+i, 5+(j-2)*2+2
        idx = convertToTitle(column)+str(row) 
        sheet[idx].value = "单身"  
        sheet[idx].font = Font(bold=True, color='FF00FF',size=12)
        sheet[idx].alignment = Alignment(horizontal='center',vertical='center')
    

############################
      
RowOffset += len(id_list)+2

row, column = RowOffset+1, 2
idx = convertToTitle(column)+str(row) 
sheet[idx].value = '-1:     absent/zero'
sheet[idx].font = Font(size=15)

row, column = RowOffset+2, 2
idx = convertToTitle(column)+str(row) 
sheet[idx].value = '-2:     not joined'
sheet[idx].font = Font(size=15)

row, column = RowOffset+3, 2
idx = convertToTitle(column)+str(row) 
sheet[idx].value = '-3:     left/quited'
sheet[idx].font = Font(size=15)

row, column = RowOffset+5, 2
idx = convertToTitle(column)+str(row) 
idx2 = convertToTitle(column+5)+str(row) 
sheet.merge_cells(idx+':'+idx2)
sheet[idx].value = 'More about the Rules'
sheet[idx].font = Font(size=15)
sheet[idx].font = Font(bold=True, size=SIZE)
sheet[idx].hyperlink = 'https://wisdompeak.github.io/lc-score-board/rules.html'

row, column = RowOffset+6, 2
idx = convertToTitle(column)+str(row) 
idx2 = convertToTitle(column+5)+str(row) 
sheet.merge_cells(idx+':'+idx2)
sheet[idx].value = 'See the full list of daily problems'
sheet[idx].font = Font(size=15)
sheet[idx].font = Font(bold=True, size=SIZE)
sheet[idx].hyperlink = 'https://bit.ly/2X0NW4e'

############################

RowOffset += 10
row, column = RowOffset, 2
idx = convertToTitle(column)+str(row) 
idx2 = convertToTitle(column+8)+str(row) 
sheet.merge_cells(idx+':'+idx2)
sheet[idx].value = 'Graduated or laidoff members in 2019'
sheet[idx].font = Font(size=15)
sheet[idx].font = Font(bold=True, size=SIZE)


RowOffset += 2

for i in range(len(table2)):

  # 1st column: Rank
  row, column = RowOffset+i, 1
  idx = convertToTitle(column)+str(row) 
  sheet[idx].value = "-"
  sheet[idx].alignment = Alignment(horizontal='center') 
  sheet[idx].font = Font(bold=True, size=SIZE)       
  if (i%2==0):
        sheet[idx].fill = PatternFill("solid", fgColor='EAEAEA')      
  
  for j in range(len(table2[i])):  # column index
     
    # 2nd Column: LC ID
    if j==0:   
      row, column = RowOffset+i, 2+j
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table2[i][0]
      sheet[idx].alignment = Alignment(horizontal='center') 
      sheet[idx].font = Font(bold=True, size=SIZE)       
      sheet[idx].hyperlink = 'http://leetcode.com/'+table2[i][j]
      if (i%2==0):
        sheet[idx].fill = PatternFill("solid", fgColor='EAEAEA')   
        
    # 3rd column :  avg score
    elif j==1:            
      row, column = RowOffset+i, 2+j
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = "-"
      sheet[idx].fill = PatternFill("solid", fgColor=colorChoice[5])
      sheet[idx].alignment = Alignment(horizontal='center')
      sheet[idx].font = Font(size=SIZE)
      
    else:     # output rank and score                    
      row, column = RowOffset+i, 5+(j-2)*2      
      idx = convertToTitle(column)+str(row) 
      
      sheet[idx].value = table2[i][j][0]
      for k in range(0,5):
        if k>0 and table2[i][j][2]==k or k==0 and i%2==0:  
          sheet[idx].fill = PatternFill("solid", fgColor=colorChoice[k])      
      sheet[idx].alignment = Alignment(horizontal='center') 
      sheet[idx].font = Font(size=SIZE)
      
      row, column = RowOffset+i, 5+(j-2)*2+1
      idx = convertToTitle(column)+str(row) 
      sheet[idx].value = table2[i][j][1]
      if (i%2==0):
        sheet[idx].fill = PatternFill("solid", fgColor='EAEAEA')      
      sheet[idx].alignment = Alignment(horizontal='center') 
      sheet[idx].font = Font(size=SIZE)


############################



      
wb.save('index.xlsx')    	

