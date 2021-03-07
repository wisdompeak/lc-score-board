import xlrd
from datetime import date,datetime

def read_excel():
    ExcelFile = 'Members/GroupRecord.xlsx'
    wb = xlrd.open_workbook(filename=ExcelFile) #打开文件

    file_in = open("Members/In.txt", "w") 
    file_out = open("Members/Out.txt", "w")     
    
    Map = dict()  

    # sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
    # print(wb.sheet_names())#获取所有表格名字
    # print(sheet1)
    # print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)	

    sheet2 = wb.sheet_by_index(1)
    print('Label:',sheet2.name,'Rows:',sheet2.nrows,'Cols:',sheet2.ncols)
    for i in range(sheet2.nrows):
        date_value1 = xlrd.xldate_as_tuple(sheet2.cell_value(i,2),wb.datemode)
        date_value2 = xlrd.xldate_as_tuple(sheet2.cell_value(i,3),wb.datemode)
        # print(sheet2.cell_value(i,1),date(*date_value1[:3]).strftime('%Y/%m/%d'),date(*date_value2[:3]).strftime('%Y/%m/%d'))    
        id = sheet2.cell_value(i,1)
        if id==1373757850: id = int(id)
        if id==457368837: id = int(id)
        file_out.write(str(id)+" "+date(*date_value1[:3]).strftime('%m/%d/%Y')+" "+date(*date_value2[:3]).strftime('%m/%d/%Y')+"\n")
        Map[str(id)] = sheet2.cell_value(i,6)

    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    print('Label:',sheet1.name,'Rows:',sheet1.nrows,'Cols:',sheet1.ncols)
    for i in range(sheet1.nrows):
        date_value = xlrd.xldate_as_tuple(sheet1.cell_value(i,2),wb.datemode)
        id = sheet1.cell_value(i,1)        
        if id==1373757850: id = int(id)
        if id==457368837: id = int(id)
        # print(sheet1.cell_value(i,1),date(*date_value[:3]).strftime('%m/%d/%Y'))        
        file_in.write(str(id)+" "+date(*date_value[:3]).strftime('%m/%d/%Y')+"\n")
        # print(sheet1.row_values(i))
        Map[str(id)] = sheet1.cell_value(i,6)
        
    file_in.close()
    file_out.close()
    
    company = []
    for key, value in Map.items():
        if value!="": company.append([key,value])    
    company = sorted(company,key=lambda x:x[1])
    file_company = open("Members/Company.txt", "w")
    for x in company:
        file_company.write(x[0]+" "+x[1]+"\n")
    file_company.close()
    
    print("Load Name List from Excel successfully.")

   
read_excel

