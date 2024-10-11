from matrice_util import generate_arr
from sorting_algo_module import bubbleSort,compare_Arr,selection_sort,insertion_sort,quickSort,merge_sort
from problems_module import findSecondLargeestAndSmallest
import sys
arr1 = generate_arr(20, 2)
arr2 = arr1.copy()

print(arr1)
low = 0
high = len(arr1) - 1
for i in range(1,len(arr1)):
    if arr1[i] == 0:
        arr1[i]