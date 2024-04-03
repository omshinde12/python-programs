def factors(x):
   
   for i in range(1,x+1):
       if x%i==0:
           print(i)
   print("the factors of ",x,"are:")
num=int(input("enter a number:"))
factors(num)
   
    
        
