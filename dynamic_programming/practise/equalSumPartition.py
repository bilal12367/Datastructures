
def equalSum(arr, target):
    n = len(arr)

    t = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][target]


if __name__ == '__main__':
    arr = [1,1,5,11,6]
    # print(can_partition(arr, len(arr) - 1, 0, 0, [],[]))
    # print(equalSum(arr, len(arr), 0, 0, [], []))
    sum1 = sum(arr)
    print(sum1)
    if sum1 % 2 == 0:
        target = int(sum1 / 2)
        print(equalSum(arr, target))
    else:
        print(False)
