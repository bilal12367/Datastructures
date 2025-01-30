
def subsetSumDP2(arr, target):
    n = len(arr)
    t = [[ -1 for _ in range(target + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
    for i in range(1,n + 1):
        for j in range(1,target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][target]

if __name__ == '__main__':
    arr = [6, 3, 5, 2, 4]
    target = 19
    print(subsetSumDP2(arr,target))