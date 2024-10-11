
def bubbleSort(arr1):
    isSwapped = True
    while(isSwapped):
        isSwapped = False
        for j in range(len(arr1) - 1):
            if(arr1[j] > arr1[j+1]):
                [arr1[j],arr1[j+1]] = [arr1[j+1],arr1[j]]
                isSwapped = True
    return arr1

def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        if i != 0:
            j = i - 1
            while j >= 0:
                if(arr[j] > temp):
                    arr[j + 1],arr[j] = arr[j],arr[j+1]
                else:
                    arr[j + 1] = temp
                    break
                j = j - 1
    return arr

def selection_sort(arr1):
    n = len(arr1)
    for i in range(n - 1):
        min = i
        for j in range(i+1, n):
            if(arr1[min] > arr1[j]):
                min = j
        [arr1[min],arr1[i]] = [arr1[i],arr1[min]]
    return arr1

def compare_Arr(arr1, arr2):
    n = len(arr1)
    if(n != len(arr2)):
        return False
    
    for i in range(n):
        if(arr1[i] != arr2[i]):
            return False
    
    return True
def merge_sort(arr):
    if(len(arr) < 2):
        return arr
    
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr,left,right)

def merge(arr, left, right):
    i = j = k = 0
    while(i<len(left) and j<len(right)):
        if (left[i] < right[j]):
            arr[k] = left[i]
            i = i+1
            k = k+1
        else:
            arr[k] = right[j]
            j = j+1
            k = k+1
    while(i<len(left)):
        arr[k] = left[i]
        i = i+1
        k = k+1
    while(j<len(right)):
        arr[k] = right[j]
        j = j+1
        k = k+1
def quickSort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    return quickSort(left) + [pivot] + quickSort(right)