def partition(lst,low,high):
    i = low-1
    pivot = lst[high]

    for j in range(low,high):
        if lst[j] < pivot:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]

    lst[i+1],lst[high] = lst[high],lst[i+1]
    return i+1


def quick(lst,low,high):

    if low < high:

        pi = partition(lst,low,high)

        quick(lst,low,pi-1)
        quick(lst,pi+1,high)

lst = list(input("enter the list if elements").split(' '))
quick(lst,0,len(lst)-1)
print(lst)