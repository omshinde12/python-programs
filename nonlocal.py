def outer():
    x="local"
    def inner():
       #s nonlocal x
        x="nonlocal"
        print("inner:", x)
    inner()
    print("outer:" ,x)
outer()         