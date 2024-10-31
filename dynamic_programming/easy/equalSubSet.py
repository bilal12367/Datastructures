

def equalSumSubset(arr, n, sum):
    if n == 0:
        return False
    if sum == 0:
        return True
    
    if arr[n - 1] <= sum:
        return equalSumSubset(arr, n - 1, sum - arr[n - 1]) or equalSumSubset(arr, n - 1, sum)


print(equalSumSubset([1,5,11,5],4, 12))