#detail about arguments

def add(a,b): #this is known as formal arguments
    c=a+b
    print(c)
    print()
add(5,6)        #this is known as actual arguments
                #there are four types of actual arguments
                #this is position arguments a=5 and b=6

#what if you dont know the positoin

add(b=7,a=6)#this is known as keyword argument


#what if you dont give value to a parameter passed in formal argument
def add1(a,b=12):#this ids known as default argument
    print(a+b)


add1(1)
add1(1,2)   #if you also pass the value in actual parameter b=18 is overrided
print()



#what if you pass n no of paramter[varialble length]
def add2(a,*b):  #*b is a tuple

    print(a)#a=first value
    print(b)#b=all value except first position

    for i in range(len(b)):
        c=0
        c=a+b[i]
        print(c,end=" ")
        print()

add2(1,2,3,4)
print()
#in variable length you dont know for waht you are passing value so we use[key variable length]
def printing(a,**b): #**b allows to have tuple and key
    print(a)
    print(b)

printing(1,age=28,name='meghan',mob=8986759)    #age ,name ,mob are keys
                                                #in normal tuple you cant do this



