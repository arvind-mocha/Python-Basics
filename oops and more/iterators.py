#iterators they are used to print values of each iteration

#using inbuilt functions
lst=[1,2,3,4,5,6]

it=lst.__iter__()   #__iter__ is a special functions used to store values of each iteration
print(it)   #it prints address

print(it.__next__())    #__next__ is a special function prints the value of the current iteration
    #or
print(next(it))         #next is a funcionwhich is same as above special function

for i in lst:
    print(i)

print()
#now we create our own iterator

class topten:
    def __init__(self):
        self.num=1      #initialising starting value as num=1

    def __iter__(self): 
        return self


    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1

            return val
        else:
            raise StopIteration #the only way to stop iteration is by raising exception

values =topten()

print(next(values))
print(values.__next__())
for i in values:
    print(i)

