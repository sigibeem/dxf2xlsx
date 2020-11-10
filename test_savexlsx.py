list12 = ('20\t584.0\n', '0\tLINE\n', '5\tAE(1)\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠-仕様欄\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbLine\n', '10\t35.0\n', '20\t15.0\n', '30\t0.0\n', '11\t600.0\n', '21\t15.0\n', '31\t0.0\n', '0\tLINE\n', '5\tAF\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠-仕様欄\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbLine\n', '10\t35.0\n', '20\t20.0\n', '30\t0.0\n', '11\t600.0\n', '21\t20.0\n', '31\t0.0\n', '0\tLINE\n', '5\tB0(2)\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠-仕様欄\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbLine\n', '10\t35.0\n', '20\t25.0\n', '30\t0.0\n', '11\t600.0\n', '21\t25.0\n', '31\t0.0\n')

import openpyxl
wb = openpyxl.Workbook()
ws = wb.active

#print(dir(ws))
k = 1
st = "0\tLINE\n"
endi = "0\t"
num = range(len(list12))
for i in num:
    if list12[i] == st:
        #iwhat = list12[i]
        for f in num:
            if list12[f].startswith(endi) and i < f:
                #fwhat = list12[f]
                listn = list12[i:f]
                for j in range(len(listn)):
                    ws.cell(k,j+1,listn[j])
                    #print(listn[j])
                else:
                    k += 1
                    break                
                    
    
wb.save('C:\\users\\田島\\Documents\\de.xlsx')