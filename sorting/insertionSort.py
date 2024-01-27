import random

arr =[]
for i in range(0,10000):
    arr.append(random.randint(0,20000))

def insertionSort(arr):
    for i in range(len(arr) - 1):
        nti = arr[i+1]
        sc = i
        while(sc >= 0 and arr[sc] > nti):
            arr[sc],arr[sc+1] = arr[sc+1], arr[sc]
            sc = sc - 1
        arr[sc+1] = nti
    return arr

print(insertionSort(arr))