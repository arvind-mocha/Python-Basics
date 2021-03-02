import math

def search(lst,value):
    answer = None
    mid = math.floor(len(inputs)/2)
    if value == lst[mid]:
        return 'found at {}'.format(mid)

    elif value > lst[mid]:
        for i in range(mid+1,len(lst)):
            print(i)
            if value == lst[i]:
                answer = i
                return 'found at {}'.format(answer)
            else:
                answer = 'not found'

    else:
        for i in range(mid-1,-1,-1):
            if value == lst[i]:
                answer = i
                return 'found at {}'.format(answer)
            else:
                answer = 'not found'

    return answer

inputs = list(input('enter the list').split(' '))
inputs = sorted(inputs)
value = input('enter the element you need to search')

print(search(inputs,value))




