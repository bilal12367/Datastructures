

def equalSumPartition(arr, n):
    sum1 = sum(arr)
    if sum1 % 2 != 0:
        return False

    return subsetSum(arr, n, sum1//2)


def subsetSum(arr, n, target):
    if target == 0:
        return True
    if n == 0:
        return False

    if arr[n-1] <= target:
        return subsetSum(arr, n-1, target - arr[n-1]) or subsetSum(arr, n-1, target)
    else:
        return subsetSum(arr, n-1, target)


arr = [1, 5, 11, 5]

# print(equalSumPartition(arr, len(arr), 0, 0, [], []))
print(equalSumPartition(arr, len(arr) - 1))
