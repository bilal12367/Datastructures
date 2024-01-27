import random
arr =[]
for i in range(0,10000):
    arr.append(random.randint(0,20000))

def bubbleSort(arr):
    isSwapped = True
    while(isSwapped):
        isSwapped = False
        for i in range(len(arr) - 1):
            if(arr[i] > arr[i+1]):
                arr[i+1], arr[i] = arr[i], arr[i+1]
                isSwapped = True
    return arr


print(bubbleSort(arr))
        