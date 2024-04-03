class cal:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y

print("please select the otion")
print('1.addition')
print("2.subtraction")
print("3.multiplication")
print("4.division")
option=int(input("enter your choice:"))
a=int(input("enter first number:"))
b=int(input('enter second number:'))
obj=cal(a,b)
if option ==1:
    print(obj.add())
elif option==2:
    print(obj.sub())
elif option==3:
    print(obj.mul())
elif option ==4:
    print(obj.div())
else:
    print("invalid option")
