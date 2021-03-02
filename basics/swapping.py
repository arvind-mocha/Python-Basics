#first way of swapping[using three variales]
a=5
b=6

temp=a
a=b
b=temp

print(a)
print(b)
print()
#second way of swapping[using only two variables]
a=20
b=30

a=a+b   #50
b=a-b   #20
a=a-b   #30

print(a)
print(b)
print()

#third way of swapping[using only two variables with xor]
a=200
b=300

a=a^b
b=a^b
a=a^b

print(a)
print(b)
print()

#fourth way[the simplst way

a=1000
b=2000

a,b=b,a

print(a)
print(b)
