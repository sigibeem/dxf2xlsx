import pathlib
list1 = ['0\tTEXT\n', '5\t281\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t642.2\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t符-号\n', '41\t0.75\n', '72\t1\n', '11\t645.0\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n', \
    '0\tTEXT\n', '5\t283\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t661.9125\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t10\n', '41\t0.75\n', '72\t1\n', '11\t672.5\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n', \
        '0\tTEXT\n', '5\t284\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t697.7999999999999\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t12\n', '41\t0.75\n', '72\t1\n', '11\t702.0\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n', \
            '0\tTEXT\n', '5\t285\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t711.2\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t1-5\n', '41\t0.75\n', '72\t1\n', '11\t714.0\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n']

lastt = len(list1)
st = "0\tTEXT\n"
endi = "0\t"
l2 =[] #stのインデックスをリスト化 >>> [0, 20, 40, 60]
l3 =[] 
for i in range(lastt):
    if list1[i] == st:
        l2.append(i)
print(l2)
try:
    for f in range(len(l2)):
        startV = l2[f]
        endV = l2[f+1]
        for j in range(startV, endV):
            j1 = list1[j]
            l3.append(j1)
except IndexError:
    for f in range(startV,lastt-1):
        j1 = list1[f]
        l3.append(j1)
        
print(l3)
