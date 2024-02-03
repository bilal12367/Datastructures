arr = [1, 2, 3, 5, 4]
# 12354, 12435, 12453, 12534, 12543


def nextPermutation(arr):
    ind = -1
    for i in range(len(arr) - 1, -1, -1):
        ind = len(arr) - 1
        if arr[i-1] < arr[i]:
            ind = i - 1
            break
    if ind == -1:
        return arr[::-1]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break
    arr[ind+1:] = reversed(arr[ind+1:])
    return arr


def nextPermutation2(arr):
    ind = -1

    # Find Break Point
    for i in range(len(arr) - 1, -1, -1):
        if arr[i - 1] < arr[i]:
            ind = i - 1
            break;

    if ind == -1: return arr[::-1]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > arr[ind]:
            arr[i] , arr[ind] = arr[ind] , arr[i]
            break
    arr[ind+1:] = reversed(arr[ind+1:])
    return arr
    

print(nextPermutation2(arr))
