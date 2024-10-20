from collections import deque
from Tree_Module import Node, level_order_traversal

def insert_into_min_heap(arr, val):
    arr.append(val)
    i = len(arr) - 1
    while(i > 1):
        if arr[i//2] <= val:
            arr[i // 2], arr[i] = arr[i], arr[i // 2]
            i = i // 2
        else:
            break
    return arr

if __name__ =="__main__":
    arr = [  15,      10,      8,      7,      5,      3,      1  ]
    arr = insert_into_min_heap(arr, 13)
    print(arr)
    arr = insert_into_min_heap(arr, 12)
    print(arr)

    
    
