class string1:
    def get_string(self):
        self.s=input("enter a string:")
    def print_string(self):
        print("string is:",self.s.upper())
        print("reverse:",self.s[::-1])
obj=string1()
obj.get_string()
obj.print_string()
    

        
