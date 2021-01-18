class Qlist:
    def Sort(self,target, end):
        num = range(len(list11))
        listTS = []
        for i in num:
            if list11[i] == target:
        #iwhat = list11[i]
                for f in num:
                    if list11[f].startswith(end) and i < f:
                #fwhat = list11[f]
                        listn = list11[i:f]
                        listTS.append(listn)
                        break
        return listTS

list11 = ["fwe", "fwei", "12fewji", "qwods", "12fewji", "weow", "qwods"]

a = Qlist()
b = a.Sort("12fewji", "q")
print(b)