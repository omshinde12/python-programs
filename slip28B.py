def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
lst1=[1,2,3,5]
lst2=["SMBST","Sangamner"]
t1=tuple(lst1)
t2=tuple(lst2)
t3=t1 + t2
print(t3)
