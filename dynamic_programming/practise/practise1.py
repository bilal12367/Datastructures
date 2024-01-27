
def knapsack(arr, valArr, W, n):
    if W == 0:
        return 0
    if n == 0:
        return 0

    if arr[n-1] > W:
        return knapsack(arr, valArr, W, n-1)
    else:
        return max(knapsack(arr, valArr, W, n-1), valArr[n-1] + knapsack(arr, valArr, W - arr[n-1], n-1))


def subsetSum(arr, n, target, subset):
    if target == 0:
        return subset

    if n == 0:
        return False

    if arr[n-1] > target:
        return subsetSum(arr, n-1, target, subset)
    else:
        return subsetSum(arr, n-1, target - arr[n-1], subset + [arr[n-1]]) or subsetSum(arr, n-1, target, subset)


def can_partition(nums, n, sum1, sum2, arr1, arr2):
    if sum1 == sum2 and len(arr1) > 0:
        return [arr1, arr2]

    if n < 0:
        return False

    res1 = can_partition(
        nums, n-1, sum1 + nums[n], sum2, arr1 + [nums[n]], arr2)
    res2 = can_partition(nums, n-1, sum1, sum2 +
                         nums[n], arr1, arr2 + [nums[n]])

    res1 = res1 or res2
    return res1


def subsetSum2(arr3, n, target, subset):
    if target == 0:
        return subset
    if n < 0:
        return False
    res1 = subsetSum2(arr3, n-1, target - arr3[n], subset + [arr3[n]])
    res2 = subsetSum2(arr3, n-1, target, subset)
    return res1 or res2


def knapsack2(wtArr, valArr, W, n, subset):
    if W == 0 or n == 0:
        return 0, subset

    if wtArr[n] > W:
        return knapsack2(wtArr, valArr, W, n - 1, subset)
    else:
        res1, s1 = knapsack2(wtArr, valArr, W, n - 1, subset)
        res2, s2 = knapsack2(wtArr, valArr, W -
                             wtArr[n], n-1, subset + [valArr[n]])
        if res1 > (res2 + valArr[n]):
            return res1, s1
        else:
            return res2 + valArr[n], s2


if __name__ == '__main__':
    wtArr = [1, 2, 3, 4]
    valArr = [10, 22, 32, 43]
    W = 5
    n = len(wtArr)

    arr = [1, 9, 3, 4]
    target = 14

    arr1 = [1, 5, 11, 5]
    print(knapsack2(wtArr, valArr, W, n - 1, []))
    # print(subsetSum2(arr, len(arr) - 1, target, []))
    # print(can_partition(arr1, len(arr1) - 1,0,0, [],[]))
