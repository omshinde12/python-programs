def getgcd(a,b):
    if(b==0):
        return a
    else:
        return getgcd(b,a%b)
a=int(input("enter value for 1st number;"))
b=int(input("enter value for 2nd number:"))
gcd=getgcd(a,b)
print("gcd is:",gcd)
    
