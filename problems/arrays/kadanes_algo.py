import sys

def findMaxSum(arr):
    max = sys.maxsize * - 1 - 1
    sum1 = 0
    for i in range(len(arr)):
        sum1 += arr[i]
        print(sum1)
        if sum1 < 0:
            sum1 = 0
        else:
            if sum1 > max:
                max = sum1

    return max

print(findMaxSum([2,-1, 3, -1 , -1, 4, 7, -6]))