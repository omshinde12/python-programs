def rec(s):
    if (len(s)==0):
        return s
    else:
        return rec(s[1:])+s[0]
s=input("enter a string")
if(s==""):
    print("string should not be null")
else:
    rev=rec(s)
    print(rev)
