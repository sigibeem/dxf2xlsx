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


# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("",".txt")]
iDir = os.path.abspath(os.path.dirname(__file__))
print(__file__)
#tkinter.messagebox.showinfo('プログラム','処理ファイルを選択してください！')
fd = tkinter.filedialog.askopenfilename(filetype = fTyp, initialdir = iDir)

path =  pathlib.Path(fd.replace('/', '\\'))
with open(path, encoding = "utf-8") as dxf_txt:
    lines_list = dxf_txt.readlines()


#ENTITIESのインデックス取得

for a in range(len(lines_list)):
        if lines_list[a] == "2\tENTITIES\n":
            entities = a
            for b in range(len(lines_list)):        
                if b > entities and lines_list[b] == "0\tENDSEC\n":
                    entiend = b
                    break
lines_enti = lines_list[entities:entiend]
#print(lines_enti)

num = range(len(lines_enti))
for i in num:
    if lines_enti[i] == "0\tTEXT\n":
        for f in num:
            if "0\t" in lines_enti[f] and i < f:
                print(lines_enti[i:f]) 
                break

    
wb.save('C:\\Users\\田島\\Desktop\\dekiteru1027.xlsx')

"""
num = len(lines_enti)
b = "100\tAcDbText\n"
for i in range(num):
    if lines_enti[i] == "b":
        e = i
        for f in range(num):
            if lines_enti[f] =="b" and f > i:
                s = f
                print(lines_enti[e+1:f])
                break
            elif f == num-1:
                print(lines_enti[e+1: ])

"""
"""
for a in range(len(lines_list)):
        if lines_list[a] == "2\tENTITIES\n":
            entities = a
for b in range(len(lines_list)):        
        if b > entities and lines_list[b] == "0\tENDSEC\n":
            entiend = b
            break
lines_enti = lines_list[entities:entiend]
print(lines_enti)

num = len(lines_enti)
b = "100\tAcDbText\n"
for i in range(num):
    if lines_enti[i] == "b":
        e = i
        for f in range(num):
            if lines_enti[f] =="b" and f > i:
                s = f
                print(lines_enti[e+1:f])
                break
            elif f == num-1:
                print(lines_enti[e+1: ])

"""
"""
1005 resolved
a=6765, need b = 49260 but hit b =49260, 61946, 62043
lines_nlist = [i for i in lines_list if lines_list[entities] % 2 == 0]
"""
"""
LLOO = lines_list[entities:entiend]
#with open('../data/design library/line_list_object_only.txt', encoding = "utf-8", mode="x") as llOO:
 #   llOO.writelines(LLOO)
print(len(LLOO))

LLTO = []
for i in LLOO:
    if LLOO[i] == "100\tAcDbText\n":
        i = "st"
"""        