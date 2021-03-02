#functions in numpy
#what if you want to multiply by 5 to all values in your array
from numpy import *
arr=array([1,6,3,2,5])

arr = arr * 5

print(arr)

#sort
arr.sort()
print(arr)

#concat

arr1=array([0,9,8])

arr=concatenate([arr,arr1])

print(arr)

#find min and max

print(min(arr)),print(max(arr))

            #before array understand a simple variable

x=100        #this three have the same address it meanes no new memeory is allocated if we change value of y
y=100        # then y is in new address but z and x are still in sam address
z=x
print(id(x))        #id is a function which gives the address of the paramter

print(id(y))        # python have good memeory management algorithm

print(id(z))

z=1
print(id(z)) #address of z changes
print()
#copying a array into another array [memory management]

arr=array([1,2,3,4])

arr1=arr    #stored in same memory address this is known as [aliasing]

print(id(arr))  #both have same address arr and arr1 [point to the same memory address]
                #so when you edit a array it affects the other array since both are in same memory address
print(id(arr1))

arr[1]=6
print(arr),print(arr1)  #value is changed for both arrays

arr1[3]=20
print(arr),print(arr1)  #value i changed for both arrays
print()
#this happens in array not to a single varialbe so to overcome this we have two types of copy

#1. shallow copy
arr1=arr.view()
print(id(arr)),print(id(arr1)) #here both are in different memory address

arr1[2]=100
print(arr1)
print(arr)
                #but they are still depentdent on each other when changes happen to a array
                #the other array also gets affected
arr[1]=29
print(arr)
print(arr1)
print()
#2. deep copy
arr1=arr.copy()
print(id(arr)),print(id(arr1))   #here both are in different memory address

arr1[0]=59
print(arr1)
print(arr)
                #they are not dependent on each other
                #changes made in a array does not affect the other array
arr[3]=99
print(arr),print(arr1)

