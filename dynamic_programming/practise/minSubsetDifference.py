import sys

def minSubsetDiff(arr, n, totalSum):
    t = [[False for _ in range(totalSum+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True

    for i in range(n+1):
        for j in range(totalSum+1):
            if i == 0:
                t[i][j] = False

            if j == 0:
                t[i][j] = True

            if arr[i - 1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    v = []
    for i in range(len(t[n])):
        if t[n][i] == True:
            v.append(i)
    mn = sys.maxsize -1 * -1
    for i in v:
        mn = min(mn, abs(totalSum - 2 * i))

    return mn

arr = [1, 6, 11, 5]

print(minSubsetDiff(arr, len(arr), sum(arr)))
