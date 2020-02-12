import xlwt

#写

new_workbook = xlwt.Workbook()
workSheet = new_workbook.add_sheet('new_sheet')
workSheet.write(0, 0, 'test')

new_workbook.save('d:/test.xlsx')
