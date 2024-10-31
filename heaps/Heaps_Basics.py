

arr = [70 , 60, 55, 53, 45, 43, 35, 32, 28]
arr2 = arr.copy()
def insert_into_heap(arr, val):
    arr.append(val)
    i = len(arr) - 1
    parent = (i - 1) // 2
    while i > 0 and arr[parent] < arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent
        parent = (i - 1)// 2
    
    print(arr)
insert_into_heap(arr, 65)