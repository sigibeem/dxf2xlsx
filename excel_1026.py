import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
list1 = ["jij", "jie", "jiwqod", "fwe"]
ll = len(list1)

for i in range(ll):
    ws.cell(i+1, 1, list1[i])
        

wb.save('C:\\Users\\田島\\Desktop\\test_list.xlsx')
"""
1026
ディレクトリ上にエクセルファイルの作成を確認
"""
