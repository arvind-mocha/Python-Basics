#run time error

try:
    print("database connection opened")
    x=int(input("enter a integer"))
    print(x)
except ZeroDivisionError as e:
    print(e,"error as occured")
except IndexError as e:
    print(e,"error as occured")
except Exception as e:
    print(e,"error as occured")
finally:
    print("database conection closed")


#user defined exception:

class speed(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class breaks(Exception):
    def __int__(self,msg):
        super.__init__(msg)

class battle:
    def __init__(self,cars):
        self.c = cars

    def race(self):
        if self.c > 80:
            raise speed('speed error :' + str(self.c))
        if self.c < 10:
            raise breaks('break error :' + str(self.c))


obj = battle(int(input()))
obj.race()
