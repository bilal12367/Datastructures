import random

arr=[]
for i in range(0,100):
    arr.append(random.randint(1,200))

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

def quickSort1(arr):
    if(len(arr) < 2):
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
    return quickSort1(left) + [pivot] + quickSort1(right)

print(quickSort1(arr))