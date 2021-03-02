#inner calsses are basically used when you are creating
# another class but it is only useful for your previous class

class student:

    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        self.lap=self.laptop("RTX 2080ti and","quad cooler")      #creating object for inner class
                                                                  #inside outter class[followed by all]

        self.lap1=self.laptop("intel and","single fan")     #even if you create object ouside
                                                            #you have to create object inside outter class again
                                                            #so why creating object outside is a unusual
                                                            #and unwanted way to be done


    def show(self):
        print(self.name,self.dept)
        print(self.lap.show())    #current object.object of inner class.method = self.lap.brand
        print(self.lap.graphics,self.lap.fan)
        print()
        print(self.lap1.show())
        print(self.lap1.graphics, self.lap1.fan)
    class laptop:
            def __init__(self,graphics,fan):
                self.brand="lenova"
                self.specs="i9"
                self.graphics=graphics
                self.fan=fan

            def show(self):
                return self.brand,self.specs




obj=student("Arvind","CSE") #creating object for outter class

lap1=student.laptop("intel and","single fan")  #creating object for inner class refering outter class itself
                                               #[unusual way] executes as same as above statment lap1
obj.show()#calling outter class


