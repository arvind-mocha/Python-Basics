

def fib(x,y):
    lst = [0]
    sum = 0
    sum1 = 1
    z=0
    for i in range(1,x+1):
        if x==1:        #this is to reduce iteration since if x=1 it does not do calculations
            print(sum)
            break

        elif(x < 0):
            print("give positive values")

        else:           #gives the range of fibanoci number
            sum2=sum+sum1
            sum=sum1
            sum1=sum2
            lst.append(sum)
        if i==y:
            z= sum
    print(lst),print("fib value of",y,"=",z)


#fib(int(input("enter the range")),int(input("enter the no to get fib no")))

