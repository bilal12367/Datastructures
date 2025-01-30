import random
import math

arr = []
for i in range(0, 30):
    arr.append(random.randint(0,200))

def merge_sort(arr):
    if (len(arr) < 2):
        return arr
    
    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr,left,right)
def merge2(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i] 
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
def merge(arr,left,right):
    i = j = k = 0
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    
    while(i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while(j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage:


def merge_sort2(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort2(left)
    merge_sort2(right)
    merge2(arr, left, right)


test = arr.copy()
test.sort()
merge_sort2(arr)
print(arr == test)
print(arr)
print(test)