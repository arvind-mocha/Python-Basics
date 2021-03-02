#creating our own function

def add_sub(x,y):
    add=x+y
    sub=x-y
    return add,sub      #return dont print the value it gives the output we can store it in a variable
                        #then we can nprint the variable
        #else

 #   print(add,sub)      #it directly prints the value you dont need to store it

#answer,answer2=add_sub(x=int(input()),y=int(input()))

#print(answer,answer2)

#learning about function memory
#passing primitive datatypes as parameter[no problem]
def printing(x):
    x=100   #what may be the parameter passed x=100
    print('x',x)

a=20
printing(id(a)) #passing address of a as parameter
print('a',a)
printing(a)     #passing value of a
print('a',a)
print()
#passing parameters like list set dictionary[cause problem]
def listing(lst):
    lst[0]=100  # value is changed and it is reflected in the lst
    print(id(lst))
    print(lst)

lst=[1,2,3]
print(lst)      #before passing as parameter
listing(lst)    #passed as parameter
print(id(lst))
print(lst)      #the value is changed   [remember (deep copy)copy() = diff address same value
                # and (shallow copy)view() = diff address changed value]