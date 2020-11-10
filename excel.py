from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws["A1"] = "iji"
wb.save('C:\\Users\\田島\\Desktop\\test.xlsx')
