"""
概要：list2tex_1.2.pyでdxfファイルから作成したリストに対して，
配管クラスの情報(0    TEXT～0 TEXTまでの情報)を抜き取りリスト化する
目的：本プログラムによって作成したリストに対して，（"1\t"で）
検索をかけ配管クラスを引っ張ってくる
"""

import pathlib, os, tkinter, tkinter.filedialog, tkinter.messagebox, tkinter.filedialog
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
path12 = pathlib.Path("C:\\users\\田島\\Documents")

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("",".txt")]
#iDir = os.path.abspath(os.path.dirname(path12))
#print(__file__)
#tkinter.messagebox.showinfo('プログラム','処理ファイルを選択してください！')
fd = tkinter.filedialog.askopenfilename(filetype = fTyp, initialdir = path12)

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
lines_enti = lines_list[a:b]
#print(lines_enti)

st = "0\tTEXT\n"
endi = "0\t"
k = 1
num = range(len(lines_enti))
lines_entit = tuple(lines_enti)
for i in num:
    if lines_entit[i] == st:
        print(type(lines_entit))
        #iwhat = lines_entit[i]
        for f in num:
            if lines_entit[f].startswith(endi) and i < f:
                #fwhat = lines_entit[f]
                listn = lines_entit[i:f]
                print(listn)
                list23 =[]
                list23.append(listn[8])

print("end")

                

