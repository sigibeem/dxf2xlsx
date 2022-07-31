class MyClass:
    CLASS_PARM = 100
    def __init__(self, instance_parm):
        self.instance_parm = instance_parm
    @classmethod
    def method(cls):
        print(cls.CLASS_PARM)
    
    @staticmethod
    def method_2(param):
        print("Static!!", param)
MyClass.method_2("hi")