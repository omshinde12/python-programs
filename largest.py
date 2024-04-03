x=int(input("enter a first number:"))
y=int(input("enter a second number:"))
z=int(input("enter a third number:"))
if(x>=y) and(x>=z):
    largest=x
elif (y>=x)and(y>=z):
     largest=y
else:
 largest=z
print("the larges number between",x ,"," ,y,"and",z,"is",largest)
