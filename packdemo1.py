import mypack.p1,mypack.p2 # package import 1st method
mypack.p1.m1()
mypack.p2.m2()
from  mypack.p1 import m1 #package import 2nd method
m1()
from mypack.p1 import m1 as function #package 3rd mrthod
function()
from mypack import p1,p2
p1.m1()
p2.m2()

