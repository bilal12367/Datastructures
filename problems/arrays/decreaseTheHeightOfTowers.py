
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quickSort(left) + [pivot] + quickSort(right)


def decreaseTheMinHeightTowers(arr, k):
    arr = quickSort(arr)
    n = len(arr)
    mi = arr[0] + k
    ma = arr[n - 1] - k
    ans = arr[n-1] - arr[0]
    for i in range(1, n):
        mi = min(mi, arr[i] - k)
        ma = max(ma, arr[i - 1] + k)
        if mi < 0: continue
        ans = min(ans, ma - mi)

    return ans


arr = [3, 9, 16, 12, 20]
k = 6
print(decreaseTheMinHeightTowers(arr, k))
