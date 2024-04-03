class school:
    def func1(self):
        print("this function is in school")
class student1(school):
    def func2(self):
        print("this function is in student 1")
class student2(school):
    def func3(self):
        print("this function is in student 2")
class student3(student1,student2):
    def func4(self):
        print("this function is in student 3")
obj=student3()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
