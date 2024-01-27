import random

arr=[]
for i in range(0,10000):
    arr.append(random.randint(0,20000))

def selectionSort(arr):
    for i in range(len(arr)):
        cm = i
        for ci in range(i, len(arr)):
            if(arr[ci] < arr[cm]):
                cm = ci
        arr[i], arr[cm] = arr[cm], arr[i]
    return arr

print(selectionSort(arr))