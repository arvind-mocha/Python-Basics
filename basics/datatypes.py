name="ARVIND"

# ARVIND has 6 letters index starts from 0 ends at 5 from backwards starts from -1 ends at -5

print(name[-1])# name[-1] is D

print(name[0])# name[0] is A

#setting Limit


print(name[1:4])#prints index starting from 1 to 3 it wont print index no 4 it is an exception

print(name[0:])#prints all if no end limit

print(name[:6])#prints ARVIN and leaves D since 6th index is not in count

print(name[0:1000])#no matter what the end limit is since it is an array it just allocates 1000 spaces in the memory

#datatypes in python

        #1. NONE == which is like null

            x=None
        #2. NUMERIC which includes int float boolean complex
            x=2
            x=2.5
            x=2+i

            x=False
        #note [for those datatypes below]
        #to print each value we use for loop use for loop like this for i in range() not like this for i in list or tulpe or ect
        #3. LIST  we can have any type of data it is mutable we use[]
            x=[1,2,3,4]
            x=["hi","hello"]
            x=[1,2,"hi",4,"bye"]

        #4.TUPLE it is as same as LIST but immutable we use () but you can check the value  of concern index
            x=(1,2,3,4)
            x=("hi","hello")
            x=(1, 2, "hi", 4, "bye")
        #5. SET it is like tuple it is immutable but it does not follow a sequence it randomly arranges the value so no indexing we use {}
            x={1,2,3,4}
            x={"hi","bye","hello"}
            x = {1, 2, "hi", 4, "bye"}

        #we can type cast by using set(x) tuple(x) list(x)

        #6. STRING

        #7.DICTIONARY it is an array but strings are used as index
            x={"ARVIND":"FOOTBALL","VICKY":"TENNIS","NANDU":"KABADI"}
            x.keys()#does not take any parameter

            x.values()#does not take any parameter
                #or
            x.get("ARVIND")#takes only one parameter of keys

