def eliminate(str):
    unique_str = []
    str = str.strip().split(' ')

    for i in range(len(str)):
        if str[i] not in unique_str:
            unique_str.append(str[i])


    return unique_str


input = input('enter the string')

print(eliminate(input))