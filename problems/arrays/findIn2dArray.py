arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

n = 4


def binarySearch2dArr(arr, num):
    n = len(arr)
    m = len(arr[0])

    left = 0
    right = (n*m) - 1
    while (left <= right):
        mid = (left+right) // 2
        row = mid // m
        col = mid % m
        
        if(arr[row][col] == num):
            return row,col
        elif(arr[row][col] < num):
            left = mid + 1
        else:
            right = mid - 1
        
    return -1,-1


print(binarySearch2dArr(arr, n))
