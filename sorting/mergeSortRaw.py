import random


# def mergeSort(arr, left, right):
#     cnt = 0
#     if left >= right:
#         return cnt
#     mid = (left + right) // 2
#     cnt += mergeSort(arr, left, mid)
#     cnt += mergeSort(arr, mid + 1, right)

#     cnt += merge(arr, left, right, mid)

#     return cnt


# def merge(arr, left, right, mid):
#     leftArr = arr[left:mid+1]
#     rightArr = arr[mid+1:right+1]
#     cnt = 0
#     l = 0
#     r = 0
#     sI = left

#     while l < len(leftArr) and r < len(rightArr):
#         if leftArr[l] <= rightArr[r]:
#             arr[sI] = leftArr[l]
#             l += 1
#         else:
#             arr[sI] = rightArr[r]
#             print(rightArr)
#             cnt += len(leftArr) - l
#             r += 1
#         sI += 1

#     while l < len(leftArr):
#         arr[sI] = leftArr[l]
#         l += 1
#         sI += 1

#     while r < len(rightArr):
#         arr[sI] = rightArr[r]
#         r += 1
#         sI += 1

#     return cnt

def mergeSort(arr, left, right):
    cnt = 0
    if left >= right:
        return cnt
    mid = (left + right) // 2
    cnt += mergeSort(arr, left, mid)
    cnt += mergeSort(arr, mid + 1, right)
    cnt += merge(arr, left, right,mid)
    return cnt

def merge(arr, left, right, mid):
    cnt = 0
    l = r = 0

    leftArr = arr[left: mid+1]
    rightArr = arr[mid+1 : right+1]
    sIndex = left

    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] <= rightArr[r]:
            arr[sIndex] = leftArr[l]
            l += 1
        else:
            arr[sIndex] = rightArr[r]
            cnt += len(leftArr) - l
            r += 1
        sIndex += 1
    
    while l < len(leftArr):
        arr[sIndex] = leftArr[l]
        l += 1
        sIndex += 1
        
    while r < len(rightArr):
        arr[sIndex] = rightArr[r]
        r += 1
        sIndex += 1
    
    return cnt




arr = [random.randint(1, 30) for i in range(1, 14)]
print("Init Arr: ", arr)
# arr = [5, 3, 2, 4, 1]
print(mergeSort(arr, 0, len(arr) - 1))
print(arr)
