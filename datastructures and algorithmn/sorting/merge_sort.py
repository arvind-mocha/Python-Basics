#index of array which is a parameter is mutable but the whole array is not mutable

def merge(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        merge(left)
        merge(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                lst[k] = left[i]
                i += 1

            else:
                lst[k] = right[j];
                j +=1

            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


inputs = list(input('enter the list to be sorted').split(' '))
merge(inputs)
print(inputs)

