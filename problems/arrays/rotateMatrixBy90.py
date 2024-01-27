arr = [[1,2,3, 4],[5,6,7, 8],[9,10,11,12]]
resArr = []

# Rotating by 90 clockwise
def rotateBy90Clockwise(arr):
    for i in range(0, len(arr[0])): # i 4
        list1 = []
        for j in range(0, len(arr)): # j 3
            k = len(arr) - j - 1
            list1.append(arr[k][i])
        resArr.append(list1)
    return resArr

# Rotating by 90 anti clockwise
def rotateBy90AntiClockwise(arr):
    resArr = []
    for i in range(0, len(arr[0])): # i 4
        list1 = []
        for j in range(0, len(arr)): # j 3
            k = len(arr[j]) - 1 - i
            list1.append(arr[j][k])
        resArr.append(list1)
    return resArr

# Printing the 2d arr
def printArr(arr):
    for i in arr:
        str1 = '['
        for j in i:
            str1 += str(j) + ','
        str1 += ']'
        print(str1)
    return arr

printArr(rotateBy90AntiClockwise(arr))