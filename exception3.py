while True:
    try:
        a=int(input("enter an integer:"))
        div=10/a
        break
    except:
        print("error occurred")
        print("please enter valid value:")
    
print("division is :",div)
