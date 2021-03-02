class ages:

    def __init__(self,name):         #self points the current object

        print("whats your age") #there is no connection between self and print statment when n no
                                #of obj is created n no of print statments are printed at that instance itself
                                #once it is printed its function is over it is not executed again when
                                #next object is called

        self.age=20             #since it is a constructer it belongs to each object so self.variable is must
        self.name=name

    def compare(self,x):
        if self.age == x.age:
            return True
        else:
            return False




obj1=ages("kumar")#now self = obj1
obj2=ages("vidyuth")#now self = obj2



obj1.age=25

if obj1.compare(obj2): #self points obj1 since function is called for obj1 and obj2 is passed as parameter
    print("both age are same")
else:
    print("they differ in age")

print("age of",obj1.name,"which belongs to [object 1] =",obj1.age)
print("age of",obj2.name,"which belongs to [object 2] =",obj2.age)
print()

obj2.age=25




if obj2.compare(obj1): #self points obj2 since function is called for obj2 and obj1 is passed as parameter
    print("both age are same")
else:
    print("they differ in age")

print("age of",obj1.name,"which belongs to [object 2] =",obj1.age)
print("age of",obj2.name,"which belongs to [object 1] =",obj2.age)