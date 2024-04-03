class student:
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("roll no:",self.rollno)
        print("name:",self.name)
        print("course:",self.course)
class test(student):
    def getmark(self,mark):
        self.mark=mark
    def displaymark(self):
        print("mark:",self.mark)
r=int(input("enter a rollno:"))
n=input("enter a name:")
c=input("enter a course:")
m=int(input("enter a mark:"))
print("result")
obj=test()
obj.getdata(r,n,c)
obj.getmark(m)
obj.displaystudent()
obj.displaymark()
      
