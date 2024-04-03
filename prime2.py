def checkprime(m):
 if m>1:
    for i in range(2,m):
      if(m%i)==0:
             print("number is not prime")
             break
    else:
                print("number is prime")
 else:
        print("not prime")
num=int(input("enter a number:"))
checkprime(num)

