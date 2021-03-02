#there is no method overloading concept in python we cant have functions with same name is same class

#method overriding

class a:
    def mybike(self):
        print("i have duke")

class b(a):                         #class b inherits a so b contains two mybike function
    def mybike(self):
        print("i have bugati")

obj=b()
obj.mybike()    #method mybike of (a) is overrided by method mybike of (b)