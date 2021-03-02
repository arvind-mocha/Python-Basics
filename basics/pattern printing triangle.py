x=int(input("enter the values"))

for i in range(1,x):

    for j in range(0,i):
        print("# ",end="")
    print()

for i in range(x+1,1,-1):
    for j in range(1,i):
            print("# ",end="")
    print()
count=0
for i in range(x,0,-1):
    for j in range(x-i):
        print(" ",end=" ")      #if print("",end=" ")it a downward pyramid
        count = count + 1
    for k in range(x-count):
        print("#",end=" ")
    print()
    count=0

    for i in range()