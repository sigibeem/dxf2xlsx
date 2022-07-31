"概要：dxfファイルをtxtファイルに変換する"


import pathlib
import math
path =  pathlib.Path("../data/design library/FS-MDO-410.dxf")

with open(path, encoding = "utf-8") as f:
    lines = f.readlines()
    lines_strip = [line.strip() for line in lines]
    linesnum = math.ceil(len(lines_strip))
    
i = 0
"""
with open('te_dxf.text', 'x') as g:
    for i in range(linesnum):
        if lines_strip[i] =="EOF":
            break
        g.writelines(lines_strip[i]\t + lines_strip[i+1]\n)
        i = i+2 #+2だとfor文に戻ってきたときに，これが適用されない
"""
try:
    with open('../data/design library/FS-MDO-410.txt', encoding = "utf-8", mode="x") as g:
        for i in range(0, linesnum, 2):
            if lines_strip[i] =="EOF":
                break
            g.write(lines_strip[i]+ '\t' + lines_strip[i+1] +'\n')

        i = i + 1
except FileExistsError:
    print("this file name has already been.")
"""      
with open('../text/text_dxf.text', 'a') as g:
    for i in linesnum:
        g.write(lines_strip[i]+ '\t' + lines_strip[i+1] +'\n')
        
        if lines_strip[i] =="EOF":
            break
        i = i + 2       

with open('../text/text_dxf.text', 'a') as g:
    while lines_strip[i] == "EOF":
        g.write(lines_strip[i]+ '\t' + lines_strip[i+1] +'\n')

        i = i + 2 
"""