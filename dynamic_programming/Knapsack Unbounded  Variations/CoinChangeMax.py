import sys

# def coinChangeMaxWays(arr, n, target):
#     t = [[0 for _ in range(target+1)] for _ in range(n+1)]

#     for i in range(n+1):
#         for j in range(target+1):
#             if j == 0:
#                 t[i][j] = 1

#             if i == 0:
#                 t[i][j] = 0
#     for i in range(n+1):
#         for j in range(target+1):
#             if arr[i - 1] <= j:
#                 t[i][j] = t[i][j - arr[i - 1]] + t[i - 1][j]
#             else:
#                 t[i][j] = t[i - 1][j]
#     return t[n][target]


def coinChangeMaxWays(arr, n, target, subset):
    if target == 0:
        return len(subset)

    if n == 0:
        return sys.maxsize

    if arr[n - 1] <= target:
        return min(coinChangeMaxWays(arr, n, target - arr[n - 1], subset + [arr[n-1]]), coinChangeMaxWays(arr, n - 1, target, subset))
    else:
        return coinChangeMaxWays(arr, n - 1, target, subset)


if __name__ == '__main__':
    arr = [1, 2, 3]
    target = 4
    print(coinChangeMaxWays(arr, len(arr), target, []))
