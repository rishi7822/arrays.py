import array as arr

arr = arr.array("i",[2,4,5,6,7,8,2,2])
print("Array before updation:",end=" ")
for i in range(0,8):
    print(arr[i],end=" ")

print("/r")

#updating array
arr[2]=10
print("Array after updation:",end="")
for i in range(0,8):
    print(arr[i],end="")
    print()



arr[4]=100
print("Array after updation:",end="")
for i in range(0,8):
    print(arr[i],end="")
    print()