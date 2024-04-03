try:
    a=10/0
except ArithmeticError ,StandardError:
    print("arithmetic exception")
else:
    print("successfully done")
