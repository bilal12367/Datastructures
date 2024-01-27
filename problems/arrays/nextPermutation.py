arr =[1,2,3,4,5]
# 12354, 12435, 12453, 12534, 12543
def nextPermutation(arr):
    ind = -1
    for i in range(len(arr) - 1, -1,-1):
        ind = len(arr) - 1
        if arr[i-1] < arr[i]:
            ind = i - 1
            break
    if ind == -1:
        return arr[::-1]
    
    for i in range(len(arr) - 1, -1 ,-1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind],arr[i]
            break
    arr[ind+1:] = reversed(arr[ind+1:])
    return arr
    
start = arr.copy()
for i1 in range(1,121): 
    arr = nextPermutation(arr)
    str1 = ''
    for i in arr:
         str1 += str(i)
    str2 = ''
    for j in start:
         str2 += str(j)
    if(str1 == str2):
         print(i1)
         print(str1," = ", str2)
         break
