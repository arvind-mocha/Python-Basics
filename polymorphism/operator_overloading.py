#behind arithmatic operation

x=10
y=20

print(x+y)#this what we do

print(int.__add__(x,y))#this what happens background add function is called

class oper():

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):    #operator overloading[addition]
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=oper(m1,m2)
        return m3
    def __gt__(self, other):     #operator overloading[greater than]
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        if m1 > m2:
            True
        else:
            False

    def __str__(self):  #operator overloading printing values of object not its address
        return "{} {}".format(self.m1,self.m2)#format is a inbuilt function which fills value inside {}


obj=oper(25,35)
obj1=oper(45,55)

m=obj+obj1  #add two objects wont work because datatypes know what is + but your class instances dont know
            #so __add__ method is defined

print(m.m1,m.m2)

if obj.m1 > obj.m2:           #it wont work because the > is not known by the by the class object
                              #so create a __gt__ function
    print("m1 is greater")
else:
    print("m2 is greater")

a=20
print(a) #value of a is printed notthe address of a[this we do]
print(a.__str__())#this what happens in the background
print()
print(obj)  #but while you print object the address of the object is printed not its value[this we do]
print(obj.__str__())#this what happens in the background so define a function __str__


