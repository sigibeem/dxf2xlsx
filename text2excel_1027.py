from openpyxl import Workbook
import pathlib
f_txt = pathlib.Path("C:\\users\\田島\\desktop\\prelist.txt")

with open(f_txt, encoding="utf-8") as pre:
    pretxt = pre.readlines()
print(pretxt)

#pre_txt2 = replace

