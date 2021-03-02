#getting array inputs from user
from array import *

arr=array('i',[])#since we dont know the size jut declare it

n=int(input("enter the array size"))

for i in range(n):
    a=int(input("enter the values in array"))
    arr.append(a)               #append inserts value into array one by one

print(arr)

#searching linear manual

x=int(input(("enter the value you need")))
count=0
for i in arr:
    if x==i:
        print(count)
        break
    count=count+1
else:
    print("not found")

#serching using index function
print(arr.index(x))

#reverse the array without using function
arr1=array('i',[])
for i in range(n-1,-1,-1):
    arr1.append(arr[i])

print("reverse of arr"),print(arr1)







