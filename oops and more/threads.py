#as same as java[thread is a class]

from threading import * #this package contains threading function
from time import *  #it contains function like sleep


class hello(Thread):    #inheriting inbuilt super class Thread
    def run(self) :     #thread accepts only to define this method
        for i in range(0,5):
            print("hello")
            print(active_count())
            sleep(3)        #makes the function to wait for 1 sec so that the other function can get workspace fo execution

class world(Thread):
    def run(self):
        for i in range(0,5):
            print("world")
            print(active_count())
            sleep(3)


obj=hello()
obj1=world()

obj1.start()
sleep(3)     #we need to make these objects to wake because what if they both wake up at the same time
obj.start() #run method can only be called by start method in threads

obj.join()      #by default there is a main thread which is always active so to make it wait join function is used
obj1.join()
print("bye")
print(active_count())

