#there are basically three types of method

class me:

    name="Arvind"

    def sports(self):   #it is a instance method since you have self which points current object specific
        self.game="shuttle"
        return self.game

    @classmethod    #you are indicating it is a class method now it is class specific not object
                    #you need to declare @classmethod else you need to pass a parameter for cls
    def myage(cls):
        age_now=20
        age_before=19
        return age_now,age_before

    @staticmethod   #you are indicating it as static method it is not class and object dependent or specific
                    #it is alo class specific
    def music():
        instruments="keyboard"
        return instruments

obj1=me()

obj1.sports() #calling instance method

print(obj1.game)    #printing thing in insatnce method

print(me.myage())   #printing things in class method they need not to be called

print(me.music())   #printing things in static method they need not to be called