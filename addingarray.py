import array as arr

a = arr.array("i",[2,3,4,5])
print("array before insertion:",end=" ")
for i in range(0,7):
    print(a[i],end = " ")
print()
a.insert(1,10)
print("array after insertion:",end=" ")
for i in (a):
    print(i,end = " ")
print()