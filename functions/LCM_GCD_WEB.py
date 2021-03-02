def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24
print("The L.C.M. is", compute_lcm(num1, num2))

#finding GCD
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x










# finding lcm using gcd
def compute_lcm_using_gcd(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
print("The GCD is",compute_gcd(num1,num2))












#finding lcm for n no of values
def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    print(gcd)
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


l = [2, 7, 3, 9, 4]

num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)
print("lcm is",lcm)
for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])








#finding gcd for multiple values

def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x

l = [2, 4, 6,31,8]

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)
for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)
