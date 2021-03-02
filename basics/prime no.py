#to find prime number between betwen a range
x=int(input("enter the starting value"))
y=int(input("enter the ending value"))
for Number in range (x, y):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count=count+1      #if the no is not prime then count =1 so break if prime count =0 then it is printed
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

#check wheter the given no is prime
print()
z=int(input("enter the number"))

for i in range(2,z//2):
    if (z%i==0):
        print("not a prime")
        break
else:
    print("prime")

