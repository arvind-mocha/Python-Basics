class sports:#creating a class

    def game(self):#self is object
        print("soccer")

obj=sports()#creating object

sports.game(obj)   #one way of calling class[no one use this] passing object as parameter
sports.game(obj)    #the [self] present in functions are for this purpose [self accepts only object]

obj.game() #another way of calling class[every one use this]
obj.game()


