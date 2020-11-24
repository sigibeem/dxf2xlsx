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
                    break#breakの位置が不適切なために，aが最初のentitiesからずれてる。（最初のa=6765,最終的なa=62043)
lines_enti = lines_list[entities:entiend]
#print(lines_enti)

st = "0\tTEXT\n"
endi = "0\t"
endii = "1\t"
k = 1
listf1 =[]
num = range(len(lines_enti))
for i in num:
    if lines_enti[i] == st:
        #iwhat = lines_enti[i]
        for f in num:
            if lines_enti[f].startswith(endi) and i < f:
                #fwhat = lines_enti[f]
                listn = lines_enti[i:f]
                for j in range(len(listn)):
                    target = listn[j]
                    if target.startswith(endii):
                        listf1.append(listn[j])
                    #print(listn[j])
                else:
                    k += 1

"""                    break                
keywd = "-" 
listf12 = [i for i in listf1 if i.count(keywd) ==  2]


print(listf12)
"""

fType2 = [("text file," "*.txt")]
fsaveloot = pathlib.Path("C:\\Users\\田島\\Documents")
root = tkinter.Tk()
root.withdraw()
fd2 = tkinter.filedialog.asksaveasfilename(initialdir = fsaveloot, title = "Save as", filetypes = fType2)
path13 = pathlib.Path(fd2.replace('/', '\\'))
with open(path13, "w", encoding="utf-8") as stxt:
    stxt.writelines(listf12)
#wb.save('C:\\users\\田島\\Documents\\de1.xlsx')
