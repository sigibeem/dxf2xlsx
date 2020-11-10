"""
概要：lsit1027から"b\t12"の（0\tTEXTと想定）の後のデータのみソートさせる
目的：entitiesの中のtextのみソートさせる。これによって，lineの情報などが消えると想定される。
"""

from openpyxl import Workbook
import pathlib

wb = Workbook()
ws = wb.active

list1027 = ["b\t12", "jiji", "de", "b\t13", "ed", "eji", "b\t98", "fwae", "b\t12", "fejae", "b\t311", "fewi"]
#print(list1027[0])

num = range(len(list1027))
for i in num:
    if list1027[i] == "b\t12":
        for f in num:
            if "b\t" in list1027[f] and i < f:
                print(list1027[i:f]) 
                break
