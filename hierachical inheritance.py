class parent:
    def func1(self):
        print("this function is in parent class")
class child1(parent):
    def func2(self):
        print("this function is in child1 ")
class child2(parent):
    def func3(self):
        print("this function is in child 2")
obj1=child1()
obj2=child2()
obj1.func1()
obj2.func1()
obj1.func2()
obj2.func3()
