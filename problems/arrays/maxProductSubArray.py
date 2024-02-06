import sys


def maxProdSubArray(arr):
    max = 1
    for i in range(len(arr)):
        prod = 1
        for j in range(i, len(arr)):
            prod *= abs(arr[j])
            if max < prod:
                max = prod

    return max


def maxProductOpt(arr):
    max1 = sys.maxsize - 1 * -1
    prod = 1
    for i in range(len(arr)):
        prod *= abs(arr[i])
        if prod == 0:
            prod = 1
        max1 = max(max1, prod)


if __name__ == '__main__':
    print(maxProdSubArray([-1, -3, -10, 0, 60]))
