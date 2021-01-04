"""
概要：list2tex_1.2.pyでdxfファイルから作成したリストに対して，
配管クラスの情報(0    TEXT～0 TEXTまでの情報)を抜き取りリスト化する
目的：本プログラムによって作成したリストに対して，（"1\t"で）
検索をかけ配管クラスを引っ張ってくる
"""
import pathlib, os, tkinter, tkinter.filedialog, tkinter.messagebox
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
path12 = pathlib.Path("C:\\users\\田島\\Documents")


# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("",".txt")]
#iDir = os.path.abspath(os.path.dirname(path12))
print(__file__)
#tkinter.messagebox.showinfo('プログラム','処理ファイルを選択してください！')
fd = tkinter.filedialog.askopenfilename(filetype = fTyp, initialdir = path12)

path =  pathlib.Path(fd.replace('/', '\\'))
with open(path, encoding = "utf-8") as dxf_txt:
    lines_list = dxf_txt.readlines()



for a in range(len(lines_list)):
        if lines_list[a] == "2\tENTITIES\n":
            entities = a
            for b in range(len(lines_list)):        
                if b > entities and lines_list[b] == "0\tENDSEC\n":
                    entiend = b
                    break
                                
lines_enti = lines_list[entities:entiend]#ENTITIESのインデックス取得
#print(lines_enti)
list_num = len(lines_enti)
st = "0\tTEXT\n"
target0 = "0\t"
target1 = "1\t"
key = "-"
listIndex =[]
listn = []
listTS = []
row = 1

for i in range(len(lines_enti)):
    if lines_enti[i] == st:
        listIndex.append(i)
try:
    for f in range(len(listIndex)):
        startV = listIndex[f]
        endV = listIndex[f+1]
        for j in range(startV, endV):
            j1 = lines_enti[j]
            listn.append(j1)
except IndexError:
    for f in range(startV,list_num-1):
        j1 = lines_enti[f]
        listn.append(j1)

"""
for k in range(len(listn)):
                    if listn[k].startswith(target1) and listn[k].count(key) >= 2:
                        bi = listn[k]
                        print(bi.strip('\n')) 
                        listTS.append(bi)
"""
#print(listn)

row = col = 1
for i1 in range(len(listn)):
    if listn[i1].startswith(target0):
        row += 1
        col = 1
        ws.cell(row, col, listn[i1])
        col += 1
    else:
        ws.cell(row, col, listn[i1])
        col += 1


wb.save("C:\\Users\\田島\\desktop\\d11e.xlsx")