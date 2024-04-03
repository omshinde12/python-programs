num=int(input("enter a number:"))
fact=1
if num<0:
    print("sorry factorial is  does not exist for negative number")
elif num==0:
    print("the zeroo factorial is 1")
else:
    for i in range(2,num+1):
        fact=fact*i
    print("factorail is",fact)
