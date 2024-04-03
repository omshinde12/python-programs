class accept:
    def getdata(self):
        self.x=input("enter a string:")
    def putdata(self):
        print("string is:",self.x)
a=accept()
a.getdata()
a.putdata()
class country:
    def getna(self):
        self.c=input("enter a country:")
        self.n=input("enter a nationality:")
    def printnationality(self):
        print("country is:",self.c)
        print("nationality is:",self.n)
class state(country):
    def getstate(self):
        self.s=input("enter a state:")
    def printstate(self):
        print("state is :",self.s)
b=state()
b.getna()
b.printnationality()
b.getstate()
b.printstate()
