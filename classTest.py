class Qlist:
    def Sort(self,target, end,targetlist):
        num = range(len(list11))
        listTS = []
        listonly = []
        for i in num:
            if list11[i] == target:
        #iwhat = list11[i]
                for f in num:
                    if list11[f].startswith(end) and i < f:
                #fwhat = list11[f]
                        listn = list11[i:f]
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

list11 = ['0\tTEXT\n', '5\t281\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t642.2\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t符-号\n', '41\t0.75\n', '72\t1\n', '11\t645.0\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n', \
    '0\tTEXT\n', '5\t283\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t661.9125\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t10\n', '41\t0.75\n', '72\t1\n', '11\t672.5\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n', \
        '0\tTEXT\n', '5\t284\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t697.7999999999999\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t12\n', '41\t0.75\n', '72\t1\n', '11\t702.0\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n', \
            '0\tTEXT\n', '5\t285\n', '330\t18\n', '100\tAcDbEntity\n', '8\t図枠\n', '6\tContinuous\n', '62\t253\n', '100\tAcDbText\n', '10\t711.2\n', '20\t29.5\n', '30\t0.0\n', '40\t3.5\n', '1\t1-5\n', '41\t0.75\n', '72\t1\n', '11\t714.0\n', '21\t31.25\n', '31\t0.0\n', '100\tAcDbText\n', '73\t2\n']

feji = ["8\t", "10\t", "20\t", "30\t", "1\t", "11\t", "21\t", "31\t"]
a = Qlist()
b = a.Sort("0\tTEXT\n", "0\t", feji)
print(b)