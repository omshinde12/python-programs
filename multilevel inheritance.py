class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("braking")
class babydog(dog):
    def weep(self):
        print("weeping")
obj=babydog()
obj.eat()
obj.bark()
obj.weep()
