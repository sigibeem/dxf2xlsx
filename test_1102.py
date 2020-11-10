"""
概要：lsit1027から"b\t12"の（0\tTEXTと想定）の後のデータのみソートさせる
目的：entitiesの中のtextのみソートさせる。これによって，lineの情報などが消えると想定される。
"""

from openpyxl import Workbook
import pathlib

wb = Workbook()
ws = wb.active

list1027 = ('20\t584.0\n', '0\tLINE\n', '5\tAE\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠-仕様欄\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbLine\n', '10\t35.0\n', '20\t15.0\n', '30\t0.0\n', '11\t600.0\n', '21\t15.0\n', '31\t0.0\n', '0\tLINE\n', '5\tAF\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠-仕様欄\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbLine\n', '10\t35.0\n', '20\t20.0\n', '30\t0.0\n', '11\t600.0\n', '21\t20.0\n', '31\t0.0\n', '0\tLINE\n', '5\tB0\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠-仕様欄\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbLine\n', '10\t35.0\n', '20\t25.0\n', '30\t0.0\n', '11\t600.0\n', '21\t25.0\n', '31\t0.0\n')#tupleにすることで，startswithが使用可能になり指定範囲（最終的には'0\tTEXT\n'，今回は'0\tLINE\n'）のソートが可能になった



print(type(list1027))

st = "0\tLINE\n"
endi = "0\t"
num = range(len(list1027))
for i in num:
    if list1027[i] == st:
        iwhat = list1027[i]
        for f in num:
            if list1027[f].startswith('0\t') and i < f:
                fwhat = list1027[f]
                print(list1027[i:f]) 
                break

