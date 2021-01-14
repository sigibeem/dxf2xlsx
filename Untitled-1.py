list1 = [["ji", ], ["ji", 'fei', 'fe', 'fe'], ['ji', 'ewi'], ["ji", "few", "jifew", "jfiwe"]]
list12 = []


for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] == "ji":
            sub = []
            sub.append(list1[i][j])
    list12.append(sub)
print(list12)