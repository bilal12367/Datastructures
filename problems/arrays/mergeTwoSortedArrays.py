import random
def generateArr():
    arr = []
    for i in range(1, 400):
        if(random.randint(0,3) == 0):
            arr.append(i)
        else:
            continue
    return arr

arr1 = generateArr()
arr2 = generateArr()
print("Arr1:" ,arr1)
print("Arr2:", arr2)
print("=====================")

def mergeTwoSortedArr(arr1,arr2):    
    i = j = k = 0
    sortedArr = []

    while(i<len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1
        
    sortedArr += arr1[i:]
    sortedArr += arr2[j:]
    return sortedArr

print(mergeTwoSortedArr(arr1,arr2))