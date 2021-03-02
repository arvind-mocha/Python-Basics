class art:

    def __init__(self,x,y):#it is a constructer it is printed every time obj is created
                           #init is not called but every time when a object is created it is called automatically

     self.name=x             #self indicates object and name is parameter x,instrument parameter y
     self.instrument=y

     self.x=x                #parameters can be of any name even it own name
     self.y=y
     print("hi tell me about your favorite musician")#since we have tow object it is printed two time simultaneously

    def music(self):
     print("i love",self.x,"who plays",self.instrument)
     print("i love",self.name,"who plays",self.y)

obj=art("ilayaraja","piano")
print()
obj1=art("aniruth","guitar")

print()

obj.music()     #self is obj
print()
obj1.music()    #self is obj1