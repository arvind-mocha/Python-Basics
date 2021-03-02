import math

def search(lst,value,jump):
    answer = None
    for i in range(0,len(lst),jump):
        if value == lst[i]:
            return f'found at {i}'


        elif lst[i] > value:
            for j in range(i,i-jump-1,-1):
                if value == lst[j]:
                    return f'found at {j}'
                else:
                    answer = 'not found'

    return answer


inputs = list(input('enter the list').split(" "))
value = input('enter the element to search')
jump = math.floor(len(inputs) / 4)

print(search(inputs,value,jump))



