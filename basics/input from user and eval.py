x=input("enter the value")  #basically input() function takes only strings

#two ways to get integer inputs by typecasting

#1.

x=int(input("enter your value"))
x1=float(input("enter your values"))
#2.

y=input("enter your values")
a=int(y)
a1=float(y)

#restricting the input (it is also used to get cahrecter values by seperating strings)

x=set(input("enter the values"))[0:4]   #it takes n no of input but the first 4 is assinged to x

print(x)[0]     #it print only the first number

#eval function

x=eval(int(input("enter the values")))  #this function calculates any arithmatic problem

#Take more than an input:
inputs = []
for i in range(3):  # loop 3 times
	inputs.append(input())
    #or
#In one line:
inputs = [input() for i in range(3)]

#Do you want to split the input?

list_of_inputs = input().split()  # separate by whitespace
list_of_inputs = input().split(',')  # separate by comma
list_of_inputs = input().split('-')  # separate by minus sign

#input in same line
var1, var2, var3 = input().split()#getting strings

r,t=map(int,input().strip().split())#map syntax is map(function,iterables) here int is a function and since we
                                    # give more inputs they acts as iterabls

#converting same line inputs to list
lst=list(map(int,input().strip().split()))#in this way you can also convert to set,tuple ect