

def countSumOfSubsetDp(arr, n, target):
    t = [[0 for _ in range(target+1)] for _ in range(n+1)]

    for i in range(n+1):
        t[i][0] = 1

    for i in range(n+1):
        for j in range(target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][target]


arr = [1, 1, 2, 3, 5, 7]
targetSum = 1
s1 = (sum(arr) + targetSum) / 2
if s1 % 2 != 0:
    print(0)
else:
    print(countSumOfSubsetDp(arr, len(arr)-1, int(s1)))
