class Rectangle:
 def __init__(self, l, w):
     self.length = l
     self.width = w
 def rectangle_area(self):
     return self.length*self.width
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
