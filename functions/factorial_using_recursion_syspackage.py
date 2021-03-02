#factorial using for loop
lst=[]

def fact(x):
    mul=1
    for i in range(x,0,-1):
        mul = i * mul
        lst.append(i)
    return lst,mul


lst,mul=fact(int(input("enter the value")))
print(lst),print("fact of x =",mul)


#recurssion
import sys

sys.setrecursionlimit(2000)            #by default it runs 1000 times now it runs for 2000 times

print(sys.getrecursionlimit())          #it prints the no of execution time
def rec():
    print("hello")
    rec()                   #there is no limit for recurssion so it runs infinte time but python limits infinite to 1000

rec()


#factorial using recursion

def fact1(n):
    if n==0:
        return 1

    return n * fact1(n-1)

ans=fact1(int(input("enter the value")))
print(ans)

