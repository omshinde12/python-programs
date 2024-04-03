import math
a = float(input('Enter 1st side: '))

b = float(input('Enter 2nd side: '))

c = float(input('Enter 3rd side: '))

s = (a + b + c)/2

Area = math.sqrt (s * (s - a) * (s - b) * (s - c))

print("Area of the triangle is %0.2f " %Area)
