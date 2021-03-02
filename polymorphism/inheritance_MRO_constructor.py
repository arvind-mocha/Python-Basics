#inheritance

class A:
    def __init__(self):
        print("i am init from a")

    def one(self):
        print("i a from one-a")

    def two(self):
        print("i am from two-a")

class B:
    def __init__(self):
        print("i am init from b")

    def one(self):
        print("i am from one-b")

    def two(self):
        print("i am from two-b")

class C(A,B):                   #class C inherits both A and B
    def __init__(self):
        super().__init__()      #here MRO[Method Resolution Order] comes into picture
                                #since C inherits both A and B both are its super class
                                #but it prints only the thing in super class A since it is inherited first
                                #or it is in left side C(A,B) and this is Method Resolution Order
        
        print("i am init from c")

    def three(self):
        super().one()           #there are two function named the same as one but
                                #things in function B is not printed things in
                                #function A is only printed because of MRO[Method Resolution Order]
        print("i am from three")

obj=C()
print()
obj.three()