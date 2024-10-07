
def bubbleSort(arr1):
    isSwapped = True
    while(isSwapped):
        isSwapped = False
        for j in range(len(arr1) - 1):
            if(arr1[j] > arr1[j+1]):
                [arr1[j],arr1[j+1]] = [arr1[j+1],arr1[j]]
                isSwapped = True
    return arr1

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