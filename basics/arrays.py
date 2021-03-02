# the value in arrays must be in same type o first we must tell the type of value
#python dont have array all are list,list are fed into function array from array or numpy
# check this https://docs.python.org/3/library/array.html

from array import *

x = array('i', (1, 2, 3, 4, 5))  # i=int only accepts int

print(x.buffer_info())  # it gives the address of the array and size of the array
print(x.typecode)       #to check type of the array
print(x)
x.reverse()             #to reverse the value cant print this as it is
print(x)
y = array(x.typecode,(b*b for b in x))  #instead of copying value in x and pasting in y we can do this
                                        #x.typecode gives 'i' the for loop takes each value from x paste it to y
                                        #instead of b you can give anything you can even perform operations to the
                                        #value which is being copied [understand in this way] important
print(y),print(x)
print()

#getting array inputs from user
arr=array('i',[])#since we dont know the size jut declare it

n=int(input("enter the array size"))

for i in range(n):
    a=int(input("enter the values in array"))
    arr.append(a)               #append inserts value into array one by one

print(arr)

#If the numbers are provided in same line then you can use,

arr = list(map(int, input().split()))

#If inputs are in different lines then,

arr = [ int(input()) for i in range(n)]


