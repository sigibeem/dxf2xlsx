"""
概要：list2tex_1.2.pyでdxfファイルから作成したリストに対して，
配管クラスの情報(0    TEXT～0 TEXTまでの情報)を抜き取りリスト化する
目的：本プログラムによって作成したリストに対して，（"1\t"で）
検索をかけ配管クラスを引っ張ってくる
"""
<<<<<<< HEAD

import pathlib, os, tkinter, tkinter.filedialog, tkinter.messagebox, tkinter.filedialog
=======
import pathlib, os, tkinter, tkinter.filedialog, tkinter.messagebox, math
>>>>>>> fefe
from openpyxl import Workbook

#filename = input("design library内のdxfファイル名(拡張子を除く）を指定してください:")
#savename = input("txtファイルとして保存する際の名前（拡張子を除く）を記入してください:")
""" #dxf2txtを行おうとしている
path =  pathlib.Path("C:\\Users\\田島\\Documents\\py\\data\\design library\\図枠と_EFD_textのみ.dxf")

with open(path, encoding = "utf-8") as f:
    lines = f.readlines()
    lines_strip = [line.strip() for line in lines]
    linesnum = math.ceil(len(lines_strip))

try:
    with open("C:\\Users\\田島\\Documents\\py\\data\\design library\\図枠と_EFD_textのみ.txt", encoding = "utf-8", mode="x") as g:
        for i in range(0, linesnum, 2):
            if lines_strip[i] =="EOF":
                break
            g.write(lines_strip[i]+ '\t' + lines_strip[i+1] +'\n')

except FileExistsError:
    print("this file name has already been.")
"""

wb = Workbook()
ws = wb.active
path12 = pathlib.Path("C:\\users\\田島\\Documents")
<<<<<<< HEAD
=======
listonly = []
>>>>>>> fefe

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("",".txt")]
#iDir = os.path.abspath(os.path.dirname(path12))
<<<<<<< HEAD
#print(__file__)
=======

>>>>>>> fefe
#tkinter.messagebox.showinfo('プログラム','処理ファイルを選択してください！')
fd = tkinter.filedialog.askopenfilename(filetype = fTyp, initialdir = path12)

path =  pathlib.Path(fd.replace('/', '\\'))
with open(path, encoding = "utf-8") as dxf_txt:
    alldxf = dxf_txt.readlines()


#ENTITIESのインデックス取得

for a in range(len(alldxf)):
        if alldxf[a] == "2\tENTITIES\n":
            entities = a
            for b in range(len(alldxf)):        
                if b > entities and alldxf[b] == "0\tENDSEC\n":
                    entiend = b
                    break
<<<<<<< HEAD
lines_enti = lines_list[a:b]
#print(lines_enti)

st = "0\tTEXT\n"
endi = "0\t"
k = 1
num = range(len(lines_enti))

list23 =[]
for i in num:
    if lines_enti[i] == st:
        print(type(lines_enti))
        #iwhat = lines_enti[i]
        for f in num:
            if lines_enti[f].startswith(endi) and i < f:
                #fwhat = lines_enti[f]
                listn = lines_enti[i:f]
                list23.append(listn[8])#8番目が必ずライン名ではない。そのため，インデックス指定ではなくstarwith("1/t")で指定

print(list23)
print("end")

                
=======
dxf_enti = alldxf[entities:entiend]#dsf_enti=dxfファイルのentities箇所の抜粋
#print(dxf_enti)
class Qlist:
    def Sort(self,target, end,targetlist):
        num = range(len(dxf_enti))
        listTS = []
        listonly = []
        for i in num:
            if dxf_enti[i] == target:
        #iwhat = dxf_enti[i]
                for f in num:
                    if dxf_enti[f].startswith(end) and i < f:
                #fwhat = dxf_enti[f]
                        listn = dxf_enti[i:f]
                        listTS.append(listn)
                        break
        for i in range(len(listTS)):
            sub = []
            for j in range(len(listTS[i])):
                for k in targetlist:
                    if listTS[i][j].startswith(k):
                        sub.append(listTS[i][j])
            listonly.append(sub)
        return listonly

Ttargetlist = ["8\t", "10\t", "20\t", "30\t", "1\t", "11\t", "21\t", "31\t"]
Ltargetlist = ["8\t", "10\t", "20\t", "90\t"]
a = Qlist()
b = a.Sort("0\tTEXT\n", "0\t", Ttargetlist)
c = a.Sort("0\tLINE\n", "0\t", Ltargetlist) 
>>>>>>> fefe

list13 = []
for i in range(len(c)):#図枠の位置データ採取
    for j in range(len(c[i])):
        if c[i][j] == "8\t図枠\n":
            list13.append(c[i][1:])
            break

print(list13)
#print(listonly)
"""excelへのテキスト（ライン情報）のみの転写
for i in range(len(listonly)):
    for j in range(len(listonly[i])):
        ws.cell(i+1, j+1, listonly[i][j])
wb.save("C:\\Users\\田島\\desktop\\di.xlsx")　
"""
