age=int(input("enter your age for election:"))
try:
    if age<18:
        raise Exception
    else:
        print("you are eligible for election")
except Exception:
    print("this value is to small,try again")
