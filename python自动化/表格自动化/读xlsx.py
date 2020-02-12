import xlrd
xlsx = xlrd.open_workbook("D:/BaiduNetdiskDownload/【完结】用Python自动办公，做职场高手/章节05：S3 PPT自动化处理，用程序快速排版/课时45【真实案例】3.8 项目  最近很火的数据动图，怎么用Python做/样例：生成数据动图/data_source.xlsx")
table = xlsx.sheet_by_index(0) 
# table = xlsx.sheet_by_name("sheet2")

#读
print(table.cell_value(1, 2))
print(table.cell(1, 2).value)
print(table.row(1)[2].value)

