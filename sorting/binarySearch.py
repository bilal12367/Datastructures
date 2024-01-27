import math
import random
arr = [random.randint(0, 1000) for _ in range(100)]
targetInd = random.randint(0, 99)
arr.sort()
num = arr[targetInd]

def binarySearch(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        current = arr[mid]

        if target < current:
            return binarySearch(arr, left, mid - 1, target)
        elif target > current:
            return binarySearch(arr, mid + 1 , right, target)
        else:
            return mid
    else:
        return -1

print(binarySearch(arr, 0, len(arr) - 1, num))
