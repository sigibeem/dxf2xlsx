listTS = [["12Eji", ], ["12Eji", '13fei', '14Wfe', '15fe'], ['12Eji', '16ewi'], ["12Eji", "14Wfe", "17jifew", "18jfiwe"]]
tarngetlist = ["12E", "14W"]
listonly = []


for i in range(len(listTS)):
    sub = []
    for j in range(len(listTS[i])):
        for k in tarngetlist:
            if listTS[i][j].startswith(k):
                sub.append(listTS[i][j])
    listonly.append(sub)
print(listonly)