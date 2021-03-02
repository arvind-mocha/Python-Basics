# 2D array = multiple list inside a numpy.array function
from numpy import *

arr=array([[1,2,3,5,12,13],[8,9,6,7,10,11]])#2D array =[[],[]] inside a array there are two array [you can add more array]

print(arr.ndim) #ndim = no of dimensions it gives the array dimension

print(arr.shape)#it gives the no of rows and colum in the array herit is (2,3)

print(arr.size)#it gives the total no of elements in the array

arr1=arr.flatten() #it converts any dimensional array into a single dimensional array
print(arr1)
print()

arr2=arr1.reshape(3,4)#it converts 1D array into multidimensional array
                      #here we are converting a 1D array into 3D array
                      #for convertion first we must have the required no of elements
                      #here we need 12 elements since (3,4) is 12
print(arr2)
print(),print(),print()


arr3=arr1.reshape(2,2,3)#it means 2 2D array with 2 rows and 3 columns
                        #first 2 is no of array second 2 is no of rows and the 3 is no of column
print(arr3)
print()
#matrix function
m=matrix(arr)#it gives a matrix but the output will me same a you print arr
print(m)
print()

m=matrix('1,2,3;4,5,6;7,8,9')#real use of matrix function
m1=matrix('1,2,3;4,5,6;7,8,9')
print(m)
print()
print(m1)
print()

print(m.diagonal())#diagonal() is used to print the diagonal elements in the matrix
print()
#you can also perform operation that you perform with normal array like

print(m.max())
print(m.min())
print(m.flatten())
print(m.size)
print(m.ndim)
print()
#matrix arithmetic operations
m2=m+m1
print(m2)

print()

m2=m-m1
print(m2)

print()

m2=m*m1
print(m2)
print()

m2=m//m1
print(m2)

