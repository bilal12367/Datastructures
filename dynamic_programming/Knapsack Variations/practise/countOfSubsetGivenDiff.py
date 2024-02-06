

def countOfSubsetGivenDiff(arr, n, target):
    t = [[0 for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1
    for i in range(n+1):
        for j in range(target+1):

            if arr[i - 1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][target]


arr = [1, 3, 4, 6, 8, 10]
print(sum(arr))
diff = 2
print(countOfSubsetGivenDiff(arr, len(arr) - 1, int((sum(arr) + diff)/2)))
