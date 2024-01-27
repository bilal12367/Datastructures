# Find max sum  of sub array
import sys


def findMaxSumSubArray(arr):
    sum = 0
    maxI = arr[0]
    arr1 = []
    for i in arr:
        sum += i
        arr1.append(i)
        if (sum > maxI):
            maxI = sum

        if (sum < 0):
            arr1 = []
            sum = 0
    
    return maxI, arr1

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(findMaxSumSubArray(arr))
