import pathlib

path =  pathlib.Path("../data/design library/FS-MDO-410.txt")
with open(path, encoding = "utf-8") as dxf_txt:
    lines_list = dxf_txt.readlines()


#ENTITIESのインデックス取得
for a in range(len(lines_list)):
    if lines_list[a] == "2\tENTITIES\n":
        break
print(a) #a=6765
entities = a    
for b in range(len(lines_list)):        
    if b > entities and lines_list[b] == "0\tENDSEC\n":
        break
"""        
print(b)
for c in range(len(lines_list)):
    if a < c and c < b and "0\t" in lines_list[c]:
"""
#with open('../data/design library/FS-MDO-410_object-only.txt', encoding = "utf-8", mode="x") as oo:
print(lines_list[entities])