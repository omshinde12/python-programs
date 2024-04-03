
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def  multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("please select the option ")
print("1.add")
print("2.subtarction")
print("3.multiply")
print("4.divide")

option=(input("enter option"))
x=int(input("enter a first number"))
y=int(input("enter a second number"))

if option=="1":
     print(add(x,y))
elif option=="2":
    print(substract(x,y))
elif option=="3":
    print(multiply(x,y))
elif option=="4":
    print(divide(x,y))

else:
    print("wrong option")

