import sys


def bestTimeToSellStock(arr):
    minTemp = arr[0]
    res = 0
    for i in range(1, len(arr)):
        minTemp = min(minTemp, arr[i])

        res = max(res, arr[i] - minTemp)

    return res 


arr = [8, 3, 6, 1, 4, 7]

print(bestTimeToSellStock(arr))