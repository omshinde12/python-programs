class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount +=1
    def displaycount(self):
        print("totol employee %d" %Employee.empcount)
    def displayEmployee(self):
        print("name:",self.name ,",salary:",self.salary)
emp1=Employee("om",100000)
emp2=Employee("ram",1000)
emp1.displayEmployee()
emp2.displayEmployee()
print("total employee %d", % Employee.empcout)
    
        
    
