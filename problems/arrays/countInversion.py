

def countInversion(arr):
    count = 0
    for i in range(len(arr)):
        current = arr[i]
        for j in range(i+1, len(arr)):
            if current > arr[j]:
                count += 1

    return count

# Optimal Solution


def mergeSort(arr, left, right):
    mid = (left + right) // 2
    cnt = 0
    if left >= right:
        return cnt

    cnt += mergeSort(arr, left, mid)
    cnt += mergeSort(arr, mid + 1, right)

    cnt += merge(arr, left, right, mid)
    return cnt


def merge(arr, start, end, mid):
    left = start
    right = mid + 1
    sortedArr = []
    cnt = 0
    while left <= mid and right < end:
        if arr[left] > arr[right]:
            cnt += (mid - left + 1)
            sortedArr.append(arr[right])
            right += 1
        else:
            sortedArr.append(arr[left])
            left += 1
    
    while left <= mid:
        sortedArr.append(arr[left])
        left += 1

    while right < end:
        sortedArr.append(arr[right])
        right += 1

    return cnt


arr = [6, 5, 3, 2, 4, 1]


print(countInversion(arr))
