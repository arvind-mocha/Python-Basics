#what if your function does a simple calculation[instead of wasting line use ananymous function]

f=lambda a:a*a  #it is a ananymous function

ans=f(5)
print(ans)

#more about lambda[odd or even]
#instead of writing a function and passing it as parameter pass the lambda function as parameter[only functions
#with simpe code and not going to use again must be done using lambda]
#lambda function is also a function but instead of wasting lines on a simple non reusable function we use lambda function

from functools import reduce

num=[3,4,2,1,6,4,7,9,2,3]

even=list(filter(lambda n:n%2==0,num))#filter accepts a funuction and a sequence(iterables) and based on the function
                                      #it filters the value[lambad function is not used again]

double=list(map(lambda n: n*2,even))   #map accepts a funuction and a sequence(iterables) and updates the value based
                                       #on the function[lambad function is not used again]

sum=reduce(lambda a,b:a+b,double)      #reduce accepts a funuction and a sequence(iterables) and gives a single value
                                       #output based on the function[lambad function is not used again]

print(even)
print(double)
print(sum)

# #using map seperating each alphabets from each string
# # List of strings
# l = [input("enter n no of strings")]
# m=["bat","cat","mat","lottery","bitch"]
#
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
# test = list(map(list, m))
# print(test)