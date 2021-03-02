#passing list as parameter (odd or even)


def check(lst):
    count = 0
    count1 = 0
    for i in lst:
        if i % 2==0:
            count += 1

        else:
            count1 += 1

    return count,count1

#to get a list input
# create an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
print("enter the values int the list")
for i in range(0, n):
    ele = int(input())
    lst.append(ele)  # adding the element to the list
check(lst)
print(lst)
even,odd=check(lst)
print("even : {} and odd : {}".format(even,odd)) #format puts value into {}


#passing list as parameter (strings)
above=0
below=0
def String(str):
    x=globals()['above']
    y=globals()['below']
    for i in range(len(str)):
        if len(str[i]) < 5:
            x += 1

        else:
            y +=1
    return x,y

str=[]
no=int(input("enter the no of srings"))
print("enter the values")
for i in range(0,no):
    value=input()
    str.append(value)

less,more=String(str)

print("more than five : {} and less than five : {}".format(more,less))
