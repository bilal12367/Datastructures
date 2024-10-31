import sys
def subArraySum(arr):
    maxSum = - sys.maxsize
    sum = 0
    for i in arr:
        sum = sum + i
        # If sum becomes greater than sum of prev array, sets maxSum
        if sum > maxSum:
            maxSum = sum
        else:
            # Resets
            if sum < 0:
                sum = 0
    
    return maxSum

def subArraySumDP(arr):
    maxSum = -sys.maxsize
    n = len(arr)
    dp = [0 for i in range(n + 1)]
    for i in range(n):
        dp[i] = dp[i - 1] + arr[i]
        if dp[i] > maxSum:
            maxSum = dp[i]
        if dp[i] < 0:
            dp[i] = 0

    return maxSum
arr = [4, -1, 2 ,3, -8, 1, -3, 4, -2]
# arr = [-8,-2,-1, -4, -3]
# arr = [-2 , -1]
print(subArraySumDP(arr))