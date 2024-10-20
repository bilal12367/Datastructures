import random as ran

def generate_arr(m,n):
    arr = []
    for i in range(m):
        arr.append(ran.randint(0,n))
    return arr


max_heap = [70, 60, 65, 53, 58, 46, 35, 27, 31]

def max_heapify(arr, n, i):
    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)

def remove_max(arr,n):
    temp = arr[0]
    arr[0] = arr[n - 1]
    arr.pop()
    max_heapify(arr,n - 1,0)
    return temp

def build_heap(arr):
    n = len(arr)

    for i in range( n// 2, -1, -1) :
        max_heapify(arr, n, i)
    stArr = []
    while len(arr) > 0:
        stArr.append(remove_max(arr, len(arr)))
    return stArr



arr = generate_arr(1000, 3000)
print(build_heap(arr))