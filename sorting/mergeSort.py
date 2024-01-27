import random
import math

arr = []
for i in range(0, 10000):
    arr.append(random.randint(0,20000))

def merge_sort(arr):
    if (len(arr) < 2):
        return arr
    
    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr,left,right)

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
merge_sort(arr)
print(arr)
