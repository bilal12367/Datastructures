
def subsetSum(arr, n, target, subset):
    if target == 0:
        print(subset)
        return True

    if n == 0:
        return False
    if arr[n-1] <= target:
        return subsetSum(arr, n-1, target - arr[n-1], subset + [arr[n-1]]) or subsetSum(arr, n-1, target, subset)
    else:
        return subsetSum(arr, n-1, target, subset)


def countOfSubsetSum(arr, n, target, subset):
    if target == 0:
        return 1
    if n == 0:
        return 0

    if arr[n-1] <= target:
        return sum([countOfSubsetSum(arr, n-1, target - arr[n-1]),  countOfSubsetSum(arr, n-1, target)])
    else:
        return countOfSubsetSum(arr, n-1, target)

def equalSumPartition(arr, n, sum1, sum2, s1, s2):
    if sum1 == sum2 and len(s1) > 0:
        return [s1, s2]
    if n == 0:
        return False
    
    first_include = equalSumPartition(arr, n - 1, sum1 + arr[n - 1], sum2, s1 + [arr[n-1]], s2)
    second_include = equalSumPartition(arr, n - 1, sum1, sum2 + arr[n - 1], s1, s2 + [arr[n-1]])
    return first_include or second_include

def knapsack(arr, val, W, n):
    if W == 0 or n==0:
        return 0
    
    if arr[n-1] <= W:
        return max(knapsack(arr, val, W, n - 1), knapsack(arr, val, W - arr[n-1],n-1) + val[n-1])
    else:
        return knapsack(arr, val, W, n-1)

if __name__ == "__main__":
    # arr = [1, 1, 2, 3, 4, 9, 6]
    # target = 15
    # print(countOfSubsetSum(arr, len(arr), target))

    # arr1 = [1, 5, 11, 5]
    # print(equalSumPartition(arr1, len(arr1), 0 , 0 ,[], []))

    arr2 = [1,2,3,4]
    val = [10, 22, 32, 43]
    print(knapsack(arr2, val, 5, len(arr2)))
