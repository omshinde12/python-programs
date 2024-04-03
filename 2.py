str=input("enter string:")
print(str)
count=0
for i in str:
    count=count+1
    print(count)
    if count<2:
        print("empty string")
else:
    new=str[0:2]+str[count-2:count]
    print("newly formed is:",new)
        