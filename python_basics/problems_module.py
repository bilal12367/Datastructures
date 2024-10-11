import sys
def findSecondLargeestAndSmallest(arr):
    max = - sys.maxsize
    min = sys.maxsize
    secondMax = secondMin = 0
    for i in arr:
        if i > max:
            secondMax = max
            max = i
        elif( i > secondMax and i != max):
            secondMax = i
        
        if i < min:
            secondMin = min
            min = i
        elif (i < secondMin and i != min):
            secondMin = i
        
    print("Max: ", max, " Second Max: ",secondMax)
    print("Min: ", min, " Second Min: ",secondMin)


def rotateArr(arr,cnt,dir):
    if(dir == 'left'):
        for i in range(cnt):
            item = arr.pop(0)
            arr.append(item)
    else:
        for i in range(cnt):
            item = arr.pop(len(arr) - 1)
            arr.insert(0,item)
    
    print(arr)