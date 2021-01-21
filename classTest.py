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

<<<<<<< HEAD
class Medaka(Fish):
    pass
"""
class Mystack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pull(self):
        a = self.stack[-1]
        del self.stack[-1]
        return a
"""
a = Fish("hi")
a.swim()
a.swim_back()
#print(a.pull())
print(a)
=======
list11 = ["fwe", "fwei", "12fewji", "qwods", "12fewji", "weow", "qwods"]

a = Qlist()
b = a.Sort("12fewji", "q")
print(b)
>>>>>>> b98531725c1b3c14a4d607e21a0a8d7667798ff6
