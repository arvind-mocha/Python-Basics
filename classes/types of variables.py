#there are bsically wo types of variables

class cars:
    wheels=4    #class variables they are shared by each object they are also called static variable

    def __init__(self):
        self.mil=10     #object/instance variables they are also shared by ach objct


obj=cars()
obj1=cars()

obj.wheel=200   #obj cant represent wheel since it belonged to class not function

obj.mil=300     #change is only to the particular object

print(obj.mil,cars.wheels)
print(obj1.mil,cars.wheels)
print()

cars.wheels=600 #cars is the class name so it can represet wheels change happens to every object since all
                #methods belongs to a particular class

print(obj.mil,cars.wheels)
print(obj1.mil,cars.wheels)
