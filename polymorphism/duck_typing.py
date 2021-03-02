#duck typing is only available in python not in any other language

class myide:
    def func(self):
        print("best software")
        print("code shinker")
        print("help support")

class oldide:
    def func(self):
        print("inbuilt functions")
        print("graphics")

class user:
    def usage(self,x):#you are passing a variable which is a object
        print("i like your ide because you have")
        work.func()     #calling the function func[but there are two function named func in different class]
                        #the first object is created to the class myide so for the first time
                        #this function func is called for myide then for the oldide

work=myide()
obj=user()
obj.usage(work)#this work is object of myide

print()

work=oldide()
obj=user()
obj.usage(work)#this work is object of oldide

#concept of duck typing

        #n no class may have function with same name
        #but all functions ma not have same things
        #if you want the help of any funtion you can call it no matters whats their name even they may be same
        #the matter is for which class you are creating object
        #object of a class can acccess only the function of that class alone

