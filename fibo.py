a=0
b=1
n=int(input("enter term of fibonacci series\n"))
for i in range(1,n+1):
    print(a,end="  ")
    c=a+b
    a=b
    b=c

    
