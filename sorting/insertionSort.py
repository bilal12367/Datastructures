import random

arr =[]
for i in range(0,20):
    arr.append(random.randint(0,100))

def insertionSort(arr):
    for i in range(len(arr) - 1):
        nti = arr[i+1]
        sc = i
        while(sc >= 0 and arr[sc] > nti):
            arr[sc],arr[sc+1] = arr[sc+1], arr[sc]
            sc = sc - 1
        arr[sc+1] = nti
    return arr

def insertionSort2(arr):
    for i in range(1,len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

test = insertionSort2(arr.copy())
arr.sort()
print(arr)
print(test)

assert arr == test, "Failed"
print("Test Passed!!")
