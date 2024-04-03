def fun1():
    print("outer class")
    def fun2():
        print("inner class")
    fun2()
fun1()        
