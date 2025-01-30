arr = [9, -3, 3, -1, 6, -5]

def longestSubarryZeroSum(arr, n, subset, max1):
    if n == 0:
        return max1
    
    if sum(subset) == 0:
        if len(subset) > max1:
            print(subset)
            max1 = len(subset)
    
    inc = longestSubarryZeroSum(arr, n - 1, subset + [arr[n-1]],max1)
    exc = longestSubarryZeroSum(arr, n - 1, subset,max1)
    return max([inc, exc])

def test(A):
    n = len(A)
    mpp = {}
    sum = maxi = 0
    for i in range(n):
        sum += A[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi

print(test(arr))
# print(longestSubarryZeroSum(arr, len(arr), [], 0))