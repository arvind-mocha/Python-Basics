#how to make a variable within function as global
a=100
b=200
print("outside b before overrided",b)
print()
def something():
    global b    #b is within loop but converted into a global variable so it repaces b=200
                #which is also a global but global keyword has high preference
    a=10
    b=20
    print("whithin loop a",a)
    print("whitih loop b",b)

something()
print()

print("outside a",a)

print("outside b",b)    #b outside is 200 but b =20 is within loop and it is printed because
                        #global variable is given high preference
print()







#how to have both global and local variable in same function
a=100
print("global a",a)
def anything():
    a=10

    x=globals()['a']     #it brings all the global variable into local or within function
                         #if you dont want all global just give ["name of variable"] which you want


    print("x which is global a",x)
    print("local a",a)
    print("address of x", id(x))
    x=47                      #now x is local change you do to x does not affect a
    print("address of modified x",id(x)),print(x)

    globals()['a']=59       #parallel to gloabl a=59
    print("globals()['a']=",x)

anything()
print("address of a",id(a)) #both a and x points the same memeory address
print(a)

print()

a=50      #the change you do to a affects x but the change you do to local a does not affect x
anything()


