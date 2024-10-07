from matrice_util import generate_arr
from sorting_algo_module import bubbleSort,compare_Arr,selection_sort
import sys

arr1 = generate_arr(10)
arr2 = arr1.copy()


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
    
arr2.sort()
print("Expected: ",arr2)

insertion_sort(arr1)


# arr2.sort()


# print(compare_Arr(arr1, arr2))

