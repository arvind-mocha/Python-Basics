#conditional statements indent acts as {} = blocks
if True==2:
     print("hi")
     if True != 1:
            print("how are you")
elif False==1:
     print("bye")
     if False==2:
        print("wrong")
else:
    print("sorry")

#looping Staments

#while loop
x=1
while x < 4:
    print(x)
    x=x+1

#for loop
x=["hi","bye",1,2,"stop"]

for i in x:                         #one way to use for (seperating a list,tuple,set) by their index
    print(i,end=" completed ")      #end is used to print all in same line and if needed add string after each iteration

for i in [1,2,3,"hi","hello"]:
    print(i,end="")                 #difference b/w end="" and (end=" comleted " or end=" ")

for i in range(2,2): #nothing will be printed starting and ending limit must not be the same
    print("hi")

for i in range(2,3):   #it is printed time
     print(" hi")

# for else  = it pirnt else value one time when if loop is no satisfied but
#             when the else is connetced to if then it is printed
#             for n no of time based on the i value when if is not satisfied
for i in range(0,6,2):
    if i %5==0:
        print(i)
        break
else:                       # else is connected to for not to if
    print("not found")




