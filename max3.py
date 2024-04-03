def max(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(f"the 1st number {n1} is maximum.")
    elif(n2>n1 and n2>n3):
        print(f"the 2nd number {n2} is maximum.")
    else:
        print(f"the 3rd number {n3} is maximum.")
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))
max(n1,n2,n3)
