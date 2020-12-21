class Fish:
    def __init__(self, name, build="ほね", eyelids=False):
        self.name = name
        self.build = build
        self.eyelids = eyelids
    def swim(self):
        print("こちらの魚は泳ぎます")
    def swim_back(self):
        print("こちらの魚は後ろ向きにも泳ぎます")

class Medaka(Fish):
    pass

class Mystack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pull(self):
        a = self.stack[-1]
        del self.stack[-1]
        return a
a = Mystack()
a.push(1)
a.push(2)
print(a.pull())
print(a)