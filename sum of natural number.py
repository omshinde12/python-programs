num=int(input("enter a number:"))
if num<0:
    print("enter a positive number")
else:
    sum=0
    for i in range(1,num+1):
        sum+=i
    print(sum)
