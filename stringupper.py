class string:
    def getstring(self):
        self.s=input("enter:")
    def display(self):
        print(self.s.upper())
        print(self.s[::-1])
obj=string()
obj.getstring()
obj.display()
        
