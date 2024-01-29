

def countOfSubsetSum(arr, n, target):
    if target == 0:
        return 1
    if n == 0:
        return 0

    if arr[n-1] <= target:
        return (countOfSubsetSum(arr, n-1, target - arr[n-1]) + countOfSubsetSum(arr, n-1, target))
    else:
        return countOfSubsetSum(arr, n-1, target)


def countOfSubsetSumDP(arr, n, target):
    t = [[0 for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                t[i][j] = 0

            if arr[i - 1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][target]


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(countOfSubsetSum(arr, len(arr), 12))
print(countOfSubsetSumDP(arr, len(arr) - 1, 12))
