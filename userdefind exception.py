class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return(repr(self.value))
try:
    raise(MyError(4*5))
except MyError as error:
    print("a new excetion occured:",error.value)
