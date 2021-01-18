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
targetlist = ["8\t", "10\t", "20\t", "30\t", "1\t", "11\t", "21\t", "31\t"]
listonly = []

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
    alldxf = dxf_txt.readlines()


#ENTITIESのインデックス取得

for a in range(len(alldxf)):
        if alldxf[a] == "2\tENTITIES\n":
            entities = a
            for b in range(len(alldxf)):        
                if b > entities and alldxf[b] == "0\tENDSEC\n":
                    entiend = b
                    break
dxf_enti = alldxf[entities:entiend]#dsf_enti=dxfファイルのentities箇所の抜粋
#print(dxf_enti)

st = "0\tTEXT\n"
endi = "0\t"
k = 1
listTS =[]
num = range(len(dxf_enti))
for i in num:
    if dxf_enti[i] == st:
        #iwhat = dxf_enti[i]
        for f in num:
            if dxf_enti[f].startswith(endi) and i < f:
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
#print(listonly)
"""excelへのテキスト（ライン情報）のみの転写
for i in range(len(listonly)):
    for j in range(len(listonly[i])):
        ws.cell(i+1, j+1, listonly[i][j])
wb.save("C:\\Users\\田島\\desktop\\di.xlsx")　
"""
