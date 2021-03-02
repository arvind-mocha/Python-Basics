# how to import and use a package (there are many functions in a package)

import math

math.factorial(5)

math.floor(5.44)

x=[1,2,3,4]

y=math.fsum(x)

#instead of pachage.function we can assusme the package as anything

import math as m

m.fsum(x)

m.floor(2.44)

#if you know what function to use and dont need all th functions in the package

from math import pow,fsum,floor

fsum(x)

floor(3.44)

#to find functions present in a package

help(math)