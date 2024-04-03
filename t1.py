def count(t,x):
    return t.count(x)
t=(12,34,67,122,-5,67)
x=122
print('{} has occurred {} times'.format(x,count(t,x)))