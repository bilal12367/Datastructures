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


def findMaxSumContigousSubArray(arr):
    max = (sys.maxsize * - 1) - 1
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if max < sum:
            max = sum
        if sum < 0:
            sum = 0
    return max


def findMaxSumBruteForce(arr):
    max = (sys.maxsize * - 1)-1
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if max < sum:
                max = sum
    return max


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(findMaxSumContigousSubArray(arr))
