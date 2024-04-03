class csstudent:
    stream="cse"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
a=csstudent("om",20)
b=csstudent("ram",21)
print(a.name)
print(a.roll)
print(b.name)
print(b.roll)
print(a.stream)
print(b.stream)
print(csstudent.stream)
