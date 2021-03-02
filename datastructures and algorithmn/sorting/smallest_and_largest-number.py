def small(arr,k):
    for i in range(k-1):
        arr.remove(min(arr))

    return min(arr)

def large(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))

    return max(arr)


list = [5,1,7,2,8]
arr = list.copy()
print(large(arr,5))

