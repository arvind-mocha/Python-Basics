def search(lst,value):
    for i in range(len(lst)):
        if value == lst[i]:
            return f'found at {i}'
        else:
            return 'not found'


inputs = list(input('enter the list').split(" "))
value = input('enter the element to search')

print(search(inputs,value))