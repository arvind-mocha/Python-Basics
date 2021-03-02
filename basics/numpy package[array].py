#discovering numpy package

from numpy import *
#six ways to create an array

#1. array()
arr=array([1,2,3,4],int)#not nessesary to indicate type while using array from numpy
                        # instead of using array package and syntax change in numpy
print(arr)

arr1=array([1,2,3,4.0]) #according to the rule of array every value must be of same type
                        #but here w have a float so every value is converted to float

print(arr.dtype)
print(arr1.dtype)           #dtype is used to find type while using nupy package
arr1=array([1,2,3,4],float) #above line is same to this line
print(arr1.dtype)
print(arr)
print()
#2. linespace

arr=linspace(0,15,3) #linespace is used to seperate the limits into several parts
                     #here the limit 0 to 15 is seperated into three parts that is [0.0 7.5 15.0]
                     #it gives float output since we are seperating into parts

arr1=linspace(0,15)#if you dont specify the no of parts to be seperated then by default 50 parts are created
print(arr)
print(arr1)
print()
#3. arange (not arrange a range)

arr=arange(0,15,2)  # arange is basically used to create a arrray

arr1=range(0,15,2)  #we cant create array using range it is basically used in loops if we dont use it loop
                    #then it is printsd as it is

print(arr)
print(arr1)
print()

#4. logspace
arr=logspace(1,40,5) #it is as like linspace only diference is it prints log value

print(arr[4])   #it prints the log value

print('%.1f' %arr[4])  #it prints the complete value of the log value '%.1f" %arr[] it is
                       #mandatory 1 is for the zero after point it can be value
                       #.f denotes that log is converted into float vlue
print(arr)
print()
#5. ZEROS

arr=zeros(5,int) #it creates an array where all the values are zero by default it gives foat output
print(arr)

#6. ONES

arr=ones(5,int) #it creates array where the values ones by default it gives float output
print(arr)