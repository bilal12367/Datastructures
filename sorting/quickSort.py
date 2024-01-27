import random

arr=[]
for i in range(0,10000):
    arr.append(random.randint(1,20000))

def quickSort(arr):
    if(len(arr) < 2):
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if(i < pivot):
            left.append(i)
        else:
            right.append(i)
    return quickSort(left) + [pivot] + quickSort(right)


print(quickSort(arr))