import random
arr =[]
for i in range(0,100):
    arr.append(random.randint(0,200))

def bubbleSort(arr):
    isSwapped = True
    while(isSwapped):
        isSwapped = False
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i+1]):
                arr[i+1], arr[i] = arr[i], arr[i+1]
                isSwapped = True
    return arr

def bubbleSort1(arr):
    isSwap = True
    n = len(arr)
    while(isSwap):
        isSwap = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i + 1] = arr[i + 1],arr[i]
                isSwap = True
    return arr
print(bubbleSort1(arr))
        